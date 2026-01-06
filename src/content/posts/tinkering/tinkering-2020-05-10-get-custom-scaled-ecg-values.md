---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: heart-rate-1375324_1280
  image: "@assets/wp-content/uploads/2018/11/heart-rate-1375324_1280.png"
date: "2020-05-10T10:38:15+00:00"

summary: '![](https://img.shields.io/badge/Project-Complete-blue.svg)'
tags:
  - ecg
  - excel
  - spreadsheet

title: Get custom scaled ECG values
---
![](https://img.shields.io/badge/Project-Complete-blue.svg)

Raw ECG signals which are in the 0-4 mV range are pretty much too small to do anything with. Hence an [AFE](/2019/04/23/ecg-analog-front-end-design/) is used to bring the ECG signals to the desired range. If we are designing a circuit that uses this amplified ECG signal, we should use a different ECG signals source or PWL source with different values.

Keeping this in mind, I created this simple spreadsheet tool (linked below) to scale ECG waveform values into the required range. The raw values are taken from the **MIT-BIH Normal Sinus Rhythm Database** and the first 30 seconds of the **16265** record.

![](@assets/images/2020/pSn0rUW.jpg)![](@assets/images/2020/IlEpEww.jpg)![](@assets/images/2020/K4fYJ95.jpg)

If you wish to produce these signals using a DAC use the sheet titled 'DAC\_values'. For more information see this [post](/2019/05/17/generating-ecg-eeg-signals-with-a-microcontroller/).

Link to spreadsheet:

[Custom ECG values](https://docs.google.com/spreadsheets/d/146w_0uU9As0id8H1MLw_fddu173FlqVm8nAkZ5s5otE/edit?usp=sharing)

Simply download the sheet and use as required. Suggestions and modifications are welcome.
