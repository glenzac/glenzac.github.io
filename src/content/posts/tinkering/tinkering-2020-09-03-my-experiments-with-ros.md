---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: ros-800x480
  image: "@assets/wp-content/uploads/2018/05/ros-800x480-e1526754294693.png"
date: "2020-09-03T00:26:29+00:00"

summary: ""
tags:
  - gazebo
  - opensource
  - opinions
  - robotics
  - ros

title: My Experiments with ROS
---
I was watching something on youtube ... Vsauce 🤔 ? when I came across a video from this company called [Boston Dynamics](https://www.youtube.com/user/BostonDynamics/featured).

<iframe width="560" height="315" src="https://www.youtube.com/embed/fRj34o4hN4I" frameborder="0" allowfullscreen></iframe>

This just blew my mind and hence began my relentless pursuit of robotics. I googled a lot about robotics, the languages used, the development, the industry, and to be honest it was overwhelming. The sheer number of different ways the same industry was growing. There were only a handful of courses on the internet that dealt with robotics. They are listed as follows :
https://www.coursera.org/specializations/robotics
https://www.edx.org/micromasters/pennx-robotics
Then there was this awesome 6-month long [Robotics Nanodegree offered by Udacity.](https://in.udacity.com/course/robotics-software-engineer--nd209) But these courses were all pretty expensive and not something I could afford 😅

This propelled me to search for open source alternatives and there was this unanimous option that turned up in all related google results - **ROS (Robot Operating System)**

Contrary to what it's called - it's not an operating system...it acts as an agent between the hardware components of the robot and the actual operating system. It runs on Linux (Ubuntu) only. So I had to play around with my VMware and created a Linux virtual machine to try ROS out.
This is your go-to place for all things ROS - http://www.ros.org/
So ROS has this crazy nomenclature procedure for its different distributions:

- Lunar Loggerhead (latest)
- Kinetic Kame
- Jade Turtle
- Indigo Igloo
- \+ everything that came before

It was a bit confusing to choose the right distro for your needs. Kinetic Kane was shown as recommended, so I just decided to go with that. Setup the sources, added and the keys and bam!

`sudo apt-get install ros-kinetic-desktop-full`

It took a while to download all the files...but everything was set up in half an hour.
I decided to start completing all the things listed in the documentation one by one to get an idea of how it works. This is where I began. http://wiki.ros.org/ROS/Tutorials

Every single day I made it a point to get through at least one page of the doc. It was too hard and I failed miserably on most days. It was very hard to understand certain core concepts of the system. **'catkin'** was one thing that set me back by days 😅. It took a while to fare through the basics of the workspace and file management and navigation. ( I also had to learn the Linux filesystem basics to go about doing tasks from the terminal)

Soon I understood that ROS Kinetic didn't yet have the full support of all features so I had to install a new machine with the almost universal Indigo. It was all smooth going until I got to more complex examples and the virtual machine started slowing down and sometimes even crashed. I saw no other option but to [dual boot](https://www.howtogeek.com/214571/how-to-dual-boot-linux-on-your-pc/) an Ubuntu and use it exclusively for ROS. This way I could use all my processing and memory on ROS. The install was quite stable and things did turn out to be way faster than when running on a virtual machine.

Then one by one I learned ` packages, nodes, topics(the Turtlesim example was pretty fun), rqt_plot.`![Screenshot-2018-5-19 ROS Tutorials UnderstandingTopics - ROS Wiki.png](@assets/wp-content/uploads/2018/05/screenshot-2018-5-19-ros-tutorials-understandingtopics-ros-wiki.png)

Then came the ` ros msg and ros serv and rosbag ` was one concept I just loved.

_Each one of these took many days to go through and often I'd get mad when things don't work out the way it's supposed to or when they returned unknown errors._ There was never a proper active forum for open discussion. Google searches of the error logs were often disappointing.

> The documentation available was good...but sparse! :(

But slowly progress happened I moved on to the Publisher and Subscriber code in C++. This was the hardest of it all... I tried a lot but..this is where I got stuck... I was getting errors and slowly I'm not sure... I guess I broke the workspace...ROS commands would often return 'not found' errors. I installed it all again on a virtual machine and tried again. This went on for a week or two... _I didn't wanna give up_... _It never worked_... I couldn't skip or move to other parts of the documentation as this was a very important part. Slowly I gave up! 😞

**After a whole no-ROS week I decided to give it one more shot.** That's when I found [Gazebo](http://gazebosim.org/) \- the platform used to simulate robots in environments using ROS. Even today it surprises me when I think that all of this is open source. (there are a lot of good people in this world 😌 ). Soon ROS was all about creating 3d models...started trying out the [examples](http://gazebosim.org/tutorials) one by one. Gazebo made things slower thanks to the 3D environment but it worked!

![simple_shapes.png](@assets/wp-content/uploads/2018/05/simple_shapes.png)

This is when I came across **URDF** or the **Universal Robot Description Format.** This was the format used to represent a robot in 3D space and define all its parameters. This was in XML and so I had to go about learning to understand and use XML. This [site](https://www.w3schools.com/xml/) made it a lot easy with very straightforward explanations and examples.

However, all these were short-lived. In a matter of days, I hit another roadblock and that was it. It more or less sealed the fate of me trying ROS on my own.
**One last attempt** before ditching went futile when the projects available in books were done in old distros and on real hardware that is very very costly. One servo ( [Dynamixel](http://www.robotis.us/dynamixel/)) even coming up to $300 (~Rs 18,000 😅) when the most expensive servo I had was the plastic geared MG995 (~Rs 400) 🤣🤣

### ---END OF STORY--

* * *

### **Update: _2018_**

It's been more than a year. I got [this](https://ieeexplore.ieee.org/document/6213236/) today in my mailbox. It's an IEEE paper that is perhaps an answer to the question:

# Is ROS Good for Robotics?

This just threw a whole new perspective on ROS and its effect on the industry. **I can feel a tinge of regret having read the paper.   :(**

### **Update: 2019**

No, no....ROS isn't going anywhere. 😌 Phew! [ROS2](https://index.ros.org/doc/ros2/) is here and people are still porting things from ROS1 and updating the documentation. It'll take time for things to fall in place, development is going on in full swing and it will soon happen!
