# Firmware
Firmware file is attached.




# Overview  

**Vendor** : Tenda


**Product** : AC9 Router


**Vulnerability Type** : Command Injection  


**Affected Version** : Firmware version = V15.03.06.42 


**Description** :  
A Command Injection vulnerability exists in the **formWriteFacMac** of the **httpd** binary in the **Tenda AC9** router.  

An authenticated user can send a POST request to the **/goform/WriteFacMac** endpoint via the web interface.  

The transmitted parameter **"mac"** is stored in the **mac** variable through **websGetVar** in the **formWriteFacMac** function, and the **mac** variable passed to the **doSystemCmd** function without any validation.  

As a result, an authenticated attacker can execute OS commands with root privileges.  


![image](https://github.com/user-attachments/assets/56360f24-a7fa-43f6-a47b-067529e2af76)


![image](https://github.com/user-attachments/assets/85b0331b-c0d1-4e1a-b1f1-f0ce32c420b7)

