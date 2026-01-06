---
author: glenzac
categories:
  - "random-views"
cover:
  alt: MSP430
  image: "@assets/wp-content/uploads/2020/07/msp430.jpg"
date: "2021-04-29T08:30:40+00:00"

tags:
  - embedded
  - msp430
  - ti

title: 2.1 Timers_Capture_Mode
---
Now, what if I wanted the timer to work like a stopwatch? To record the time it takes to do a process or to note down the time when an event occurs. For this, we need to use the timer in Capture mode. What we learned above was using the timer in Compare mode where we compare the timer value with the value in the **CCRn** register.  
The Capture Mode is selected when **CAP** = 1\. The capture inputs **CCIxA** and **CCIxB** are connected to external pins or internal signals and are selected with the **CCIS** bits. The **CM** bits select the capture edge of the input signal as rising, falling, or both. A capture occurs on the selected edge of the input signal. If a capture occurs:  
• The timer value is copied into the **TAxCCRn** register  
• The interrupt flag **CCIFG** is set

https://i.imgur.com/ZmYHtfm.jpg

Overflow logic is provided in each capture/compare register to indicate if a second capture was performed before the value from the first capture was read.Bit **COV** is set when this occurs.

Output modes

Registers needed

Interrupt vector

code
