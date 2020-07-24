---
layout: post
title: Making a Li-ion battery charger
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


<table width="344" >
<tbody >
<tr >

<td width="78" >Item
</td>

<td width="51" >Quantity
</td>

<td width="151" >Reference
</td>

<td width="64" >Part
</td>
</tr>
<tr >

<td >1
</td>

<td >1
</td>

<td >C1
</td>

<td >10n
</td>
</tr>
<tr >

<td >2
</td>

<td >1
</td>

<td >C2
</td>

<td >100n
</td>
</tr>
<tr >

<td >3
</td>

<td >1
</td>

<td >D1
</td>

<td >D1N4148
</td>
</tr>
<tr >

<td >4
</td>

<td >1
</td>

<td >D2
</td>

<td >4.7V zener
</td>
</tr>
<tr >

<td >5
</td>

<td >1
</td>

<td >D3
</td>

<td >Red LED
</td>
</tr>
<tr >

<td >6
</td>

<td >1
</td>

<td >Q1
</td>

<td >TIP122
</td>
</tr>
<tr >

<td >7
</td>

<td >4
</td>

<td >R1
</td>

<td >10K pot
</td>
</tr>
<tr >

<td >
</td>

<td >
</td>

<td >R5
</td>

<td >10k
</td>
</tr>
<tr >

<td >
</td>

<td >
</td>

<td >R8
</td>

<td >10k
</td>
</tr>
<tr >

<td >
</td>

<td >
</td>

<td >R12
</td>

<td >10k
</td>
</tr>
<tr >

<td >8
</td>

<td >1
</td>

<td >R2
</td>

<td >68k
</td>
</tr>
<tr >

<td >9
</td>

<td >2
</td>

<td >R3
</td>

<td >1k
</td>
</tr>
<tr >

<td >
</td>

<td >
</td>

<td >R7
</td>

<td >1k
</td>
</tr>
<tr >

<td >10
</td>

<td >1
</td>

<td >R4
</td>

<td >4.7k
</td>
</tr>
<tr >

<td >11
</td>

<td >1
</td>

<td >R6
</td>

<td >1
</td>
</tr>
<tr >

<td >12
</td>

<td >1
</td>

<td >R9
</td>

<td >1.2k
</td>
</tr>
<tr >

<td >13
</td>

<td >1
</td>

<td >R10
</td>

<td >1.5k
</td>
</tr>
<tr >

<td >14
</td>

<td >1
</td>

<td >R11
</td>

<td >100k
</td>
</tr>
<tr >

<td >15
</td>

<td >1
</td>

<td >R13
</td>

<td >560
</td>
</tr>
<tr >

<td >16
</td>

<td >1
</td>

<td >U1,U2,U3
</td>

<td >LM324
</td>
</tr>
<tr >

<td >17
</td>

<td >1
</td>

<td >
</td>

<td >Heat sink
</td>
</tr>
<tr >

<td >18
</td>

<td >1
</td>

<td >
</td>

<td >Power jack
</td>
</tr>
</tbody>
</table>


## Making it :


---------------------------------------------------------------------------------------------------------------------------


### Update : 05/2020: 


I finally designed a PCB and here's the link to the [post](https://glenzac.github.io/2020/05/18/li-ion-battery-charger-pcb-design/).

---------------------------------------------------------------------------------------------------------------------------

Getting PCB's printed was not economical so I had to do with manual wiring and soldering (yes it did take a couple of hours! )

[caption id="attachment_808" align="alignnone" width="2710"]![Untitled picture.png](https://glenzac.files.wordpress.com/2018/09/untitled-picture.png) Laying out the components[/caption]

[caption id="attachment_media-358" align="alignnone" width="1280"]![photo_2018-09-20_00-01-33.jpg](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-01-33.jpg) Soldering the parts in place[/caption]

[caption id="attachment_811" align="alignnone" width="1280"]![photo_2018-09-20_00-01-15](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-01-15.jpg) Finally![/caption]

[caption id="attachment_810" align="alignnone" width="1280"]![photo_2018-09-20_00-01-21](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-01-21.jpg) This is how the bottom looks 😅[/caption]

[caption id="attachment_815" align="alignnone" width="1280"]![photo_2018-09-20_00-09-05](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-09-05.jpg) The 4.1V reference[/caption]

[caption id="attachment_814" align="alignnone" width="1280"]![photo_2018-09-20_00-01-27](https://glenzac.files.wordpress.com/2018/09/photo_2018-09-20_00-01-27.jpg) Voltage across 1 ohm resistor = 0.32V => 0.32A charging current[/caption]

I tested it using different batteries with different capacities and it just works great!
