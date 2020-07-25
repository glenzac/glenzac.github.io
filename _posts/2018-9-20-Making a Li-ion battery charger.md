---
layout: post
title: Making a Li-ion battery charger
comments: true
---
![](https://img.shields.io/badge/Project-Complete-blue.svg)

<!-- more -->

I had many Lithium-ion batteries lying around from obsolete devices that could be potentially repurposed to power small projects.

**This project is based on @[pinomelean](https://www.instructables.com/member/pinomelean/)'s work out there on** **Instructables:** [**Li-ion Battery Charging**](https://www.instructables.com/id/Li-ion-battery-charging/)
It's a great guide that well explains the whole process of charging and the circuit is realised using easily available components.

So what did I do?  I realised the circuit using a rail to rail opamp and just one transistor (TIP122) => less complexity and less power loss. (as clearly suggested by @pinomelean)

Checking the datasheet of the LM324, I found that it is indeed a rail to rail opamp.

![More info in datasheet]({{ site.baseurl }}/images/more-info-in-datasheet.png)


So I removed the 2.5V virtual ground in the original circuit and tweaked few resistors here and there to come up with this reduced design.


Just to make things sure I validated the new circuit in PSPICE and it was looking great.

![New schematic]({{ site.baseurl }}/images/new-schematic.png)

**Download schematic and PSPICE files here [Download](https://drive.google.com/open?id=1yXKxjsWxHYU5TE74-5EYB8yabKiaWvr0)**
(_If at all you have a power supply with a higher current rating you can redo the design of opamp U1 in the circuit to get a higher charging current _)

**This circuit provides a max. reference of ~4.1V**. (  I prefer battery longetivity over runtime ...More details [here](https://batteryuniversity.com/learn/article/charging_lithium_ion_batteries))

If you need it exactly at 4.2V replace the only 1.2k resistor in the circuit with a single 1k resistor.


## BOM:


| Item  | Quantity  | Reference  | Part        |
|-------|-----------|------------|-------------|
| 1     | 1         | C1         | 10n         |
| 2     | 1         | C2         | 100n        |
| 3     | 1         | D1         | D1N4148     |
| 4     | 1         | D2         | 4.7V zener  |
| 5     | 1         | D3         | Red LED     |
| 6     | 1         | Q1         | TIP122      |
| 7     | 4         | R1         | 10K pot     |
|       |           | R5         | 10k         |
|       |           | R8         | 10k         |
|       |           | R12        | 10k         |
| 8     | 1         | R2         | 68k         |
| 9     | 2         | R3         | 1k          |
|       |           | R7         | 1k          |
| 10    | 1         | R4         | 4.7k        |
| 11    | 1         | R6         | 1           |
| 12    | 1         | R9         | 1.2k        |
| 13    | 1         | R10        | 1.5k        |
| 14    | 1         | R11        | 100k        |
| 15    | 1         | R13        | 560         |
| 16    | 1         | U1,U2,U3   | LM324       |
| 17    | 1         |            | Heat sink   |
| 18    | 1         |            | Power jack  |


## Making it :


---------------------------------------------------------------------------------------------------------------------------


### Update : 05/2020: 


I finally designed a PCB and here's the link to the [post](https://glenzac.github.io/2020/05/18/li-ion-battery-charger-pcb-design/).

---------------------------------------------------------------------------------------------------------------------------

Getting PCB's printed was not economical so I had to do with manual wiring and soldering (yes it did take a couple of hours! )

![Laying out the components]({{ site.baseurl }}/images/Li-ion_battery_3.png) 
**Laying out the components**

![photo_2018-09-20_00-01-33.jpg](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-01-33.jpg) 
**Soldering the parts in place**

![photo_2018-09-20_00-01-15](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-01-15.jpg) 
**Finally!**

![photo_2018-09-20_00-01-21](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-01-21.jpg) 
**This is how the bottom looks 😅**

![photo_2018-09-20_00-09-05](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-09-05.jpg) 
**The 4.1V reference**

![photo_2018-09-20_00-01-27](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-01-27.jpg) 
**Voltage across 1 ohm resistor = 0.32V => 0.32A charging current**

I tested it using different batteries with different capacities and it just works great!
