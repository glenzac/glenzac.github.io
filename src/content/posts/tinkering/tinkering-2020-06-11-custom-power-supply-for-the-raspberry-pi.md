---
author: glenzac
categories:
  - "tinkering"
date: "2020-06-11T11:16:37+00:00"

summary: ""
tags:
  - charger
  - power
  - raspberrypi
  - testing

title: Custom power supply for the Raspberry pi
---


My 2A and 2.4A mobile charger adapters were frequently going under-voltage whenever the Rpi did some heavy processing. These chargers are not built to sustain heavy 2.5A loads for milliseconds. They are not built to run powerful SBCs. So instead of directly buying the official raspberrrypi charger I thought about using the parts I have to make a stable custom power supply for the pi.

My first attempt was with the Phillips power module that I had found in a DVD player. Link to the post [here](/2018/08/21/its-a-dvd-player-this-week/).

This supply had 5V, 12V and -22V connections on it. I simply soldered a USB female connector to a perfboard and connected the power supply. I ensured that the voltage is safe enough and accurate for the pi. I did 3 such trials of voltage verification after switching it on and off. It was indeed a stable power supply. It was giving around 5.05V.

![](@assets/images/2020/uxZnB2q.jpg)

![](@assets/images/2020/2UDXQhM.jpg)

Unfortunately, just opening up chromium on the Rpi made the infamous ⚡️ symbol to appear. So this power supply too was drooping and going below 4.65V under high loads. Checking the datasheet of the DVD player confirmed that the max. expected current consumption of the DVD player was 10W so this was basically operating out of margin.

The official Rpi power supply is 5.1V and 2.5A which means 12.75 Watts. So we need anything above that value.

Next, I tried a AC-DC hobby power supply adapter of 24W that too kept showing the ⚡️ symbol from time to time.

Next in line was a industrial grade power supply that I had lying around. It was rated at 24V and 1.1A => clearly about 26W of power.

![](@assets/images/2020/Qaz3Q98.jpg)

I used one of the LM2596 buck converter modules to bring the voltage down to 5.1V and powered up the pi again through the USB port. This power supply fared better than the others. Still, opening applications and streaming at HD resolutions brought the power supply to its knees. 😐😐

Apparently they can handle large loads and 24W but not a SBC that draws a huge amount of current for a very short time in the range of milliseconds.

Next in line was a power supply brick from a laptop that I had taken apart. 😅 Most laptop supplies provide around 19V.

![](@assets/images/2020/U5ufoPE.jpg)

The laptop PCB had 4 USB ports waiting to be scavenged

![](@assets/images/2020/EorAoxW.jpg)

And a nice and shiny DC jack

Desoldering it was no easy thing. 🙁 The connections just refused to budge. No amount of heat could get the terminals out. I didn't have any copper braid around, using strands of copper wire didn't help much. So I had to literally go about ripping the PCB with pliers to get the thing out.

![](@assets/images/2020/rB7vTov.jpg)

Thankfully, one USB port was easy to remove and I got it out safely.

![](@assets/images/2020/FjDe1y3.jpg)

Soldered the USB connector in place. Initially I had placed another DC jack but the connector got stuck due to excess solder.

![](@assets/images/2020/RDHGK0g.jpg)

I decided to attach the pins found in berg strips to connect the power jack to the pads beneath the perfboard.

![](@assets/images/2020/v2UjQZU.jpg)

That didn't go well. In the end I had to cut out the green PCB from underneath the DC jack with force and finally soldered connections to the perfboard.

I also decided to add a NodeMCU to the circuit to run a cooling fan and some other home accessories. Note: I know that the Rpi has enough PWM pins to run fans but I didn't want to load the pi any further.

![](@assets/images/2020/4hb6GI9.jpg)

![](@assets/images/2020/TpIWUwS.jpg)

Then I decided to try out the NodeMCU and see if it works properly. As a safety step I always check the VCC - GND continuity to ensure that there is no short circuit. I plugged it in. The NodeMCU fired up fine. Decided to flash some random code. No matter what it wouldn't upload the code. There was something wrong. I decided to check if any pins were shorted together. I found two pins to be shorted. 😳

I blamed by shoddy soldering skills at first and redid the soldering connections and tried continuity again. There was still a short. After a while of thinking my eye went to this spot on the other side of the board.

![](@assets/images/2020/knrJZhY.jpg)

Damn, the things I do are already error prone now I've to even look out for manufacturing defects. 🙁

Hopefully, this is the last time I have to use perfboards for big projects.

Also decided to place two separate LM2596 buck converter modules. One for exclusively for the Rpi at 5.25V and another one for the cooling fan and the NodeMCU at 5V. I know it's a bit overkill but I just let it be.

![](@assets/images/2020/PJgOEAA.jpg)

![](@assets/images/2020/puAq0Ia.jpg)

![](@assets/images/2020/0M2xyUS.jpg)

![](@assets/images/2020/LJ3C4Zq.jpg)

I forgot to add a switch for the pi so that too was done and resoldered the wires again.

![](@assets/images/2020/vwYmQ87.jpg)

Tested and set the right voltages

![](@assets/images/2020/BRYua3c.jpg)

Testing the cooling fan that I got from the laptop. Checkout this [post](/2020/02/17/variable-frequency-pwm-generator/) where I made a PWM generator for the fan.

![](@assets/images/2020/WbDl9C8.jpg)

The fan works as expected from the NodeMCU.

![](@assets/images/2020/p4co34C.jpg)

I decided to use the Blynk app for controlling the NodeMCU. I set buttons to set pin states and a slider for controlling the speed of the fan. As of now I've to manually use the Blynk app to on the cooling fan.

![](@assets/images/2020/vuOHL6J.jpg)
