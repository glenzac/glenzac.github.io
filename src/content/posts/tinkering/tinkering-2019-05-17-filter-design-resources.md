---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: Screenshot_2018-11-10 Filter Wizard Analog Devices(7)
  image: "@assets/wp-content/uploads/2019/04/screenshot_2018-11-10-filter-wizard-analog-devices7.png"
date: "2019-05-17T04:05:17+00:00"

summary: '![](https://img.shields.io/badge/Post-In%20Progress-brightgreen.svg)'
tags:
  - analog-devices
  - c++
  - code
  - dsp
  - filter
  - opensource
  - ti

title: 'Filter design: Resources, tools, C/C++ code'
---
![](https://img.shields.io/badge/Post-In%20Progress-brightgreen.svg)

https://www.youtube.com/playlist?list=PL64A193CF0B94C5D3

**I don't care I just need a simple working filter:** [http://www.ti.com/general/docs/litabsmultiplefilelist.tsp?literatureNumber=sloa093](http://www.ti.com/general/docs/litabsmultiplefilelist.tsp?literatureNumber=sloa093)

## **Filter Designing Tools:**

- Analog Devices : [https://www.analog.com/designtools/en/filterwizard/](https://www.analog.com/designtools/en/filterwizard/)
- Texas Instruments : [http://www.ti.com/design-tools/signal-chain-design/webench-filters.html](http://www.ti.com/design-tools/signal-chain-design/webench-filters.html) The desktop version of the tool : [http://www.ti.com/tool/filterpro&DCMP=hpa\_amp\_general&HQS=NotApplicable+OT+filterpro](http://www.ti.com/tool/filterpro&DCMP=hpa_amp_general&HQS=NotApplicable+OT+filterpro)
- Microchip : [https://www.microchip.com/developmenttools/ProductDetails/filterlabdesignsoftware](https://www.microchip.com/developmenttools/ProductDetails/filterlabdesignsoftware)

### Update : 5/2/2019

The following website lets you design filters and it also generates the **required C code** for the filter.

[http://www-users.cs.york.ac.uk/~fisher/mkfilter/](http://www-users.cs.york.ac.uk/~fisher/mkfilter/)

### Update: 29/4/2019

 [http://www.iowahills.com/A7ExampleCodePage.html](http://www.iowahills.com/A7ExampleCodePage.html) [http://www.schwietering.com/jayduino/filtuino/index.php](http://www.schwietering.com/jayduino/filtuino/index.php)

## **Free Books on filters and DSP**

 [https://www.dsprelated.com/documents-1/mp/all.php#tabs1-popular](https://www.dsprelated.com/documents-1/mp/all.php#tabs1-popular) [http://www.dspguide.com/](http://www.dspguide.com/)

## C/C++ resources for filters/signal processing

A C++ class to implement low-pass, high-pass, and band-pass filters: [https://cardinalpeak.com/blog/a-c-class-to-implement-low-pass-high-pass-and-band-pass-filters/](https://cardinalpeak.com/blog/a-c-class-to-implement-low-pass-high-pass-and-band-pass-filters/)

Signal Processing using C++ [http://spuc.sourceforge.net/](http://spuc.sourceforge.net/) [https://github.com/ruohoruotsi/Butterworth-Filter-Design](https://github.com/ruohoruotsi/Butterworth-Filter-Design) [https://sestevenson.wordpress.com/implementation-of-fir-filtering-in-c-part-1/](https://sestevenson.wordpress.com/implementation-of-fir-filtering-in-c-part-1/)

Open source DSP library for C++:  [https://aquila-dsp.org/](https://aquila-dsp.org/) A Collection of Useful C++ Classes for DSP:  [https://github.com/vinniefalco/DSPFilters](https://github.com/vinniefalco/DSPFilters) [http://liquidsdr.org/](http://liquidsdr.org/)

C subroutine library for DFT:   [http://www.fftw.org/](http://www.fftw.org/)
