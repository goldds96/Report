# Firmware
Firmware file is attached.




# Overview  

**Vendor** : Tenda


**Product** : AC18 Router


**Vulnerability Type** : Command Injection  


**Affected Version** : Firmware version = V15.03.05.19


**Description** :  
A Command Injection vulnerability exists in the **formWriteFacMac** of the **httpd** binary in the **Tenda AC18** router.  

An authenticated user can send a POST request to the **/goform/WriteFacMac** endpoint via the web interface.  

The transmitted parameter **"mac"** is stored in the **mac** variable through **sub_2ba8c** in the **formWriteFacMac** function, and the **mac** variable passed to the **doSystemCmd** function without any validation.  

As a result, attacker can execute OS commands with root privileges.  

![image](https://github.com/user-attachments/assets/2e2e6d6e-f57b-44d2-a56e-af1a3920ec9f)

![image](https://github.com/user-attachments/assets/3ce58748-2643-4592-b0b2-73625146c71a)
