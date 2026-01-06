---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: My Post (1)
  image: "@assets/wp-content/uploads/2018/03/my-post-1.jpg"
date: "2018-03-07T14:40:46+00:00"

summary: The basic modulation systems (like AM or FM) modulate the carrier signal's properties continuously based on the changing values of the message signal.
tags:
  - dm
  - modulation
  - pspice
  - spice

title: Delta modulation circuit - PSPICE model
---
The basic modulation systems (like AM or FM) modulate the carrier signal's properties continuously based on the changing values of the message signal.

When we move on to [PAM](https://en.wikipedia.org/wiki/Pulse-amplitude_modulation) (Pulse amplitude modulation) we sample the signal with a train of pulses and the amplitude of these pulses are varied according to the amplitude of the message signal.

![natural_pam](@assets/wp-content/uploads/2018/03/natural_pam.png)

Even though the signal looks incomplete at the receiver end the pulse is smoothened out using a filter.

Moving on to [PCM](https://en.wikipedia.org/wiki/Pulse-code_modulation) (Pulse-code modulation) these values of amplitudes are converted into bits say if the Vmax of the above-given signal is +5V and the Vmin is -5V then different voltage levels are assigned certain binary digits. +5V will be assigned 111 (if we are transmitting using 3 bits) and -5V will be assigned 000 and all the values that come in between will be assigned intermediate bits. So in effect, we are sending streams of 0s and 1s, this greatly helps reduce the effect of noise on the signal as we are just sending two discrete values.

[Delta modulation](https://en.wikipedia.org/wiki/Delta_modulation), I'd say is a more efficient technique because instead of sending the value of the signal at each instance (as we did for PCM) we are only sending the difference between the present value and the last value.

For example, consider our PCM signal has the following values

\[...4 5 6 7 8 7 6 5 4 3 2 1 0 1 2 3 4...\] -> a signal that resembles a sine wave (needs 3 bits)

\[...1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1...\] -> delta modulated signal (needs only one bit)

When the signal is rising we give a 1 and when it is decreasing in value we send a 0. If it is staying constant we send ...0 1 0 1 0 1...

The PSPICE circuit is as follows:

![Screenshot (286).png](@assets/wp-content/uploads/2018/03/screenshot-286.png)![spice.png](@assets/wp-content/uploads/2018/03/spice.png)

The PSPICE design files are attached [here](https://drive.google.com/open?id=1FsUaYmfV0Y9yE3v5EtJO_upz_ZUR1hSX).
