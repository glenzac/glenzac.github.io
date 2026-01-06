---
author: glenzac
categories:
  - "tinkering"
date: "2019-02-27T05:58:57+00:00"

summary: ""
tags:
  - code
  - particle-photon
  - testing

title: Essential Particle CLI commands
---


I installed [Particle CLI](https://docs.particle.io/tutorials/developer-tools/cli/) on Windows. This allowed for cloud compiling and flashing of Particle devices via serial. Once you have the Photon connected via USB and have navigated to the correct folder where you have saved the file that needs to be flashed, the following are the basic commands that one must know :

**To find the port of the Particle Photon:**

```
particle serial list
```

 **To compile firmware(after navigating to the right folder)**

```
particle compile photon code.ino --saveTo firmware.bin
```

 **if you have additional libraries put their header files in the current directory and use:**

```
particle compile photon code.ino library.cpp --saveTo firmware.bin
```

 **To put the photon into DFU mode (this is a workaround of sorts) fill XX with COM port number obtained before**

```
mode COMXX 14400
```

 **To flash the firmware**

```
particle flash --usb firmware.bin
```

 **To read serial data**

```
particle serial monitor
```
