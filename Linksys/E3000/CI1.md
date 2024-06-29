## Linksys E3000 OS Command Injection Vulnerability


**Vendor** : Linksys   

**Product** : E3000 Router 

**Firmware Link** : You can download firmware at (https://downloads.linksys.com/downloads/firmware/FW_E3000_1.0.06.002_US_20140409_code.bin)



## Detailed Description

 
**Vulnerability Type** : OS Command Injection  

**Affected Version** : Firmware version = v1.0.06.002

**Description** : Unauthenticated remote code execution vulnerability exists in **cgibin** binary in **DIR-845L** router firmware **version ≤ v1.01KRb03**. In **soapcgi_main** function, variable **v19** is the contents behind **‘service=’** in the **REQUEST_URI** environment variable. Format **v19** to **byte_434BB0**, and execute system, resulting in command execution.

