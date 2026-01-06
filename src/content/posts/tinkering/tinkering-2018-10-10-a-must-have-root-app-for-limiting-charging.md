---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: unnamed
  image: "@assets/wp-content/uploads/2018/10/unnamed.png"
date: "2018-10-10T22:05:07+00:00"

summary: ""
tags:
  - android
  - app
  - custom-rom
  - root

title: A must have root app for limiting charging
---


I don't know the number of times I've searched for the top root apps and all I see are the same 5-6 apps every single time on every other website.

However there are some very good, not-much-heard-of root apps out there that you very rarely stumble upon. Battery Charge Limit was one among them.

[https://forum.xda-developers.com/android/apps-games/root-battery-charge-limit-t3557002](https://forum.xda-developers.com/android/apps-games/root-battery-charge-limit-t3557002)

Now I have no intention of going into why charging your devices to 100% is bad for Li-ion batteries - I leave that to [Battery University.](https://batteryuniversity.com/) [https://batteryuniversity.com/learn/article/how\_to\_prolong\_lithium\_based\_batteries](https://batteryuniversity.com/learn/article/how_to_prolong_lithium_based_batteries)

But before you use the app you need to check if it will actually work on your device. For that, open any root file explorer and navigate to

```
sys/class/power_supply/battery/
```

Now connect the phone to a wall adaptor and open "charging\_enabled" file with any text editor and change the value from 1 to 0 and save the file. If the charging gets automatically disabled, then your phone will work with this app. So in short what this app does is tweak those values when needed, with root privilege.

I've been running this service for 2 days now and it's just great! 🔋


<Gallery cols={1}>

</Gallery>  
