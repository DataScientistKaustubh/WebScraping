# Before Starting Here  we have To install The Three External Packages
'''
1) bs4 ie  Beautiful Soup
2) requests
3)openpyxl (To Load Data in a Excel File)
'''

from logging import exception
from bs4 import BeautifulSoup
import requests, openpyxl
excel=openpyxl.Workbook()
print(excel.sheetnames)  # to print Excel sheet name
sheet=excel.active       # to get the Active Sheet
sheet.title='Top Rated Movies'# to change Active Sheet title
print(excel.sheetnames)
sheet.append(['Rank','Movie Name', 'Year Of Release','IMDB Rating']) #To Create  Column Names in a Excel

try:

    source = requests.get('https://www.imdb.com/chart/top')     #  To Get the Site HTML Code in  Python
    source.raise_for_status()                                   # Shows if any Errors are there

    soup = BeautifulSoup(source.text,'html.parser')             # To Get the Site HTML Code in  Python
 #   print(soup)


    movies = soup.find('tbody',class_="lister-list").findAll('tr') # To Get the Whole Data Present inside the tbody Tag
  #  print(len(movies))

    for movie in movies:
            name = movie.find('td',class_='titleColumn').a.text    # To get the data in name  ie of movie name
            rank = movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]  # To get the data in rank  ie of movie Rank
            year = movie.find('td',class_='titleColumn').span.text.strip('()')    # To get the data in year  ie of movie year
            rating =movie.find('td',class_="ratingColumn imdbRating").strong.text # To get the data of rating  ie of movie Rating
            print(rank, name, year, rating)
            
            sheet.append([rank, name, year, rating])      # To add the data in the EXCEL

except exception as e:
    print(e)
    
excel.save('IMDB Movie Rating')      #To save Excel in Folder Where Code is present
