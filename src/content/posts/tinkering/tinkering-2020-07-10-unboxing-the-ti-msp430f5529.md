---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: MSP430
  image: "@assets/wp-content/uploads/2020/07/msp430.jpg"
date: "2020-07-10T23:33:04+00:00"

tags:
  - c
  - c++
  - embedded
  - "msp430-series"
  - programmer

title: Unboxing the TI-MSP430F5529
---
The TI-MSP430 was highly recommended on most online forums for anybody who wanted to move on from the safety net of the Arduino environment and do some real register level thing. It had the most flexibility. One could write in ASM or directly to registers using C or use the available device Libraries from TI or fall back to Energia (the Arduino like environment ported to such devices).

I also had the option of going with the STM32 (another highly recommended microcontroller) but I didn't want to directly jump to ARM devices. I wanted to start small.

![](@assets/images/2020/pQbBhSg.jpg)

![](@assets/images/2020/EpmTKuj.jpg)

![](@assets/images/2020/xICYBZ2.jpg)

![](@assets/images/2020/ciwpvD9.jpg)

![](@assets/images/2020/oUh1Xg6.jpg)

TI decided to keep it nice and simple. Had the hardware and pins mapping and a small Evaluation kit user guide that only asked the user to visit the TI website for user guides and software.

![](@assets/images/2020/dimrN7Y.jpg)

![](@assets/images/2020/9AoKx7e.jpg)

I really had trouble deciding on the right version of MSP430 device to buy. I had shortlisted 3 popular ones based on their availability. The Value-line series device MSP430G2xx and the MSP430F55xxx and finally the MSP430FR2xxx.

The G2xx was the cheapest and had an onboard DIP IC which could be removed and a new MSP430 could be put in place. Those were the only serious advantages of the value line series device. It lacked in most other features.

The next two devices had about the same costs. The F55xx series didn't have an [FRAM](https://en.wikipedia.org/wiki/Ferroelectric_RAM) while the MSP430FR2xx series had one. Apart from the FRAM thing, the F55xxx outshone the other one in all aspects.

So I was only left with the **MSP430F5529**
