---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: chart (20)
  image: "@assets/wp-content/uploads/2018/03/chart-20.png"
date: "2017-02-28T05:24:37+00:00"

summary: I used the following expression for a triangular waveform to first generate the waveform mathematically and then try and remove the higher harmonics to band limit the signal and study the effect band-limiting had on the shape of the signal.
tags:
  - band-limiting
  - excel
  - filter
  - triangular

title: 'Experiments with MS Excel: Effects of Bandlimiting - Triangular Waveform'
---
I used the following expression for a triangular waveform to first generate the waveform mathematically and then try and remove the higher harmonics to band limit the signal and study the effect band-limiting had on the shape of the signal.

![NumberedEquation1.gif](@assets/wp-content/uploads/2018/03/numberedequation1.gif)

The MS Excel file is attached [here](https://drive.google.com/open?id=1DKP6B2fjsnICPAa-asDq5d-KTAwUWc1A)

The time frame is taken to be from -10 to +10. Since I can't possibly include infinite components I decided to go for the first 5 harmonics, the expansion would then be as follows.

> =(D2-((A2/121)\*(SIN(22\*3.14\*100\*B2))))![chart (13).png](@assets/wp-content/uploads/2018/03/chart-13.png)

This is the waveform for the signal with 5 harmonics.

**Plotting the signal as I keep on cutting down on the number of components.**![chart (14).png](@assets/wp-content/uploads/2018/03/chart-14.png)![chart (15).png](@assets/wp-content/uploads/2018/03/chart-15.png)![chart (16).png](@assets/wp-content/uploads/2018/03/chart-16.png)

The equation for the signal with only the 1st component would look like this:

> =(H2-((A2/9)\*(SIN(6\*3.14\*100\*B2))))

![chart (17).png](@assets/wp-content/uploads/2018/03/chart-17.png) **And finally the band-limited signal: taking only the case: n=1 and neglecting all other higher harmonics.**

> =(A2\*(SIN(2\*3.14\*100\*B2)))![chart (18).png](@assets/wp-content/uploads/2018/03/chart-18.png)
