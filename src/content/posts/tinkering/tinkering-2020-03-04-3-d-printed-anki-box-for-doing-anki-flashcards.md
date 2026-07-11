---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: optimised-featured
  image: "@assets/wp-content/uploads/2020/02/optimised-featured.jpg"
date: "2020-03-04T13:12:51+00:00"
summary: '![](https://img.shields.io/badge/Post-In%20Progress-brightgreen.svg)'
tags:
  - 3d-printing
  - anki
  - eagle
  - electronics
  - flashcards
  - fusion360
  - particle-photon

title: 3-D printed Anki Box for doing Anki flashcards
---
![](https://img.shields.io/badge/Post-In%20Progress-brightgreen.svg)

I guess the keyboard isn't cool enough that the thought of making a custom flashcard answering device popped up in my mind. 😛

I needed something on my table that would serve as a constant reminder for me to do my Anki cards. (Btw I still don't have a fixed time to do my cards 😐  )

### **Usecase:** To do Anki flashcards.

 **Note:** this device is not a keyboard. Ideally should only be used for cards that don't require input in the form of typed text and that needs to be answered quickly (more details about timer below) (this stands true to the spirit of Anki and in accordance with the super memo principles)

The device basically has 4 buttons :

1. Again
1. Hard
1. Good
1. Easy

Buttons that can be used to rate cards. I've also included a 2 digit seven segment timer. I initially thought of having a 3 digit timer, but that's totally against the whole point of reviewing cards.

Additionally, it also has a replay button that's going to be useful to replay audio in the case of language cards. I've also included buzzers and LEDs for feedback.

I initially thought about using Arduino so that. Then I dropped the plan as an Arduino 328p uC can't act as a USB HID device. (not until you make some deep level mods)

Boards with the Atmega324 IC like the Micro, Leonardo are capable of mimicking a USB HID device. I didn't have any of those around. So I went with the [Particle Photon](https://docs.particle.io/photon/).

### The circuit :

![](@assets/images/2020/xGw6Tdn.jpg)

I wanted to try out the Autodesk Eagle - Fusion 360 integration. So I created the board in Eagle and pushed it to Fusion 360.

![](@assets/images/2020/Pyt3dZ9.jpg)

Building the enclosure took a lot of time. Firstly, I had to find 3D packages and models for each and every part that I use in Eagle and then understand the chaotic Eagle Managed Library. A couple of online [tutorials](https://www.youtube.com/watch?v=8_cNpTUh1sI&t=98s) helped me understand the process of building enclosures.

![](@assets/images/2020/zuIodTr.jpg)![](@assets/images/2020/O4vEuXj.jpg)![](@assets/images/2020/yR5WZ5U.jpg)

Hit a few roadblocks in between when the enclosure overlapped with the components on the board. 🤦‍♂![](@assets/images/2020/fw5dz6H.jpg)![](@assets/images/2020/pbKhPSD.jpg)

The enclosure uses slots as a locking mechanism.

### Here's the rendered PCB:

![](@assets/images/2020/xc22oIr.png)

<video controls muted playsinline src="/videos/9tXJsr8.mp4"></video>

### The Case:

![](@assets/images/2020/wRmrgw7.png)

### The Top cover:

![](@assets/images/2020/5JAQEla.png)

### The PCB resting on the mounts:

![](@assets/images/2020/BKIZTIV.png)

I must use [light pipes](http://static.vcclite.com/pdf/LFBSeries.pdf) to bring the light from the LED to the surface (suggested by [Xials](https://www.reddit.com/user/Xials/))

![](@assets/images/2020/Etv4pxw.png)

This is how it looks in the end:

### Anki Box

![](@assets/images/2020/rjefrzQ.png)![](@assets/images/2020/RFZ3GrG.png)

⚠️  This is still a work in progress  ⚠️
