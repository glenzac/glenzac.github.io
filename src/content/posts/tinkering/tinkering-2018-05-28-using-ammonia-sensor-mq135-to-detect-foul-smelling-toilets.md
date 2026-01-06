---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: mq135-gas-sensor-2
  image: "@assets/wp-content/uploads/2018/05/mq135-gas-sensor-2.jpg"
date: "2018-05-28T12:29:23+00:00"

summary: ""
tags:
  - ammonia
  - electronics
  - gas
  - mq135
  - mq137
  - sensor

title: Using ammonia sensor - MQ137 to detect when a toilet needs cleaning?
---


## **Challenges**

1. **Standard detecting conditions required are 20°C ± 2°C and 65%± 5% relative humidity(RH) with 95%RH being the maximum.** The relative humidity in toilets can very often go above 95% thus, affecting the readings**.**
1. **Detecting scope of an MQ137 sensor is 10 ppm to 300 ppm** Our required functional data lies very close-to or below the lower limit of the sensor. (To give an idea of the scale of magnitudes: Ammonia at about 30 ppm can cause eye/nose irritation)
1. **Household and industrial cleaning solutions may contain ammonia.** This can trigger false positives.
1. **An added power consumption of ~800 mW on the board due to the presence of heating coils that are required for the sensor to operate.** We might need to alter the onboard power supply if it was designed for a specific current rating.
1. **Not selective to one particular gas, it can be affected by other gases like CO2, NOx, alcohol, smoke etc.** Since the MQ135 measures gas concentration based on changes in conductivity, it can be affected by other gases like CO2 ( CO2 is denser than air and hence does not rise up easily - since sensor is placed at head level it is more prone to being negatively affected by CO2) or alcohol which is found in antiseptic solutions.
1. **The sensitivity of the sensors will be reduced when spattered or dipped in water.** There is always a possibility of the sensor to come in contact with water (as it is exposed).
1. **Prolonged exposure to adverse conditions (like high humidity) will permanently affect the sensor's performance.** Hence they might need periodic calibration

## **Conclusion**

 **The reliability of using the MQ135 sensor for a valid data point is questionable**. **There are too many factors at play in harsh environments like toilets.** **Need to test it in the real world before I conclude anything.**\[Note : All the above conclusions are drawn based on the MQ135 datasheet\]
