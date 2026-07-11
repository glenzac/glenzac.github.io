---
author: glenzac
categories:
  - "random-views"
cover:
  alt: MSP430
  image: "@assets/wp-content/uploads/2020/07/msp430.jpg"
date: "2020-07-14T21:27:50+00:00"

tags:
  - embedded
  - msp430
  - ti

title: Understanding the clock system
---
The **MSP430F5529** has something called the **Unified Clock System (UCS)** other devices have other names for their systems. This is summarized in the table below:

![](@assets/images/2020/qkVQsAP.jpg)

💡 If you are following other MSP430 guides too, it's likely that you'll be seeing a different clock naming scheme there.

I've summarized the UCS in the diagram below:

![](@assets/images/2020/iJ7yYCa.jpg)

As can be seen in the figure above, the UCS produces 3 kinds of clock signals:

- **ACLK**: Auxiliary Clock
- **MCLK**: Master Clock
- **SMCLK**: Subsystem Master Clock

These different signals have different functions and the diagram below gives a rough idea:

![](@assets/images/2020/ysz0VVq.jpeg)

So the different clocks are selected based on the requirement and there is a trade off between performance and power consumption. The faster you want the device to run the more power it consumes.

The UCS derives its clock signals from 5 different sources namely:

- Very Low-frequency Oscillator ( **VLO**)
- REFerence Oscillator ( **REFO**)
- Digitally Controlled Oscillator ( **DCO**)
- **XT1** and **XT2** are the external oscillators that one can add (this is included on the LaunchPad boards ⇒ XT1 = ~32KHz and XT2 = 4MHz)

So if we need to run a timer on our microcontroller we need to choose any of the clock signals available. The default source is the **DCO**. It is calibrated and set to particular values that sets **MCLK** and **SMCLK** at **~1.045 MHz**. For now, we'll be using the clock sources as it is without changing any of the **DCO** frequency range. (This will be covered in a future advanced lesson)

The selectors are basically MUX's that enable us to select the different clock sources to generate the required clock signals. For eg. **MCLK** is software selectable to use XT1, REFO, VLO, DCO or XT2 as sources. Thus we have full flexibility in choosing any of the available sources to run our Master Clock on.

The divider blocks are frequency dividers that are required to get different higher time periods (as frequency reduces time period increases) using the same clock. We'll see it in action in an upcoming lesson.
