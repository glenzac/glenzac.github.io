---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: tl_wr740n1-cbec5
  image: "@assets/wp-content/uploads/2018/11/tl_wr740n1-cbec5.jpg"
date: "2020-06-09T20:00:30+00:00"

summary: ""
tags:
  - dd-wrt
  - router
  - wifi

title: Using custom firmware on a WiFi router
---


I had an old TP-Link TL-WR740N WiFi router lying around - unused. Since I have a separate D-Link router that I use for an internet connection. This automatically qualified the TL-WR740N for tinkering  ;) .

[DD-WRT](https://dd-wrt.com/) is one popular choice and so I decided to stick with that. ( [OpenWRT](https://openwrt.org/) is another alternative out there)

Before you spend anytime on reading the instructions, it is advisable to check if your router supports DD-WRT. [https://wiki.dd-wrt.com/wiki/index.php/Supported\_Devices](https://wiki.dd-wrt.com/wiki/index.php/Supported_Devices)
Access the router database [here](https://dd-wrt.com/support/router-database/). (But don't download any files that come on your router's page in the database - they are often outdated )

Next head over to the [wiki](https://wiki.dd-wrt.com/wiki/index.php/Main_Page) for installation instructions.

Reading the whole thing is going to take more than an hour but it's totally worth the time. If at all something goes wrong you know what to do next.

Reading list:

1. [https://wiki.dd-wrt.com/wiki/index.php/Installation](https://wiki.dd-wrt.com/wiki/index.php/Installation)
1. [https://forum.dd-wrt.com/phpBB2/viewtopic.php?t=51486](https://forum.dd-wrt.com/phpBB2/viewtopic.php?t=51486)
1. [https://wiki.dd-wrt.com/wiki/index.php/Hardware-specific](https://wiki.dd-wrt.com/wiki/index.php/Hardware-specific)
1. [https://wiki.dd-wrt.com/wiki/index.php/Recover\_from\_a\_Bad\_Flash](https://wiki.dd-wrt.com/wiki/index.php/Recover_from_a_Bad_Flash)

I didn't use the latest build over worries of instability. It's safe to use builds that are at least a couple of months old.

Download latest firmware from here : [ftp://ftp.dd-wrt.com/betas/](ftp://ftp.dd-wrt.com/betas/)

* * *

#### Flashing

![WP_20181018_17_16_43_Pro](@assets/wp-content/uploads/2018/11/wp_20181018_17_16_43_pro.jpg)

* * *

The new firmware :

![Screenshot_2018-11-02 dd-wrt (build 36168) - Info.png](@assets/wp-content/uploads/2018/11/screenshot_2018-11-02-dd-wrt-build-36168-info.png)

#### Things I did with the new custom router:

1.  Use it as a repeater for the main WiFi ![screenshot_2018-11-02-dd-wrt-build-36168-wireless.png](@assets/wp-content/uploads/2018/11/screenshot_2018-11-02-dd-wrt-build-36168-wireless-e1541176461570.png)

   Running it in client mode and setting up a virtual interface so that the TP-Link router can also be an access point. This helped increase the range of the WiFi by a large margin. The improved siganl quality also meant lesser errors while transmission => faster.
1. Changed the DNS to 1.1.1.1 -> [Cloudflare's DNS](https://blog.cloudflare.com/announcing-1111/)
   Which is [ranked](https://www.techradar.com/news/best-dns-server) the fastest free DNS out there and reportedly better than even Google's Open DNS 8.8.8.8
   ![screenshot_2018-11-02-dd-wrt-build-36168-setup1.png](@assets/wp-content/uploads/2018/11/screenshot_2018-11-02-dd-wrt-build-36168-setup1-e1541176991706.png)

There are hundreds of other cool things that can be done with the custom firmware. I'm still exploring the tricks out there.

The status page lists some cool stats.

![Screenshot_2018-11-02 dd-wrt (build 36168) - Router Status.png](@assets/wp-content/uploads/2018/11/screenshot_2018-11-02-dd-wrt-build-36168-router-status.png)**More updates later.**
