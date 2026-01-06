---
author: glenzac
categories:
  - uncategorized
cover:
  alt: 'AEX Dark #2 by Savio.jpeg'
  image: "@assets/wp-content/uploads/2017/12/aex-dark-2-by-savio-e1517413681990.png"
date: "2017-12-22T15:32:21+00:00"

summary: It's been almost a year since I bought a new phone and it is customary to root it and
tags:
  - android
  - aosp
  - customrom
  - magisk
  - rooting
  - xda
title: In search of that perfect ROM
---
It's been almost a year since I bought a new phone and it is customary to root it and flash a custom ROM at the end of the warranty period (didn't wanna take any chances). Even though officially there is still a month left in the warranty period, I couldn't wait for any longer.I'm sick of using an outdated lollipop Rom. Can you even imagine using lollipop in 2017?

Once the decision was made, only the easy part was over. Now I had to choose the best possible and stable ROM that had a lot of features without a lot of those hiccups. The process involved meticulously reading through the different device-specific and ROM specific threads on xda devs. Lineage OS was so tempting with their neat UI and proven track record, but I also had to try out other options. I was indeed surprised by the plethora of ROMs available for each device nowadays. My phone had at least 10-15 different options from different developers and they all had a lot of differences among them. This was a far cry from the number of device-specific ROMs you had back during Gingerbread. Back then even popular phones had only a couple of ROMs. I still remember the different ROMs I flashed back then...HYDROPERIA, ELASYS, EXPLODE.

I had an overwhelming number of options before me. I decided to go for a Nougat ROM as the latest OREO build had problems with VoLTE. So 7.1.2 was the leap I was planning to take. This took all those different Lollipop and MM ROMs off my list. Then I was left with a couple of ROM options - Lineage, AOKP, AICP, RESURRECTION  and AOSP Extended, these were the ones with official support. I was not looking for an unofficial or alpha build - I just wanted a stable, reliable, day to day phone with all the bells and whistles :D

Reading through 100s of thread pages for every single ROM is a herculean task, but I had to ensure that the ROM was at least near flawless. After days of research, I decided to go with the AEX (AOSP Extended) ROM. The screenshots looked minimal and beautiful. The ROM also had a lot of features cherry-picked from various other ROMs. It didn't have those fancy gimmicks, only those absolutely necessary and a large number of customization options.

After I made my mind, I went forward with the rooting followed by flashing a custom TWRP recovery. After it all went smoothly, I wiped the device and flashed the new ROM and it's supported gapps package. The boot animation was modern and everything worked well but apparently, the device got unrooted again. So I quickly jumped to TWRP recovery and flashed a SuperSU package and hit reboot. Just after I hit reboot I remembered that I hadn't wiped the Dalvik cache and that was it - **Bootloop.**

There I was, once again at square one. Initial attempts to get into recovery failed but I somehow managed to get into the fastboot mode. So I downloaded the stock ROM in hopes of reverting to stock and starting all over. Whatever I did, I couldn't establish an ADB connection and I was starting to panic. It looked like a dead end.

Then I started redoing things, when I tried a different key combination, it jumped to the custom recovery and thankfully all was not lost. This time I flashed Magisk and it worked.

**Update**:

It's been weeks now and it's stable. No issues so far. Battery life is just amazing and performance has improved a lot!
