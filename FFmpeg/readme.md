# Buffer Overflow Vulnerability in FFmpeg

## Overview

**Vendor** : FFmpeg (https://github.com/FFmpeg/FFmpeg)  
**Product** : FFmpeg  
**Vulnerability Type** : Out-of-Bound Write  
**Affected Version** : git master v.5c635b7 ~ v.4565747  
**Description** : There is Buffer Overflow vulnerability in `ref_pic_list_struct` function in `libavcodec/evc_ps.c`. Due to this vulnerability, remote attacker can execute arbitary code and cause denial-of-service.  


## Reproduce

1. Crash file
[ffmpeg_crash.zip](https://github.com/goldds96/Report/files/13292743/ffmpeg_crash.zip)

2. Command
You can reproduce vulnerability as follow command
```Shell
$ ./ffmpeg -i ffmpeg_crash test
```

## Results

ASAN


![image](https://github.com/goldds96/Report/assets/86287862/5da0826c-c122-4b1a-851e-8b081c4a8831)

## Reference

[1] https://github.com/FFmpeg/FFmpeg/commit/4565747056a11356210ed8edcecb920105e40b60  
[2] https://patchwork.ffmpeg.org/project/ffmpeg/patch/20230915131147.5945-2-michael@niedermayer.cc/
