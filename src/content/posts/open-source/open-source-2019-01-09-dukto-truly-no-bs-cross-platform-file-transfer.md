---
author: glenzac
categories:
  - "open-source"
date: "2019-01-09T16:41:52+00:00"

summary: ""
tags:
  - app
  - opensource

title: Dukto - Truly no BS cross-platform file transfer
---


I've tried umpteen ways to send files within a single network...from FTP file managers to dedicated clients that offered a lot of flashy features. I'm not sure if it was the complexity in setting up or the apathy towards all the bloat that such applications came with, I never stuck to an application for more than a couple of days.

Only recently did I chance upon Dukto (💁‍♂ I pronounce it "duck - toe" ) and I haven't searched for another one. It does what it says, no flashy features, connects gracefully - forget manually connecting or typing in large local addresses, cross-platform and a UI that is not so bad.

![](@assets/wp-content/uploads/2019/01/dukto_xm8z5zmuq6.png)

The screenshot on the left is from the Windows Desktop app. I specify Desktop because it also has apps for Windows Phone 10 (Yes!), Android, MacOSX and even Linux and they all look the same. Truly, cross-platform.

Buddies are remote hosts (other devices) to which we can send data on the same network. Remote hosts that have Dukto opened will show up in the list automatically. There is no pairing or key matching to be done. It just connects. If at all you don't see it due to possible network restrictions you can type in the IP address. These are the things that can be done. Basically - send files.

**The features as listed on the dev's website are as follows :**

![](@assets/wp-content/uploads/2019/01/dukto_gd6dflofst.png)

- Simple user interface
- No server or internet connection needed
- Zero configuration
- Clients auto-discovery
- High-speed file transfer
- Multi-OS native support
- Portable version available
- Multi files and folders transfer
- Transfers log
- Send and receive text snippets (eg. useful for sending URLs)
- Open received files directly from the application
- Windows 7 taskbar integration with progress and transfer indicator
- Show your IP addresses on the IP connection page
- Full Unicode support
- Metro-style UI
- Free and open source

Link to the developer's page: [http://www.msec.it/blog/?page\_id=11](http://www.msec.it/blog/?page_id=11)

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpmwktxTmovn51anlqv1ldIic7dcGt-kae2U1-ZZPM2SOxXOhR)

Extras: The Dukto logo reminds me of the green warp pipes from Mario 😬

![](https://p.apk4fun.com/a5/32/c8/it.msec.dukto-icon.jpg)

### Update: 23/10/19

Apparently the developer has stopped all development and updates for Dukto  :(

Time to move on. This is what I've found : [Resilio sync](https://www.resilio.com/)  
It has all the features you'll ever need to replace Dukto in the free plan. Just install the desktop app, choose a folder to sync, install the free Resilio Sync application on your phone (Android or iOS) and then scan a code to establish a connection. And that's it! You can forget everything about connections then. The sync is seamless and there are plenty of ways to customize it too. I guess it additionally allows sharing over mobile data over using the local server. Plus this connection is way more secure than other simple connections over the local server.

If you don't want to install any apps on your phone and prefer using the browser to browse your files on the local server, then try this tool:  [https://www.rejetto.com/hfs/?f=intro](https://www.rejetto.com/hfs/?f=intro)

### Update: 8/6/20

I've slowly started adopting Open Source software whenever possible. In view of that I've moved from Resilio Sync to [Syncthing](23/10/19). It's totally free and open source. It works really well for local file transfers. For transferring files over the internet we need to setup our own server. My review of Syncthing qualifies for another post of its own. I'll link to it here once I've used Syncthing long enough to write about it.
