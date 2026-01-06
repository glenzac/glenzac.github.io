---
author: glenzac
categories:
  - uncategorized
cover:
  alt: brain-1787622_1920
  image: "@assets/wp-content/uploads/2017/12/brain-1787622_1920.jpg"
date: "2017-10-19T10:28:05+00:00"

summary: Recently I came across the fact that the cerebellum was responsible for smoothing out muscle movement and my initial reaction was _whoa_ it's a filter of sorts and it quickly dawned on me the use of Kalman filter to smooth out values from different sensors by predicting the different state variables.
tags:
  - brain
  - cerebellum
  - filter
  - kalman
title: Kalman filter and the brain
---
Recently I came across the fact that the cerebellum was responsible for smoothing out muscle movement and my initial reaction was _whoa_ it's a filter of sorts and it quickly dawned on me the use of Kalman filter to smooth out values from different sensors by predicting the different state variables.

A quick google search confirmed my approach and there indeed is something called the " [Kalman Filter theory of the Cerebellum](https://link.springer.com/chapter/10.1007/978-1-4612-4536-0_15)"

The main argument is based on the fact that damage to the cerebellar region affected muscle movement and coordination and the author of the paper goes on to say that there exists a neural analogue of the Kalman-Bucy filter. Kalman filter is a filtering technique that uses a series of measurements along with estimates of unknown variables to produce a more accurate prediction using a joint probability distribution.

The cerebellum is said to smooth out the otherwise shaky motor movements. This is required because there is a time delay between issuing motor commands and receiving sensory feedback, even though the motor nerve conduction velocity is about 60m/s.
