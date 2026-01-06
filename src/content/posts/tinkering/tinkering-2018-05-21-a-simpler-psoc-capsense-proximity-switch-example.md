---
author: glenzac
categories:
  - "tinkering"
date: "2018-05-21T19:43:28+00:00"

summary: ""
tags:
  - capsense
  - cypress
  - electronics
  - microcontroller
  - psoc

title: A simpler PSoC CapSense Proximity switch example
---


The built-in Capsense example of the **CY8KIT-043 PSOC 4200M** is a bit complex. So I searched their tutorials for simpler ones and found a very good one but it was implemented on a different PSoC chip. I stole the DWR (design wide resources) and the code from there and used my specific bootloader to flash my chip.

![Sketch (1).png](@assets/wp-content/uploads/2018/05/sketch-1.png)

**Then mapped the pins as follows:**![Sketch (1).png](@assets/wp-content/uploads/2018/05/sketch-12.png) **The code is as follows:**

```
#include "project.h"
int main(void)
{
CyGlobalIntEnable; /* Enable global interrupts. */
CapSense_1_Start();
CapSense_1_EnableWidget(CapSense_1_PROXIMITYSENSOR0__PROX);
CapSense_1_InitializeAllBaselines(); /* To take care of stray capacitances*/
CapSense_1_ScanEnabledWidgets();

for(;;)
{
/* Place your application code here. */
if (CapSense_1_IsBusy()==0)
{
LED_Write(CapSense_1_CheckIsWidgetActive(CapSense_1_PROXIMITYSENSOR0__PROX));
CapSense_1_UpdateEnabledBaselines();
CapSense_1_ScanEnabledWidgets();

}

}
}

```

![IMG\_20180529\_013509\_HDR.jpg](@assets/wp-content/uploads/2018/05/img_20180529_013509_hdr.jpg)

The next thing to try is testing the same with many CSD (CapSense Devices) to turn on multiple LEDs.

As per the [datasheet](http://www.cypress.com/documentation/datasheets/psoc-4-psoc-4200-family-datasheet-programmable-system-chip-0) most of the general pins support CSD.

**Update:**

It worked perfectly. One CSD module was enough for all the proximity detectors. I only added digital outputs in each case and assigned them different pin numbers and above all made the necessary modifications in the code.
