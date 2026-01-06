---
author: glenzac
categories:
  - uncategorized
cover:
  alt: creative internet computer display
  image: "@assets/wp-content/uploads/2020/06/pexels-photo-2004161.jpeg"
date: "2020-09-02T18:56:24+00:00"

tags:
  - linux
  - perl
  - python
  - windows
  - wsl

title: Thoughts on the Windows Subsystem for Linux
---
**Should I move to Linux?**

I've been occasionally asking myself this question for a really long time. The urge to move, reaches a peak when I'm starting to learn a new programming language or when any of those pesky proprietary background processes on Windows decide to devour all of my CPU and RAM.

I had asked myself this question when I was [starting with ROS](/2017/07/24/my-experiments-with-ros/), when I needed a full fledged development station for my college project, when I was learning Git and using cygwin and what not. My biggest concerns were software compatibility and the fear of messing up my daily driver PC and putting at stake, all my personal files. I did take the leap once and went forward with dual booting Ubuntu on my PC. Dual booting meant that I had to let go of the hibernating feature (which I tend to overuse) and try my best to avoid conflicts between the systems as the same drive was accessed in both OSes. Linux hates NTFS file systems and Windows hates EXT file systems. Most often, even after a clean shutdown from Windows, the drives were un-mountable in Linux and I found myself in a mucky locked-up situation. Getting Ubuntu and grub out of the system and fixing the Windows bootloader is another headache. It needs those repair discs or stock images and everything. After that episode, I swore to never dual-boot a system. I either solely run Linux or use virtualization to run it on Virtual Box.

Couple of months back, when I was jobless and working on making a [streaming device using the Raspberry pi](/2020/05/26/youtube-tv-using-the-raspberry-pi-on-raspbian-with-hdmi-cec/) that was when I truly got to indulge into the Linux file system and tweak every tiny bit of those config files, run automatic scripts, build GUIs in Python and all those. I truly got to understand the benefits and was so overwhelmed by the sheer control over the system that the question on top again popped up into my mind. I decided to search for my options and maybe try out a new flavour of Linux. Ubuntu had a lot of bloat. I needed something lighter to work on. I also had to buy a Hard disk to backup all my personal files and photos, just in case. I was almost getting ready to make the shift to Linux from Windows. I made a list of all the software that I would have to let go, which includes everything to do with the Adobe suite, the games I played from time to time, my [AutoHotKey scripts](/2019/08/12/anki-latex-helper-using-autohotkey/) and a lot of such things. It was quite a sacrifice.

Once the decision was made, I thought to download the files and go about making a image of my existing Windows system. While searching for this, I came across something called WSL - The Window's Subsystem for Linux. In short it is simply the whole Linux environment built straight into Windows. I couldn't believe my eyes when I found Ubuntu as just a simple app on the Microsoft Store that I could install and use just like a new system. Okay wait... this only gives me the Linux Terminal. No flashy GUI or X or anything, just bare bones Linux nothing less, nothing more. Hmmm ...so I anyways decided to try it out before making 'The Big Move'. It was around 1GB and once installed I had to also download the new [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) and had to do the initial configuration. Once done, I literally had Linux within Windows and very surprisingly the system resource usage was very very less compared to dedicating resources for a virtual machine. It was so efficiently built into windows that I could literally keep running both. So I dropped my plan. Windows was good enough and I had to learn to do with just the terminal. But that's totally fine. There are people out there who solely only use the terminal for everything.

Fast forward 2 months and I've been using WSL almost every single day. I've learnt almost all the bash commands and I only need to see the $ to get started. Lol. My coursework requires that I know Scripting languages so that I can automate the stuff in the world of electronics - make things easier when using HDLs.

Lately, I've begun to love the simplicity of Python and it is too tempting to write anything and everything in Python. I've written a number of scripts now, that do a lot of complex arithmetic. I'm also doing this awesome [Python course](https://www.udemy.com/course/automate/) that is solely about automating boring stuff with python. Here's the companion [website](http://automatetheboringstuff.com/) which the author has generously made available for free for everyone.

I've also started learning [Perl](https://perldoc.perl.org/), just to write automation scripts. Even though, I have heard the word [regex](https://en.wikipedia.org/wiki/Regular_expression) several times before, it always scared me. Alarms would go off in my head when I saw the word regex because I've seen people write indecipherable jargon using this so called regex and do some amazing things with it. And this was literally everywhere. I've seen people use it in Excel docs, [Airtable](http://https://airtable.com), [Anki](https://en.wikipedia.org/wiki/Anki_(software)) decks and every other place. Finally, I got the chance to confront the regex beast and guess what?... it's not that hard. I'm still learning the basic things. A fellow redditor pointed out using a [Regex coach](http://www.weitz.de/regex-coach/) to interactively learn regex. That is left to be done, but sounds really promising. Who knows, it might even be worthy of a new post.

So now, just the Terminal works for me. Another interesting thing to do is to use Visual Studio Code on Windows to open the Linux WSL remotely. So now I can happily code in VSCode into a Linux system that sits right within my Windows machine.

So I can finally put this question " **Should I move to Linux?** " to rest.
