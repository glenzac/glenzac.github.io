---
author: glenzac
categories:
  - "tinkering"
date: "2018-03-13T18:47:04+00:00"

summary: |-
  ![](https://img.shields.io/badge/Project-Abandoned-red)

  So this is like our department's group project. As always I'll be documenting all the things that I learned from working on this project.

title: Basketball Score Display System
---
![](https://img.shields.io/badge/Project-Abandoned-red)

So this is like our department's group project. As always I'll be documenting all the things that I learned from working on this project.

**📆 14-2-2018**

After discussing the rules of the game and the things to be implemented. We directly jumped to the things needed:
1\. Microcontroller
2\. Internal Timer
3\. A transmitter and a handheld controller
4\. Receiver
5\. 7 segment displays
6\. Buttons
Then the microcontroller to be used was specified as 8051 (because we still like to live in the 80s and rediscover things again for ourselves). Zigbee Tx and Rx modules were chosen due to obvious reasons. Calculations followed. It was found out that we needed at least 105 lines to control the segmented displays. This created a sudden shortage of I/O pins

**🚩Milestone 1:  Choosing between a a MUX and Shift Register** **MUX****Pros:**

1. Less hardware
1. simpler circuit
1. low power consumption

**Cons:**

1. Low brightness

**Shift Register** **Pros:**

1. High brightness

**Cons:**

1. high power consumption
1. Require as many shift registers as 7 segment displays
1. complex circuit

Winner : **Shift Register** even thought the cons far outweigh the pros from the end-user perspective a well lit display is paramount especially for outdoor enviroments.

🚩 **Milestone 2 : Deciding the interface and the display layout**

After using Adobe Illustrator for a long time it's always tempting to go back to the sophisticated yet easy tool to create anything to do with vectors. I quickly downloaded a few 7 segment svg files from wikipedia and the layout was ready in a  few minutes. The buttons took another couple of minutes.  I neither bothered about the aesthetics of the design nor the dimensions.

![basketball-01.png](@assets/wp-content/uploads/2018/03/basketball-01.png)![basketball-02.png](@assets/wp-content/uploads/2018/03/basketball-02.png)

🚩 **Milestone 3 : Designing the circuit**

I've used Fritzing in the past and naturally it was my first choice. The learning curve was quite flat and I added all the missing libraries and parts in no time. I designed based on the faint idea I had in mind.

🥊❌ Pitfall 1 : decoupling capacitors

I hadn't added decoupling capacitors to any IC's on the board nor did I know their importance.

🥊❌ Pitfall 2 : LPF

I had made switches in the design, but never added filters to it. A low pass filter was important  to reject high frequency noise and bounces caused during switching.

-\> Checking voltage tolerances is very important

Xbee VOH = 2.8V ✅
8051 VOH = 1.9V ✅
Xbee VOL = 0.5V ✅
8051 VOL = 0.9V ✅

All designs given below were done in Autodesk Eagle.

The updated Tx part :

![TX-1.png](@assets/wp-content/uploads/2018/03/tx-1.png)

The module in the Tx circuit:

![TX-11.png](@assets/wp-content/uploads/2018/03/tx-11.png)

The updated Rx part:

![RX-1.png](@assets/wp-content/uploads/2018/03/rx-1.png)

The module in the Rx circuit:

![RX-11.png](@assets/wp-content/uploads/2018/03/rx-111.png)

* * *

> **❌** Due to various reasons this project had to be abandoned.
