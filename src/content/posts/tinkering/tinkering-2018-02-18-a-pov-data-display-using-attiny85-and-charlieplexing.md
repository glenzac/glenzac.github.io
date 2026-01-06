---
author: glenzac
categories:
  - "tinkering"
date: "2018-02-18T19:36:20+00:00"

summary: |-
  ![](https://img.shields.io/badge/Project-Abandoned-red)**_This post is still a work in progress_**

  Our lab coursework in college requires everyone to build a simple project on any microcontroller and which uses interfacing of some I/O devices like a relay, Tx-Rx, temperature sensor etc.
tags:
  - attiny85
  - charlieplexing
  - display
  - pov

title: A POV data display using ATTINY85 and charlieplexing
---
![](https://img.shields.io/badge/Project-Abandoned-red)**_This post is still a work in progress_**

Our lab coursework in college requires everyone to build a simple project on any microcontroller and which uses interfacing of some I/O devices like a relay, Tx-Rx, temperature sensor etc.

I started thinking about different project ideas to implement and eventually landed on the Persistence of Vision Display using an [ATTINY85](https://www.mouser.com/ds/2/268/Atmel-2586-AVR-8-bit-Microcontroller-ATtiny25-ATti-1066528.pdf). Though a simple display is already implemented [here](http://www.instructables.com/id/ATtiny8545-POV-Display/) , I wanted to take it further - to drive more than 5 LEDs and also if possible to take in an analog or digital sensor input. There are multiple methods to get more I/O pins - one could use an I/O expander (not possible in this case as size and power is a big constraint), [multiplexing](https://en.wikipedia.org/wiki/Multiplexing) or [Charlieplexing](https://en.wikipedia.org/wiki/Charlieplexing).I couldn't entertain the idea of using another IC for multiplexing due to the aforementioned constraints. So I decided Charlieplexing was the way out.

### Design Constraints

Using the following Dot Matrix ASCII table I found [here](https://electronics.stackexchange.com/questions/254244/displaying-ascii-codes-to-an-7x5-led-matrix) I figured out that I needed at least 7 rows of LEDs to display most characters.

1. ### **Minimum no. of LEDs required = 7**

![uuwfg](@assets/wp-content/uploads/2018/02/uuwfg.jpg)

### **2\. No. of I/O pins on the microcontroller**

![attiny45-85](@assets/wp-content/uploads/2018/02/attiny45-85.jpg)

With only a total of 8 pins out of which - 1 VCC, 1 GND and 1 Reset pin set back the useful total to 5. 5 I/O lines. That's it! Going by the normal method of one LED per line, this could only drive a total of 5 LEDs. So I started searching if I could use the other RESET pin as an I/O port and it turns out - its possible, but then there is a catch - Setting the RESET pin as an I/O pin involves reprogramming the internal fuses and one extra I/O line comes at a hefty price - No more ISP programming with an Arduino is possible. Then altering the microcontroller code will require a high voltage programmer. Though my curiosity led me to a [workaround](http://mightyohm.com/blog/2008/09/arduino-based-avr-high-voltage-programmer/), making a whole new device for a project beats the whole purpose of it.Hence I concluded that I'm stuck with 5 I/O pins.

**No. of available I/O pins - 5**

### 3\. Charlieplexing

Using the equation **No. of pins = \[(1+sqrt(1+4L))/2\]** where L is the no. LEDs. In this case with L=7, we get no. of pins required as **3.192.** We cannot do any rounding here and come to the conclusion that only 3 pins are required. 3.192 => we need at least 3.192 pins that is we need more than 3 pins => **4 pins for 7 LEDs**

4\. Calculating your current requirements

https://www.embedded.com/electronics-blogs/break-points/4429960/How-much-energy-can-you-really-get-from-a-coin-cell-

LED = 7\*5mA = 35mA

ATTINY85 <= 2mA

The total comes to 37mA.

Most button cells (CR2032) have about 220mAh. So 220/37 = 5.945 hrs of battery life which is not that bad. But unfortunately, a bit of digging up led me to this [page](https://www.embedded.com/electronics-blogs/break-points/4429960/How-much-energy-can-you-really-get-from-a-coin-cell-) and according to the author at such high consumption (relatively) the battery voltage falls of rapidly and if it goes below 2.7V the m

_so probably use series connection of button cells?_

Soldering

[http://mightyohm.com/files/soldercomic/FullSolderComic\_EN.pdf](http://mightyohm.com/files/soldercomic/FullSolderComic_EN.pdf)

Components Required:

1. ATTINY85
1. LEDs 5mm ( preferably red due to their low current consumption)
1. Button cell CR2032
1. Motor and it's power source
1. Arduino Uno - just to program the IC
