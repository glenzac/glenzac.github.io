---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: DVP3146K_98-IMS-en_SG
  image: "@assets/wp-content/uploads/2018/08/dvp3146k_98-ims-en_sg-e1534589706538.png"
date: "2020-06-10T06:10:19+00:00"

summary: It was time to bid goodbye to an old [Phillips DVD player](https://www.philips.com.sg/c-p/DVP3146K_98/divx-playback).
tags:
  - components
  - dvd
  - salvaging

title: A DVD player at stake!
---
It was time to bid goodbye to an old [Phillips DVD player](https://www.philips.com.sg/c-p/DVP3146K_98/divx-playback).


<Gallery cols={1}>

</Gallery>  
[**Link to the instructable I published on this.**](https://www.instructables.com/id/Parts-to-Salvage-From-a-DVDCD-Player/)

Removed the AC main cable and unscrewed the enclosure.

⚠️ Ensured that all the capacitors are safely discharged by touching them with a metal part. ⚠️

![WP_20180818_08_26_01_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_08_26_01_pro.jpg)

Then I looked for its service manual (thankfully I found it [here](https://www.manualslib.com/download/987399/Philips-Dvp3126k.html)) and followed the part removal procedure.

![Screenshot (324).png](@assets/wp-content/uploads/2018/08/screenshot-324.png)

Took things apart one be one.

## 1\. The power supply

![WP\_20180818\_12\_30\_11\_Pro](@assets/wp-content/uploads/2018/08/wp_20180818_12_30_11_pro.jpg)

The power supply is perhaps the best thing to salvage from such a device and is totally worth the time.

![Screenshot (325)](@assets/wp-content/uploads/2018/08/screenshot-325-e1534596554610.png)

From the service manual I got to know the voltages at the different connector pins.
I was pleased to find 5V, 12V and -12V all regulated DC outputs from a single board.

I could use this to run opamps that need voltages at both polarities and well I needn't explain the potential use of a 5V supply :P

And all this was present as a single isolated board.

From the diagram below it was quite obvious that this is a well designed and stable supply.

![screenshot-328.png](@assets/wp-content/uploads/2018/08/screenshot-328-e1534597103176.png)**Update : 20/5/2019** : After lying around for a while, I finally made use of the power supply board to charge lead acid batteries. To bring down the voltage to the required levels I used a regular buck converter module.

## 2\. The Front Board

![WP_20180818_09_06_22_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_09_06_22_pro.jpg)

The front board consists of the following parts:

- IR module
- switches
- LED display
- Mic with amplifier

![WP\_20180818\_09\_16\_01\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_09_16_01_pro.jpg)

Looks like those standard 3 pin IR LEDs out there.

![WP\_20180818\_09\_16\_09\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_09_16_09_pro.jpg)

![WP\_20180818\_09\_15\_44\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_09_15_44_pro.jpg)

The display uses a [ET6202](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjM48yw2PbcAhVLO48KHRvnBC8QFjAAegQICRAC&url=http%3A%2F%2Fread.pudn.com%2Fdownloads166%2Fdoc%2Fproject%2F763821%2FET6202-en.pdf&usg=AOvVaw3xVzjXsPiGN3OKTF3ODzf_) LED driver which appears to have been used with an arduino too (check [this](https://gist.github.com/powerswitch/79e91f8f2d5f311f0734438726b63486)). So this looks like a good catch!

![WP_20180818_12_27_43_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_12_27_43_pro.jpg)

![WP\_20180818\_12\_29\_01\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_12_29_01_pro.jpg)

This board had a mic, an 8.3K potentiometer ( measured it using a multimeter), and an amplifer. The pot is used to adjust the gain of the mic.

## 3\. The DVD tray


<Gallery cols={1}>

</Gallery>  

## 3.1 Motors + a wonderful switch


<Gallery cols={1}>

</Gallery>  

\[enter video here\]

## 3.2 Lens, Neodymium magnets and more...

Took a closer look and found that the optical reader was from SONY.

![WP_20180818_10_28_23_Pro](@assets/wp-content/uploads/2018/08/wp_20180818_10_28_23_pro1.jpg)

![WP\_20180818\_11\_20\_52\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_11_20_52_pro.jpg)


<Gallery cols={2}>

</Gallery>  

Scraped off the white drop of glue (visible in the above images) and removed the outer cover.

![WP\_20180818\_11\_28\_15\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_11_28_15_pro.jpg)

https://youtu.be/hNsJkvjbRbk

![WP\_20180818\_11\_29\_17\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_11_29_17_pro.jpg)

![WP\_20180818\_11\_34\_14\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_11_34_14_pro.jpg)

Yoohoo....Time to play around with it...


<Gallery cols={1}>

</Gallery>  

The above shown are images I took with the lens supplementing my phone camera. The fingerprint ridges look so deep!!


<Gallery cols={1}>

</Gallery>  

The lens when held above a phone's screen, the pixels are perfectly visible. The different combination of RGB LEDs that create wonderful images on screen. Beautiful.

![WP\_20180818\_11\_51\_31\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_11_51_31_pro.jpg)


<Gallery cols={2}>

</Gallery>  

![WP\_20180818\_11\_55\_08\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_11_55_08_pro.jpg)

## 3.3 Motors

![WP\_20180818\_12\_29\_28\_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_12_29_28_pro.jpg)

## 3.4 Linear Slider


<Gallery cols={1}>

</Gallery>  

## 4\. What remains:

### ![WP_20180818_09_07_09_Pro.jpg](@assets/wp-content/uploads/2018/08/wp_20180818_09_07_09_pro.jpg)

This board is mostly made of SMD components that are not so easy for hobbyists to handle. Though the board has components like

- EEPROM
- SDRAM
- FLASH
- VIDEO DRIVER
- MOTOR DRIVER

the time and money you put into making some use of it will far cross the actual value of the component. Hence I usually discard them.
