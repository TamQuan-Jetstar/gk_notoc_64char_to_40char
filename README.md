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


Dev Information:
Converted to exe with py2exe.com then moved the config_files folder into the _internal folder 