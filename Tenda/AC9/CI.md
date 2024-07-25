# Firmware
You can download firmware at https://downloads.linksys.com/downloads/firmware/1224666604712/FW_E1500_v1.0.06.001_US_20140327_code.bin




# Overview  

**Vendor** : Linksys


**Product** : E1500 Router


**Vulnerability Type** : Command Injection  


**Affected Version** : Firmware version <= v1.0.06.001  


**Description** :  
A Command Injection vulnerability exists in the **do_upgrade_post function** of the **httpd** binary in the **Linksys E1500** router.  

An authenticated user can send a POST request to the **apply.cgi** endpoint via the web interface to change the UI language.  

The transmitted parameter is stored in the **v4** variable through **nvram_get("detect_lang")** in the **do_upgrade_post** function, and the **v4** variable is formatted into **v15** through **snprintf** and then passed to the **system** function without any validation.  

As a result, an authenticated attacker can execute OS commands with root privileges.  

This vulnerability is the same as **CVE-2021-25310** and has also been found in the Linksys E1500.

![Untitled](https://github.com/user-attachments/assets/6d8f2d41-8274-4bf6-b260-688c07c30220)

![Untitled](https://github.com/user-attachments/assets/ea382dd6-3264-4ce2-b674-c3736bec178d)
