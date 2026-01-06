---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: My Post
  image: "@assets/wp-content/uploads/2018/03/my-post.jpg"
date: "2018-03-07T15:05:35+00:00"

summary: Adaptive delta modulation is used to improve the efficiency of the delta modulator by varying the **Δ** and step duration.
tags:
  - adm
  - circuit
  - modulation
  - pspice
  - spice

title: Adaptive Delta Modulation - PSPICE
---
Adaptive delta modulation is used to improve the efficiency of the delta modulator by varying the **Δ** and step duration.

This is achieved by varying the gain of the integrator circuit in the following figure.The different values of gain are selected by the IC 74163 MUX.

The circuit sure looks scary at first. :P

![Screenshot (288).png](@assets/wp-content/uploads/2018/03/screenshot-288.png)

Even after verifying everything I'm not getting a satisfactory adaptive delta modulated output. Planning to look into it later when I'm free.

The files are attached [here](https://drive.google.com/open?id=1x3j4x26xhVS1SGaCFkRHzBZj9qZtNZMZ).
