---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: black-and-white-black-and-white-car-441103(1)
  image: "@assets/wp-content/uploads/2019/09/black-and-white-black-and-white-car-4411031.jpg"
date: "2019-11-03T16:51:14+00:00"

summary: ""
tags:
  - "#mathisfun"
  - calculations

title: Does changing the tire diameter mess up the odometer?
---


###### Photo by **[Mike](https://www.pexels.com/@mikebirdy?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)** from **[Pexels](https://www.pexels.com/photo/vehicle-tire-441103/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)**

While we were almost finalizing to a car for the family and were going through our options and various other specs, an agent told us that a particular model of the car under consideration came with 15" tires and that it also supported 16" tires. We opted for the larger tires, and when I got home I felt something amiss.

### Assumption : The odometer uses the number of tire rotations to calculate the distance driven.

Vehicle tires are mainly specified by three important parameters : wheel diameter, width and aspect ratio. See the rest [here](https://www.goodyearautoservice.com/en-US/tire-basics/tire-size).

When the wheel diameter increases the circumference also increases as follows from this elementary equation.

```
Circumference = π x Diameter
```

So a 15" tire has a circumference of 47.12 inches and a 16" tire has a circumference of 50.26 inches. i.e the 16" tire covers 50.26 inches when it rotates once.

Thus for each rotation the bigger tire covers more distance i.e 50.26 - 47.12 = 3.14 inches (or π inches more).

Thus if my assumption that odometers use the number of tire rotations to calculate distance traveled then undoubtedly there is going to be an error in the reading.

### How significant is this error?

To make this easily understandable to the majority, I'm switching over to the metric system.

```
15" = 0.381m
16"= 0.4064m
Difference = 0.4064 - 0.381 = 0.0254m
```

i.e 16" tires cover 2.5cm extra for every rotation. This might appear to be quite negligible. 👀 But don't let it fool you.

If the odometer difference **reads (and also covers)** 1000m with 15" tires:

Then the number of rotations = 1000m/0.381m = ~ 2625 rotations

If I switch over to the 16" tires and **cover exactly 1000m** (measured separately and not using the odometer):

Then the number of rotations = 1000/0.4064 ~ 2461 rotations.

Thus it has 164 less rotations and hence the odometer will read $latex \\frac{2461}{2625} \\times 1000 = 937.5m $  instead of 1000m.

Thus for every km traveled the odometer will read 62.5m less. If a car travels 100km then the odometer will read 6.25km less. If it travels 10,000km the odometer will read 625km less. 😱

**Conclusion :** If you increase your tire size your odometer will read less than the actual distance covered. If you use the odometer reading to calculate mileage that too will have errors. The only benefit I see here is that when you sell your car it'll be more worthy thanks to the extra distance that doesn't show up on the odometer. 🤣😅
