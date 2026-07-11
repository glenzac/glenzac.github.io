---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: DSCN1210
  image: "@assets/wp-content/uploads/2018/11/dscn1210-1.jpg"
date: "2021-04-07T11:14:49+00:00"

summary: ""
tags:
  - electronics
  - laptop
  - parts
  - teardown

title: Laptop at stake!
---


This post has been pending for a really long time now. Finally, I got time to come back and finish up my old drafts.

This is about the [MSI CR420](https://www.msi.com/Laptop/CR420/Specification) classic series laptop. This was bought in ~ 2010. It ran without much issues for 4+ years. After that it showed signs of overheating, battery issues and random shutdowns. It fell out of use. Finally, around 2016 it totally stopped working. It was powering up but not booting. I decided to checkout the RAM and try and reinsert it. That didn't help. Giving this for repair would be a joke. So naturally, it ended up in my e-junk collection🤣

![](@assets/images/2021/Aitye6r.png)

I started by removing all the screws and nice and carefully removing the the full enclosure.

![](@assets/images/2021/NxjpOor.jpg)

The CMOS battery quickly caught my attention. That could be the issue that was preventing the boot. So I quickly got another CR2032 from a remote and put it in. That too didn't work 🙁

It uses two 2GB RAM modules. I removed those carefully.

![](@assets/images/2021/xZrfnPj.jpg)

#### Update: I later used these RAM modules to try out an incompatible RAM upgrade with my brother's DELL laptop. To our surprise, it really worked well and continues to run so. 😁

![](@assets/images/2021/kTm26C6.jpg)

I see familiar wires and connectors. So this is the WiFi adapter. I tracked those black and grey wires, it ran into the screen. This is kinda surprising.

![](@assets/images/2021/Wy3ra4A.jpg)

The white and grey wires running into the screen panel

I didn't know laptops had their antennas in their screens. A google search confirmed this. Now that I think of it, perfect design strategy!

Disconnected those connectors to separate the display from the main board

![](@assets/images/2021/17TGguc.jpg)

Pretty impressed by their all-metal solid hinge that was still tight even after years of use.

![](@assets/images/2021/yM6mDPp.jpg)

![](@assets/images/2021/sPlbPG8.jpg)

The top view ofcourse

Extracted the DVD-RW tray out. Opening it up is worthy of another post. 🤣

![](@assets/images/2021/3Vu6zjh.jpg)

This is where the cooling fan was placed. Copper shielding either to conduct heat well or maybe even to guard the processor from EMI. Don't know for sure.

![](@assets/images/2021/EBjD9fc.jpg)

The all famous Synaptics touch pad.

![](@assets/images/2021/z7vG8Eb.jpg)

Next in line is the processor itself. The image below shows the top side.

![](@assets/images/2021/xkZYQYt.jpg)

I removed the safety lock at the bottom and took the chip out. Beauty!😍 Yeah, now you can roast me for taking it out. 😅I'm fully aware that just opening that lock and taking it out is going to add infinite amount of dust and other tiny particles in it that's going to render it useless. I've no plans of using a raw i5 🤣🤣 anyway.

![](@assets/images/2021/Ih2cVzZ.jpg)

The Intel i5 in all its glory 😍

![](@assets/images/2021/AP94wa0.jpg)

![](@assets/images/2021/YNU4GsA.jpg)

The white substance is the thermal paste

![](@assets/images/2021/ONmql39.jpg)

Intel i5

Lol, it took me a while to finally put the chip down. Next, moving on to the screen. Removed the panel.

![](@assets/images/2021/JFTp2r4.jpg)

Now, I finally see the WiFi antennas. Okay, so laptops have two WiFi antennas at the two topmost corners. I think I can use these antennas and connectors on my [Particle Photon](https://docs.particle.io/photon/) devices. Should try that out later.

![](@assets/images/2021/ED2JMKX.jpg)

This is very unlike my personal laptop's shoddy hinge that is shown [here](/2020/02/04/laptop-hinge-repair-guide/).

![](@assets/images/2021/0IxZPe2.jpg)

Got two powerful neodymium magnets too!

![](@assets/images/2021/q8RMawO.jpg)

#### Update: I used the 19V power supply brick of the laptop for creating a [power supply](/2020/06/10/custom-power-supply-for-the-raspberry-pi/) for the raspberry pi
