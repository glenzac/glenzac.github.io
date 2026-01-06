---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: photo_2018-08-01_22-41-06
  image: "@assets/wp-content/uploads/2018/08/photo_2018-08-01_22-41-06-e1533144388268.jpg"
date: "2020-02-04T22:39:05+00:00"

summary: Today I'm going to test three different WiFi products and see if there is any difference between them.
tags:
  - testing
  - wifi

title: WiFi RSSI testing
---
Today I'm going to test three different WiFi products and see if there is any difference between them.


<Gallery cols={1}>

</Gallery>  

To standardize the test I've kept the WiFi access point \[D-Link\] at about 5 meters away and not in direct LOS. To avoid any plausible effect of interfernce on the test, I removed all wireless devices from the zone.

### 3 test cases:

1. The inbuilt WiFi adapter : **Intel(R) Dual Band Wireless-AC 3160 (driver)**
1. [iBall Baton WiFi](https://www.iball.co.in/Product/Baton/Network-Adapters/USB-Adapters/150M-Wireless---N-Mini-USB-Adapter/846) **iB-WUA150NM**
1. [AirLive **WL-1600USB**](http://www.airlive.com/support/firmware/WL-1600USB)

## 1\. In-built WiFi adapter

First I collected basic info by running Netsh in cmd (Admin)
\[Netsh is a cool cmd utility that can be used to play around with network settings \]

`Netsh WLAN show drivers`![cmd1.png](@assets/wp-content/uploads/2018/08/cmd1.png)

Here's a [guide](https://www.windowscentral.com/how-manage-wireless-networks-using-command-prompt-windows-10) to using Netsh. The following command would give the strength.

`Netsh WLAN show networks mode=bssid`![cmd2.png](@assets/wp-content/uploads/2018/08/cmd2-e1533148658556.png)

But the values were in % and not dBm. With a bit of searching, it was confirmed that extracting that sort of information was not possible from the command line. Hence I went in search of good open source tools that does the job.

My search ended here. I downloaded the freeware - [WiFi Infoview](https://www.nirsoft.net/utils/wifi_information_view.html) ![cmd3.png](@assets/wp-content/uploads/2018/08/cmd31.png)

### Result :  \- 57 dBm

## 2\. iBall Baton WiFi **iB-WUA150NM**

Then I switched off the on-board WiFi and plugged in the tiny dongle.

![cmd4.png](@assets/wp-content/uploads/2018/08/cmd4.png)**Even the signal quality is very low.**

### Result :  \- 71 dBm

## 3\. AirLive **WL-1600USB**

![cmd6.png](@assets/wp-content/uploads/2018/08/cmd6.png)

I could clearly see the Signal quality and the RSSI values change with change in orientation of the antenna.

### Result :  \- 51 dBm

* * *

{ In an IEEE 802.11 system, **RSSI** is the relative received signal strength in a wireless environment, in arbitrary units. **RSSI** is an indication of the power level being received by the receive radio after the antenna and possible cable loss. Therefore, the higher the **RSSI** number, the stronger the signal. } _Source : Wikipedia_

* * *

https://www.metageek.com has a list of acceptable signal strength values.

![Screenshot_2018-08-02 Understanding RSSI Levels MetaGeek.png](@assets/wp-content/uploads/2018/08/screenshot_2018-08-02-understanding-rssi-levels-metageek.png)

* * *

**dBm (Decibel-milliwatt)**

It is the output power in decibels referenced to 1 mW.

Since dBm is based on a logarithmic scale,for every increase of 3 dBm there is roughly twice the output power, and every increase of 10 dBm represents a tenfold increase in power.

## Verdict:

There is a difference of **6dBm** between the Airlive Dongle and the in-built WiFi adapter.

```
Using this formula:  P(mW) = 10(P(dBm)/10)

P(mW) = 100.6
                 = 3.98  ~ 4 times more received signal strength

```

**Hence Airlive Dongle is the clear winner. Now it's also very obvious that one shouldn't spend any money on small WiFi dongles that kill your speed.**

```
The antenna 🏆
```
