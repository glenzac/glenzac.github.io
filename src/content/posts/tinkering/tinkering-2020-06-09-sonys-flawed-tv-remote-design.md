---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: 5G290g31
  image: "@assets/wp-content/uploads/2020/06/5g290g31-1.jpg"
date: "2020-06-09T16:58:16+00:00"

summary: ""
tags:
  - battery
  - design

title: SONY's flawed TV remote design
---


The remote was only working intermittently when I thought the battery was nearing its end. Opening the back cover gave me rude shock. A single AA Eveready Ultima Battery had leaked. A leak would have been acceptable if it was the ordinary red or yellow coloured Eveready battery. Instead this was the Ultima 😐. Very disappointing.

Putting in fresh new batteries after cleaning the battery compartment too didn't help any bit. So I decided to pry it open.

![](@assets/images/2020/h0BpU5Z.jpg)

![](@assets/images/2020/5G290g3.jpg)

The chemical reaction between the electrolyte and the rubber pad had turned the black thing to orange in colour where the leak occured.

### **The Design flaw:**

SONY had placed the controller IC just behind the battery slot. That means any leak had direct chance of affecting the IC. After all these batteries contain conducting electrolytes that can easily short IC pins. 🤦‍♂

Instead of placing it away from the batteries they placed it right along with it. 😐 I've seen other manufacturers now place batteries along the lenght of the remote. I haven't yet opened one to notice the change in position of ICs. Some brands have moved to coin cells which are less prone to leaks.

![](@assets/images/2020/03wPqAr.jpg)

![](@assets/images/2020/tHcnTl3.jpg)

The damage to the PCB is clearly visible near the battery terminal on the left.

![](@assets/images/2020/5jnYh7C.jpg)

Another area that appears to be affected with the leak. So I decided to clean the whole thing. Took out the rubber - washed it in soap water to remove the dirt and dried it using a hair dryer😅.

This was followed by 3 rounds of cleaning of the PCB using IsoPropyl Alcohol (IPA) and cotton swabs.

![](@assets/images/2020/0xH0hxK.jpg)

![](@assets/images/2020/mjkXCm4.jpg)

![](@assets/images/2020/oq7tM3C.jpg)

![](@assets/images/2020/3yZ2pjN.jpg)

The orange coloured discolouration appears to be permanent. I put everything back in place and tried the remote. Half the buttons had started working. Still the media playback buttons and the volume up key and the return key was not working. As a last resort, I decided to try and resolder all the connections. I did the resonator and the caps easily. The SMD is still difficult for me. So I just touched the soldering rod steadily on the pins in hopes of redoing joints. This did the trick. Almost all the buttons started working now. 😁
