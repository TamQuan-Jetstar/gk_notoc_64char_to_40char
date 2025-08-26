# notoc-acars-integration

Python application to convert 64CHAR NOTOC to a ACARS Printer compatible 40CHAR NOTOC for Jetstar Japan GK.

Retrieves 64CHAR NOTOC Messages from
```
\\corp\operations$\OPSDATA\FIRSTLOAD\GK_NOTOC_ACARS_64CHAR 
```

Transformed 40CHAR NOTOC Messages are stored in  
```
\\corp.jetstar.com\operations$\OPSDATA\GK_NOTOC_File\PROD
```

Transformed 40CHAR and untransformed 64CHAR NOTOC Messages are archived in
```
\\corp.jetstar.com\operations$\OPSDATA\GK_NOTOC_File\ARCHIVE
```
