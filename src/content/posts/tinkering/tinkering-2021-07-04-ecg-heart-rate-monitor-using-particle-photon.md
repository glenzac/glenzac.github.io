---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: IMG_20190611_113950(1)
  image: "@assets/wp-content/uploads/2019/08/img_20190611_1139501.jpg"
date: "2021-07-04T19:17:19+00:00"

summary: '![](https://img.shields.io/badge/Project-Complete-blue.svg)'
tags:
  - circuit
  - ecg
  - electronics
  - medical
  - particle-photon
  - projects
  - testing

title: ECG Heart rate monitor using Particle Photon
---
![](https://img.shields.io/badge/Project-Complete-blue.svg)

**Disclaimer:** This is not a medical device and cannot be used as a replacement for medical diagnosis in any circumstances. Only use an appropriate battery to power this device. Do not connect it to a power supply that is connected to the AC mains. Double-check all connections before connecting yourself to the device. **I assume no responsibility for anything that might happen due to the use/misuse of this project. I acknowledge that this a crude implementation of an ECG monitor. There are several safety features that I've skipped or overlooked for the sake of reducing complexity or costs or form factor.**

This device has an [Analog Front End](https://en.wikipedia.org/wiki/Analog_front-end) that conditions the ECG signal that is picked up by the electrodes from the body. The signal is then given to the Particle Photon's analog input pin.

For insights on Analog Front End design and to know how I arrived at the following circuit. Do check out my previous [post](/2019/04/23/ecg-analog-front-end-design).

![fig(1)](@assets/wp-content/uploads/2019/08/fig1.png)

The circuit consists of the following:

1. **Instrumentation amplifier**
1. **High Pass Filter** \- 2nd order Sallen Key Topology
1. **Low Pass Filter** \- 3rd order \[Buffered RC + Sallen Key\]
1. **Right leg Driver circuit**
1. **Switched capacitor voltage converter**
1. **Particle Photon**

The high pass filter has a cut of ~1Hz and the low pass filter has a cut off of ~160Hz giving medical diagnostic quality ECG signals.

Refer the following figure for exact values:

![Screenshot_2019-06-13 Signal Calculator.png](@assets/wp-content/uploads/2019/08/screenshot_2019-06-13-signal-calculator.png)

This filtered ECG signal is given to the analog input of the Particle photon. The signal is sampled at fixed intervals and stored into a buffer. This data is then processed using some techniques borrowed from the renowned [Pan Tompkins algorithm](http://www.robots.ox.ac.uk/~gari/teaching/cdt/A3/readings/ECG/Pan+Tompkins.pdf).

Once the QRS intervals are detected the heart rate is calculated and then plotted. If the heart rate goes beyond the normal range the red LED warns the user of the abnormal reading. (Note: The device takes a couple of seconds to stabilize to the normal range at startup)

![ECG noise free.jpg](@assets/wp-content/uploads/2019/08/ecg-noise-free.jpg)

If the ECG electrodes are connected following all the electrode placement rules, then this device will produce a much better-looking waveform.

**Note:** I haven't incorporated a 50Hz/60Hz notch filter to remove noise caused by  AC mains as I developed this circuit to be used in an environment which is far from AC interference. Hence, I found the signal to further improve in quality when I cut-off the AC mains.

![serialplot\_NgI7oO7IRQ.jpg](@assets/wp-content/uploads/2019/08/serialplot_ngi7oo7irq.jpg)

Note : All signals are plotted in realtime using the SerialPlot software available [here](https://hackaday.io/project/5334-serialplot-realtime-plotting-software).

![serialplot\_Tg8V0b9TGU.jpg](@assets/wp-content/uploads/2019/08/serialplot_tg8v0b9tgu-1.jpg)

Finally, if the heart rate goes out of the normal range, the LED lights up to warn the user. This can be further improved by giving an audio feedback or the ECG data can be directly sent to the patients doctor via the Internet.

For this project I used the particle in it's MANUAL mode, i.e without connecting to the cloud. Do note that maintaining a cloud connection slows down the loop considerably.

Finally, the device does the job pretty well. There are many more safety features and processing steps that I plan to include into this.
**If anyone finds this interesting or need any of the design files or have any queries do post in the comments section below and I'll be more than happy to help.**

* * *

**Additional Resources**

1. [ECG](/2018/12/14/ecg-references-guide)
1. [Filter design](https://wordpress.com/post/glenzac.wordpress.com/940)
