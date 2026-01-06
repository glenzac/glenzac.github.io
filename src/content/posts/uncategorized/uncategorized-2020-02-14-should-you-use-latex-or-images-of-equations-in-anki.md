---
author: glenzac
categories:
  - uncategorized
cover:
  alt: black and white blur book business
  image: "@assets/wp-content/uploads/2020/02/pexels-photo-240163.jpeg"
date: "2020-02-14T05:47:12+00:00"

summary: ""
tags:
  - latex
  - opensource
  - opinions

title: Should you use LaTeX or images of equations in Anki?
---


I've extensively tried both and here are my findings:

## Why should you use LaTeX:

- if you have enough time before your exams to make all the cards
- makes it easy to edit and simplify those difficult cards later
- It's hard to make photos of equations in uniform font size and fonts when you're collecting information from different sources
- if fonts or size are not uniform - we'd inadvertently make use of the non-uniformity while reviewing but that doesn't ensure that we actually learned the card.
- I sometimes [color code](https://www.overleaf.com/learn/latex/Using_colours_in_LaTeX) portions of my equation to make it easy to remember....but that is not directly possible with images.
- if at all you later decide to change the way all your equations look you can just edit the LaTeX options in the manage note type menu.

I find it more difficult to make equations in an ordinary equation editor than type out its equivalent LaTeX.

I made a simple AHK tool to quickly enter LaTeX equations into Anki. Preview : ![](@assets/images/2020/vJKFLo1.gif)

Link to the post on [reddit](https://www.reddit.com/r/Anki/comments/cpb1rs/anki_latex_helper_using_autohotkey/).

Download this script from [here](/2019/08/12/anki-latex-helper-using-autohotkey)

## Why should you use images:

- when you're running short of time and LaTeX seems to be too difficult
- I use images when I need to [annotate my equations or draw arrows to show relations](https://i.imgur.com/aVtu5k8.jpg) ( I use OneNote for that)
- when you have access to all equations in uniform fonts
- if you don't mind the repeated process of blurring images/deleting sections when you're make a lot of cards (Note: [Image Occlusion](https://ankiweb.net/shared/info/1374772155) is still in alpha for Anki 2.1 :( but nevertheless it works okay )
- If you are sure you won't be editing cards later
