---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: IMG_20191102_095459
  image: "@assets/wp-content/uploads/2020/02/img_20191102_095459.jpg"
date: "2020-02-07T11:54:32+00:00"

summary: ""
tags:
  - electronics
  - repair
  - teardown
  - testing

title: Vintage CASIO Math Pet MP-500 teardown
---


I have this vintage device from CASIO which was actually a gift from Dad when I was in second grade or so. This is aptly named Math Pet - it helps you learn Math Tables and gives you simple arithmetic problems to solve. It also has a clock and a stopwatch.

I guess this product was released by CASIO after 1995 and it apparently it didn't sell much? I scoured the entire CASIO website looking for the product's info or the service manual. I could not find a single thing. I could not find anything much on the internet too. There were only 2-3 [websites](https://casio.ledudu.com/pockets.asp?type=1894&lg=eng) offering images of the device along with how to use it.

There was just one video on YouTube and that too just explaining its features.🤷

\[youtube <iframe width="560" height="315" src="https://www.youtube.com/embed/a8tYPwshvz8" frameborder="0" allowfullscreen></iframe>&w=1366&h=768\]

I then asked the Reddit community for help. That too didn't give any leads.

With no hope of finding a reference manual, I decided to open it up and see.

The problem:

1. The LCD display isn't clear and has poor viewing angles
1. The slider switch stopped working

![ The not so clear LCD](@assets/images/2020/BaLyd0z.jpg)

https://www.reddit.com/r/AskElectronics/comments/dq7xmm/how\_can\_i\_fix\_the\_lcd\_of\_this\_very\_old\_math/

https://www.reddit.com/r/AskElectronics/comments/dq7xmm/how\_can\_i\_fix\_the\_lcd\_of\_this\_very\_old\_math/f618vez?utm\_source=share&utm\_medium=web2x

https://www.reddit.com/r/AskElectronics/comments/dq7xmm/how\_can\_i\_fix\_the\_lcd\_of\_this\_very\_old\_math/f681229?utm\_source=share&utm\_medium=web2x

Since people were suggesting to try and clean the device and connections. I opened it up.

![ Looks pretty neat on the inside](@assets/images/2020/KttGnft.jpg)

![ Looks like a well designed device with few discrete components](@assets/images/2020/DTckkJm.jpg)

![ Ouch CASIO has dismembered the IC](@assets/images/2020/apoEaGf.jpg)

No wonder I couldn't find a reference manual. It's irreparable, components can only be replaced. Plus it's almost useless in trying to reverse engineer the IC with a logic analyzer to try and guess the IC used with these many number of pins. :(

![](@assets/images/2020/AfcPPYf.jpg)

![ If you look carefully you can see a dead ant inside (near the display filters). And how did it get there - I don](@assets/images/2020/uUAjlK9.jpg)

![](@assets/images/2020/FgT1QIu.jpg)![](@assets/images/2020/3WbSGTp.jpg)

![ The sheet that](@assets/images/2020/NYUCbKA.jpg)

![](@assets/images/2020/qvJ2BDi.jpg)

![ The slider switch is simply a piece of conductor](@assets/images/2020/ZpkbHTp.jpg)

![](@assets/images/2020/FrmzMZ4.jpg)

I did a bit of cleaning. Reassembled the whole thing back again.
The screen looked better. The slider switch hasn't improved much.

Update:
The display went back to how it was initially in just a couple of days. 😐 So it's more of a connection problem. I didn't have any IPA (iso-propyl alcohol) to clean things thoroughly. So I just ordered some. Will have to do round 2 once it arrives.
