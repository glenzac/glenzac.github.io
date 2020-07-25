---
author: glenzac
comments: true
date: 2020-03-04 13:12:51+00:00
layout: post
link: https://glenzac.wordpress.com/2020/03/04/3-d-printed-anki-box-for-doing-anki-flashcards/
slug: 3-d-printed-anki-box-for-doing-anki-flashcards
title: 3-D printed Anki Box for doing Anki flashcards
wordpress_id: 1306
categories:
- Tinkering 🛠️
tags:
- 3D printing
- Anki
- Eagle
- electronics
- flashcards
- fusion360
- Particle Photon
---

![](https://img.shields.io/badge/Post-In%20Progress-brightgreen.svg)

<!-- more -->

I guess the keyboard isn't cool enough that the thought of making a custom flashcard answering device popped up in my mind. 😛

I needed something on my table that would serve as a constant reminder for me to do my Anki cards. (Btw I still don't have a fixed time to do my cards 😐  )


### **Usecase:** To do Anki flashcards.


**Note:** this device is not a keyboard. Ideally should only be used for cards that don't require input in the form of typed text and that needs to be answered quickly (more details about timer below) (this stands true to the spirit of Anki and in accordance with the super memo principles)

The device basically has 4 buttons :



	
  1. Again

	
  2. Hard

	
  3. Good

	
  4. Easy


Buttons that can be used to rate cards. I've also included a 2 digit seven segment timer. I initially thought of having a 3 digit timer, but that's totally against the whole point of reviewing cards.

Additionally, it also has a replay button that's going to be useful to replay audio in the case of language cards. I've also included buzzers and LEDs for feedback.

I initially thought about using Arduino so that. Then I dropped the plan as an Arduino 328p uC can't act as a USB HID device. (not until you make some deep level mods)

Boards with the Atmega324 IC like the Micro, Leonardo are capable of mimicking a USB HID device. I didn't have any of those around. So I went with the [Particle Photon](https://docs.particle.io/photon/).


### The circuit :


![](https://i.imgur.com/xGw6Tdn.jpg)

I wanted to try out the Autodesk Eagle - Fusion 360 integration. So I created the board in Eagle and pushed it to Fusion 360.

![](https://i.imgur.com/Pyt3dZ9.jpg)

Building the enclosure took a lot of time. Firstly, I had to find 3D packages and models for each and every part that I use in Eagle and then understand the chaotic Eagle Managed Library. A couple of online [tutorials](https://www.youtube.com/watch?v=8_cNpTUh1sI&t=98s) helped me understand the process of building enclosures.

![](https://i.imgur.com/zuIodTr.jpg)

![](https://i.imgur.com/O4vEuXj.jpg)

![](https://i.imgur.com/yR5WZ5U.jpg)

Hit a few roadblocks in between when the enclosure overlapped with the components on the board. 🤦‍♂![](https://i.imgur.com/fw5dz6H.jpg)

![](https://i.imgur.com/pbKhPSD.jpg)

The enclosure uses slots as a locking mechanism.


### Here's the rendered PCB:


![](https://i.imgur.com/xc22oIr.png)

https://i.imgur.com/9tXJsr8.mp4


### The Case:


![](https://i.imgur.com/wRmrgw7.png)


### The Top cover:


![](https://i.imgur.com/5JAQEla.png)


### The PCB resting on the mounts:


![](https://i.imgur.com/BKIZTIV.png)

I must use [light pipes](http://static.vcclite.com/pdf/LFBSeries.pdf) to bring the light from the LED to the surface (suggested by [Xials](https://www.reddit.com/user/Xials/))

![](https://i.imgur.com/Etv4pxw.png)

This is how it looks in the end:


### Anki Box


![](https://i.imgur.com/rjefrzQ.png)

![](https://i.imgur.com/RFZ3GrG.png)

⚠️  This is still a work in progress  ⚠️
