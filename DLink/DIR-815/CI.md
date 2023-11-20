# Firmware
Firmware file is attached.  
Or you can download firmware at https://www.mydlink.co.kr/2013/beta_board/product_detail.php?no=119&model=DIR-815

![Untitled](https://github.com/goldds96/Report/assets/86287862/d1f3d665-6a56-4524-918e-d5244278a222)


# Overview  

**Vendor** : DLink  
**Product** : DIR-815 Router  
**Vulnerability Type** : Command Injection  
**Affected Version** : Firmware version <= v1.04  
**Description** : There is command injection vulnerability in **ssdpcgi_main** function of **cgibin** binary in **DIR-815 router firmware version <= v1.04.
In this function, obtains the data from web interface via **getenv**, and directly pass to **lxmldbc_system** without any filtering.
**lxmldbc_system** is **system** wrapper function.
Due to this vulnerability, attacker can inject commands and gains shell privileges.

![Untitled](https://github.com/goldds96/Report/assets/86287862/7562495c-8be9-4101-9106-95d17fc3c5f8)

# PoC
PoC code is attached.  
To reproduce this vulnerability, you can emulate firmware by using FirmAE(https://github.com/pr0v3rbs/FirmAE)  

![Untitled](https://github.com/goldds96/Report/assets/86287862/c8b91194-a6c1-422c-9c5a-19eaac38626f)

If emulation is success, you can access web interface  

![Untitled](https://github.com/goldds96/Report/assets/86287862/2ca2e0c7-778e-4b2f-aa40-da76b5e28f42)

Finally, run the PoC code.  

![Untitled](https://github.com/goldds96/Report/assets/86287862/301fc413-8ff0-4a64-a02e-893988b3ef71)
