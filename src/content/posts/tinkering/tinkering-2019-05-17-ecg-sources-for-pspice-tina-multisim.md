---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: Untitled picture
  image: "@assets/wp-content/uploads/2018/11/untitled-picture1.png"
date: "2019-05-17T04:05:20+00:00"

summary: ""
tags:
  - ecg
  - multisim
  - pspice
  - tina

title: ECG sources for PSPICE, LTSPICE, TINA, Multisim
---


### Note: This post uses a text file with ECG signal values that are a bit too ideal-looking. If you want realistic ECG signals in the desired range please use this [spreadsheet tool](/2020/05/10/get-custom-scaled-ecg-values/) I've created. (It uses ECG values from the MIT-BIH Normal Sinus Rhythm Database)

## For PSPICE :

An ECG source is implemented using a Piecewise Linear source. To do this we should create a text file with the values of ECG voltages for the corresponding time. I've already done that. Download the text file [here](https://drive.google.com/open?id=1xrgt_RNGtGreaA8Z371iloxJJ-D4e_Ann7G26KgT4YI).

Now, in the parts library search for a **VPWL\_F\_RE\_FOREVER** source. ![Untitled picture.png](@assets/wp-content/uploads/2018/11/untitled-picture.png)

It should look like the image on the left. Now double-click the <FILE> and specify the location of the downloaded text file. e.g   _D:\\Downloads\\ecg\_source.txt_

Now that's your ECG source.![Untitled picture.png](@assets/wp-content/uploads/2018/11/untitled-picture1.png)

## For LTSPICE :

#### \- Method: 1

The ECG source is implemented using a Piecewise Linear source. To do this we should create a text file with the values of ECG voltages for the corresponding time. I've already done that. Download the text file [here](https://drive.google.com/open?id=1iwnLhuqCglDixIUDfQU2IDphx5zZn1KB).

- Place a Voltage source in the schematic
- Right-click the voltage source and click 'Advanced'
  ![](@assets/images/2019/DCo5Cq0.jpg)
- Then choose PWL FILE option and provide the address of the text file uploaded above. ![](@assets/images/2019/Z4RGyDO.jpg)

#### \- Method: 2

Use a .wav file as input to a voltage source

## For TINA :

![Untitled picture.png](@assets/wp-content/uploads/2018/11/untitled-picture2.png)

Files :

[ECG sources.tsc](https://drive.google.com/open?id=1Vjoqpe2VLiG-Dh8-j3T4roIhGmbSqOek)

Source :

[https://e2e.ti.com/support/amplifiers/f/14/p/248858/871282](https://e2e.ti.com/support/amplifiers/f/14/p/248858/871282)

## For Multisim:

One can either use a Labview ECG VI that is already available or a Piecewise linear source.

- Labview ECG VI - [http://www.ni.com/example/30925/en/](http://www.ni.com/example/30925/en/)
- Using a PWL source
  Files : [ECGsignals.ms11](https://drive.google.com/open?id=1FERhSDfLk0BAQM4dIjtxtb51GHkY55OZ)
  Source : [https://forums.ni.com/t5/Multisim-and-Ultiboard/simulating-ecg-signal-on-multisim/td-p/1121584](https://forums.ni.com/t5/Multisim-and-Ultiboard/simulating-ecg-signal-on-multisim/td-p/1121584)
