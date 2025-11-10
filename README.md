# gk_notoc_64char_to_40char

Python application to convert 64CHAR NOTOC to a ACARS Printer compatible 40CHAR NOTOC for Jetstar Japan GK.

Retrieves 64CHAR NOTOC Messages from
```
\\corp\operations$\OPSDATA\FIRSTLOAD_GK\NOTOC_File\PROD
```


Transformed 40CHAR NOTOC Messages are stored in  
```
\\corp\operations$\OPSDATA\FIRSTLOAD_GK\NOTOC_Parsed_File\PROD
```

Transformed 40CHAR and untransformed 64CHAR NOTOC Messages are archived in
```
\\corp\operations$\OPSDATA\FIRSTLOAD_GK\NOTOC_Archived\PROD
```

Deployment steps:
 - Zip the CONTENTS of the src folder (config_files, file_handling, logger, notoc_builder, notoc_parser, text_handling, create_config.py, create_modules.py, main.py, start.py)
 - Open a browser to py2exe.com/convert
 - Drag that zip file into the drop-off box on the new browser
 - Wait for the conversion to be complee and download the result
 - This outputs a exe file and a _internal folder
 - Copy the config_files folder and paste it into the _internal folder.
 - Move both the exe file and the _internal folder to a server and deploy with Task Scheduler
 - Within task scheduler, run the exe file with the argument "test" or "prd" to use the correct NAS locations. Calling the exe file with no argument will default to prod.

Note: there are many other ways to convert python code to exe, such as with pyinstaller --onefile, but the above approach has the simplest dependecies. Note that there are configuration files with relative paths that need to be included when using a different conversion approach.