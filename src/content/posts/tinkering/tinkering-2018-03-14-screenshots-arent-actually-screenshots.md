---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: pexels-photo-301718
  image: "@assets/wp-content/uploads/2018/03/pexels-photo-301718.jpeg"
date: "2018-03-14T16:36:20+00:00"

summary: Screenshots play a vital role in our day to day lives be it in the form of stealing memes/status updates, storing evidence, getting help etc.
tags:
  - android
  - customrom
  - lspeed
  - screenshot

title: Screenshots aren't actually 'screen'shots
---
Screenshots play a vital role in our day to day lives be it in the form of stealing memes/status updates, storing evidence, getting help etc. 

I decided to dig in deeper and find out what's actually happening when you take a screenshot. [Wikipedia](https://en.wikipedia.org/wiki/Screenshot) didn't offer any information on the technique used. An answer on  Quora popped up as one of the top search results for the query. The falling credibility of Quora as a Q/A platform is long enough for another post. So that too didn't help.

Then I started testing it out myself in different scenarios - full screen, overlays, split screen etc. The only thing I thought, I understood was that the data that was pushed to the screen was being stored - Just like the 'Freeze' function found on projectors. To test my hypothesis I decided to do an experiment.

I used root privileges and [Lspeed](https://play.google.com/store/apps/details?id=com.paget96.lspeed&hl=en) to make my screen monochromatic. Then I took a screenshot, surprisingly, the image was not monochromatic but in full colour.

![Screenshot_20180311-195839 (1).png](@assets/wp-content/uploads/2018/03/screenshot_20180311-195839-1.png)

To prove that I actually took a screenshot with a monochromatic screen, I decided to shoot a video with a camera. But then the inbuilt screen recording feature quickly came to my mind and I decided to screen record me taking a screenshot, fully knowing the likely outcome. I was in for another surprise when I found the screen recording to be monochrome.The gif for it is attached below.

![ezgif.com-video-to-gif.gif](@assets/wp-content/uploads/2018/03/ezgif-com-video-to-gif1.gif)

So here I am, back at square one. Screenshots in Android don't work the way I expected it to work. Screen recording probably keeps on storing information about each frame. But they should have technically worked the same way. Why would anyone implement them differently?

Too many questions and I finally turned to Stack Exchange. Here's the link to the question :

[https://android.stackexchange.com/questions/192061/how-is-screen-recording-different-from-a-screenshot-with-respect-to-the-way-it-i](https://android.stackexchange.com/questions/192061/how-is-screen-recording-different-from-a-screenshot-with-respect-to-the-way-it-i)

At the time of this writing, the question hasn't been answered yet. Will update if at all anybody answers it.
