 ########################---------------BASIC INFO -------------#########################
 
 First:  create a enviroment  for a project In ANACONDA
           
	ANACONDA-->CMD.exe.prompt----> conda create --name YT-env  python=3.9
				       conda activate YT-env

	Libraries needed         ----> conda install pandas;
				-----> conda install seaborn;
				-----> conda install openpyxl; # for  output in excel 
				-----> conda install google-api-python-client;


Second: Generate A API KEY 
  		
        Console.Developer.google.com ---->Library--> Youtube data API Key---->Enable APIKey----->Credentials---->Copy API Key
	
	Goto Youtube data api  page --> References there you will find all the methods and other stuffs


Third : Use Json Formatter  and validator to find the  proper elementId in hirearchy of  return response Output
