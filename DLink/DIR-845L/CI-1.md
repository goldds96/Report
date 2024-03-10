## D-Link DIR-845L OS Command Injection Vulnerability

**Credit** : 주송아 (본인 이메일 추가)  

**Vendor** : DLink  

**Product** : DIR-815 Router 

**Firmware Link** : Firmware file is attached. Or you can download firmware at https://www.mydlink.co.kr/2013/beta_board/product_detail.php?no=119&model=DIR-815

![Untitled](https://github.com/goldds96/Report/assets/86287862/825ee633-8b3a-48ce-88a8-9e65db8d2f4b)



## Detailed Description

 
**Vulnerability Type** : OS Command Injection  

**Affected Version** : Firmware version <= v1.01KRb03  

**Description** : Unauthenticated remote code execution vulnerability exists in **cgibin** binary in **DIR-845L** router firmware **version ≤ v1.01KRb03**. In **soapcgi_main** function, variable **v19** is the contents behind **‘service=’** in the **REQUEST_URI** environment variable. Format **v19** to **byte_434BB0**, and execute system, resulting in command execution.

![Untitled](https://github.com/goldds96/Report/assets/86287862/97265845-c621-4787-8216-cfb3e07a79ab)


## PoC
PoC code is attached.  
To reproduce this vulnerability, you can emulate firmware by using FirmAE(https://github.com/pr0v3rbs/FirmAE)  

![Untitled](https://github.com/goldds96/Report/assets/86287862/b7761c61-8356-4068-83e2-fd3cf32cd2da)


If emulation is success, you can access web interface  

![Untitled](https://github.com/goldds96/Report/assets/86287862/2ca2e0c7-778e-4b2f-aa40-da76b5e28f42)

Finally, run the PoC code.  

![Untitled](https://github.com/goldds96/Report/assets/86287862/42c6a846-45b2-4695-9527-8d3d3c407697)
