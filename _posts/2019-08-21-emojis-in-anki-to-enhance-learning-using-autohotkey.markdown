---
author: glenzac
comments: true
date: 2019-08-21 03:06:53+00:00
layout: post
link: https://glenzac.wordpress.com/2019/08/21/emojis-in-anki-to-enhance-learning-using-autohotkey/
slug: emojis-in-anki-to-enhance-learning-using-autohotkey
title: Emojis in Anki to enhance learning - using AutoHotkey
wordpress_id: 1316
categories:
- Tinkering 🛠️
tags:
- Anki
- Autohotkey
- code
- learning
- scripts
---


<!-- more -->


Emojis make memorizing things easier. But I found it very cumbersome to add emojis on Anki. The normal Windows 10 (Win + .) emoji keyboard didn't work. I tried other ways but that too never produced color emojis. However, copy-pasting from an online emoji database seemed to work. But copy-pasting every time you need an emoji is not feasible. So I wrote a simple AutoHotkey script that sends the Unicode characters of the emojis when a hotkey is entered.












[caption id="" align="alignnone" width="1366"]![](https://i.imgur.com/0g5CnjR.jpg) The text next to the emojis are only possible use-cases and not the keyword[/caption]














    
    eg:- Using :flag: results in 🚩










I've restricted my list to only few emojis that I think are the most essential in making cards.






















The keywords (hotkey) to use can be found by opening the .ahk file with a text editor. Feel free to add your own emojis and modify the hotkeys.










Note: This is not an Anki addon. It's a script that runs separately in the background.










Know issue: Sometimes certain emojis don't seem to work. I haven't yet figured out why. But the problem gets fixed either with a reload of the script (Alt + r) or by typing another hotkey.













[Download](https://drive.google.com/open?id=1uCUaU2mk7VcQup6YhM6q4ebGAMd_2iem)






















**Code:**






[code language="cpp"]
#NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir% ; Ensures a consistent starting directory.
#SingleInstance force

#Hotstring EndChars :
#Hotstring 0

:::bulb::
send % chr(0x1F4A1)
return

:::100::
send % chr(0x1F4AF)
return

:::ok::
send % chr(0x1F44C)
return

:::v::
send % chr(0x270C)
return

:::left::
send % chr(0x1F448)
return

:::right::
send % chr(0x1F449)
return

:::up::
send % chr(0x1F446)
return

:::down::
send % chr(0x1F447)
return

:::+1::
send % chr(0x1F44D)
return

:::-1::
send % chr(0x1F44E)
return

:::eyes::
send % chr(0x1F440)
return

:::anchor::
send % chr(0x2693)
return

:::zap::
send % chr(0x26A1)
return

:::fire::
send % chr(0x1F525)
return

:::medal::
send % chr(0x1F3C5)
return

:::target::
send % chr(0x1F3AF)
return

:::textbook::
send % chr(0x1F4DA)
return

:::pin::
send % chr(0x1F4CC)
return

:::key::
send % chr(0x1F511)
return

:::link::
send % chr(0x1F517)
return

:::warning::
send % chr(0x26A0)
return

:::stop::
send % chr(0x26D4)
return

:::checkbox::
send % chr(0x2705)
return

:::wrong::
send % chr(0x274C)
return

:::flag::
send % chr(0x1F6A9)
return

!r::Reload

[/code]















**If you're new to AHK: **[Documentation](https://www.autohotkey.com/docs/AutoHotkey.htm)





















