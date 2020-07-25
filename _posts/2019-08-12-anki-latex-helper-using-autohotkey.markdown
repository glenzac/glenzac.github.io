---
author: glenzac
comments: true
date: 2019-08-12 10:36:35+00:00
layout: post
link: https://glenzac.wordpress.com/2019/08/12/anki-latex-helper-using-autohotkey/
slug: anki-latex-helper-using-autohotkey
title: Anki LaTeX Helper using AutoHotkey
wordpress_id: 1282
categories:
- Tinkering 🛠️
tags:
- Anki
- Autohotkey
- code
- LATEX
- learning
- scripts
---

<!-- more -->

It's been a while since I've started using Anki for learning mathematical equations and various other formulae. I didn't have much trouble typing in the equations as I already knew LaTeX. But this is not the case for most people using Anki. I've seen a lot of people requesting devs to add buttons to Anki that will make it easier to type in equations. But, LaTeX seems almost irreplaceable when it comes to formatting things the way you want it.

Hence, the script I've written only eases the process of adding many equations at once. This is written in the famous scripting language called [AutoHotkey](https://www.autohotkey.com/).

If you're new to AHK: [Documentation](https://www.autohotkey.com/docs/AutoHotkey.htm)

People have already made comprehensive [hotkeys](https://autohotkey.com/board/topic/6949-script-for-latex/) covering almost all of the LaTeX syntax, but I find it too overwhelming to learn all of the shortcuts. A GUI solution was more preferable.

This is a script I wrote in 2 hours with just basic knowledge of AHK. Hence, it's a very crude implementation that involves <del>quickly changing window focus and sending in keystrokes when buttons are pressed in a GUI.</del> **Update: **directly sending keystrokes to the Anki Add window. Nevertheless, it works as intended.

**Note:** This is not an Anki addon. It's a script that runs separately in the background. Let's call it **Anki Latex Helper (ALH)**. I've only added the most commonly used LaTeX symbols.


## Screenshots


[caption id="" align="alignnone" width="1366"]![](https://i.imgur.com/zRFsKD3.jpg) The ALH window within Anki[/caption]

![](https://i.imgur.com/vJKFLo1.gif)

![](https://i.imgur.com/JlMRRJM.jpg)

[caption id="" align="alignnone" width="1366"]![](https://i.imgur.com/dcptrav.gif) The script automatically moves the cursor to the right position.[/caption]

[caption id="" align="alignnone" width="1042"]![](https://i.imgur.com/hVOBVaZ.jpg) List of all the included symbols, as seen in the Anki preview screen[/caption]


## How does it work?


I've simply created a window and added many buttons to it. These buttons when clicked, sends out keystrokes to the text field that types in the required syntax and also moves the cursor to the right place. <del>But to do this simple thing the application where text needs to be entered should be in focus, hence this app momentarily loses focus sends the keystrokes and comes back up. This is why it keeps flashing with every click. ( Experts out there, am I missing something? )</del>


**Update:** This script directly sends the required keystrokes to the specific window, in this case the Anki 'Add' window.


I've also made this window to stay on top of all other applications for it to be always visible. I removed the title bar and made the GUI transparent just to make it look better. The window automatically positions itself at the right place every time. (i.e with Anki window maximized)

**Note:** ALH stays on top until you use the shortcuts below to minimize or close it.

![](https://i.imgur.com/1aQiF6R.jpg)


### **Shortcuts:**




### Alt-J to restore the window
Alt-K to minimize the window
Alt-L to stop the script and close ALH.


(You can easily change these in the code)


## **Installation**





	
  1. Download [AutoHotkey](https://www.autohotkey.com/) and install it.

	
  2. Download the Anki LaTeX Helper.ahk script attached below and simply double click to run it. Voila!


Just run the script whenever you need to add in equations.


## **Things to work on: **





	
  1. Find out better workflows to implement this.

	
  2. <del>Prevent ALH from flashing with every button press.  </del> (Thanks to reddit user [Khonkhortisan's](https://www.reddit.com/user/Khonkhortisan/) suggestions.)

	
  3. Replace the text in the buttons with the actual symbols

	
  4. Add more buttons?




## **Code**


The code is well commented and pretty straight forward so it's quite easy to modify it as per your needs.

[code language="cpp"]
;-------------------------------------------
; Author: Glen Zachariah
; License: MIT License
; Copyright (C) 2019
; ------------------------------------------

; --------------------- GUI ---------------------

Gui, +AlwaysOnTop ; Forces window to stay on top
Gui, -Caption ; Removes the titlebar
Gui +ToolWindow ;comment this if you want the program window in the taskbar
Gui, Color, EEAA99 ; Color set and will be made transparent below
Gui +LastFound
WinSet, TransColor, EEAA99
Gui, Font, S10 CDefault Bold, Verdana ; Set Font and size

Gui, Add, Button, x22 y19 w100 h70 , LaTeX
Gui, Add, Button, x22 y109 w100 h70 , Fraction
Gui, Add, Button, x142 y19 w100 h70 , Integral
Gui, Add, Button, x262 y19 w100 h70 , Partial
Gui, Add, Button, x502 y19 w100 h70 , Omega
Gui, Add, Button, x622 y19 w100 h70 , pi
Gui, Add, Button, x742 y19 w100 h70 , Nabla
Gui, Add, Button, x382 y19 w100 h70 , Del
Gui, Add, Button, x862 y19 w100 h70 , phi
Gui, Add, Button, x22 y199 w100 h70 , Bar
Gui, Add, Button, x142 y109 w100 h70 , Differential
Gui, Add, Button, x262 y109 w100 h70 , Sum
Gui, Add, Button, x382 y109 w100 h70 , delta
Gui, Add, Button, x502 y109 w100 h70 , sigma
Gui, Add, Button, x622 y109 w100 h70 , rho
Gui, Add, Button, x742 y109 w100 h70 , lambda
Gui, Add, Button, x862 y109 w100 h70 , Infinity
Gui, Add, Button, x142 y199 w100 h70 , DDifferential
Gui, Add, Button, x262 y199 w100 h70 , SqRoot
Gui, Add, Button, x382 y199 w100 h70 , =
Gui, Add, Button, x742 y199 w100 h70 , .
Gui, Add, Button, x862 y199 w100 h70 , x
; Generated using SmartGUI Creator for SciTE

Gui, Show, Center Y300 w990 h295, Anki LaTeX Helper
; Modify the xx value in Yxx to change vertical position

return

;----------Button Functions-------------------

ButtonLaTeX:
WinActivate, Add
SetTitleMatchMode, 2
ControlSend,, ^+{t} , Add
ControlSend,, m, Add
WinActivate, Add
return

ButtonFraction:
SetTitleMatchMode, 2
ControlSend,,{Raw} \frac{}{} , Add
ControlSend,, {Left 3} , Add
WinActivate, Add
return

ButtonIntegral:
SetTitleMatchMode, 2

ControlSend,, {Raw} int_{}^{}, Add
ControlSend,, {Left 4} , Add
WinActivate, Add
return

ButtonDifferential:
SetTitleMatchMode, 2
ControlSend,, {Raw} \frac{d}{dx} , Add
WinActivate, Add
return

ButtonDDifferential:
SetTitleMatchMode, 2
ControlSend,, {Raw} \frac{d^2}{dx^2} , Add
WinActivate, Add
return

ButtonSum:
SetTitleMatchMode, 2
ControlSend,, {Raw} \sum_{n=-\infty}^{\infty} , Add
ControlSend,, {Left 19} , Add
WinActivate, Add
return

ButtonInfinity:
SetTitleMatchMode, 2
ControlSend,, {Raw} \infty , Add
WinActivate, Add
return

ButtonSqRoot:
SetTitleMatchMode, 2
ControlSend,, {Raw} \sqrt{} , Add
ControlSend,, {Left 1} , Add
WinActivate, Add
return

ButtonPartial:
SetTitleMatchMode, 2
ControlSend,, {Raw} \frac{\partial}{\partial x} , Add
WinActivate, Add
return

ButtonOmega:
SetTitleMatchMode, 2
ControlSend,, {Raw} \omega , Add
WinActivate, Add
return

ButtonNabla:
SetTitleMatchMode, 2
ControlSend,, {Raw} \nabla , Add
WinActivate, Add
return

ButtonDel:
SetTitleMatchMode, 2
ControlSend,, {Raw} \Delta , Add
WinActivate, Add
return

Buttondelta:
SetTitleMatchMode, 2
ControlSend,, {Raw} \delta , Add
WinActivate, Add
return

Buttonsigma:
SetTitleMatchMode, 2
ControlSend,, {Raw} \sigma , Add
WinActivate, Add
return

Buttonrho:
SetTitleMatchMode, 2
ControlSend,, {Raw} \rho , Add
WinActivate, Add
return

Buttonlambda:
SetTitleMatchMode, 2
ControlSend,, {Raw} \lambda , Add
WinActivate, Add
return

ButtonPhi:
SetTitleMatchMode, 2
ControlSend,, {Raw} \phi , Add
WinActivate, Add
return

ButtonBar:
SetTitleMatchMode, 2
ControlSend,, {Raw} \bar{} , Add
ControlSend,, {Left 1} , Add
WinActivate, Add
return

Button=:
SetTitleMatchMode, 2
ControlSend,, {Raw} \geq , Add
WinActivate, Add
return

ButtonImplies:
SetTitleMatchMode, 2
ControlSend,, {Raw} \Rightarrow , Add
WinActivate, Add
return

Buttonpi:
SetTitleMatchMode, 2
ControlSend,, {Raw} \pi , Add
WinActivate, Add
return

Button.:
SetTitleMatchMode, 2
ControlSend,, {Raw} \cdot , Add
WinActivate, Add
return

Buttonx:
SetTitleMatchMode, 2
ControlSend,, {Raw} \times , Add
WinActivate, Add
return

;--------------------------------------------

;Shortcut to restore window
!j::
Gui, Restore
return
;Shortcut to minimize window
!k::
Gui, Minimize
return
;Shortcut to close window and stop script
!l::
ExitApp

; Uncomment the following if you enable the titlebar/caption
; GuiClose:
; ExitApp
[/code]

I'll be working on this in my free time. Comment below if you have any suggestions or questions. Feel free to modify the script and add your own required symbols and customizations. Also don't forget to share your work here.

[Download ALH](https://drive.google.com/open?id=1lSg1zZBQn2ekIEEks_eIEnR8DrFt3g3H)

Updated: 13/8/19 : 

[Download ALH_1.1](https://drive.google.com/open?id=1ZtAtBh47JwxCOTiV7hWqBVYGsvtRYKs4)


