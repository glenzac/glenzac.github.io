---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: microwave
  image: "@assets/wp-content/uploads/2021/07/microwave.jpg"
date: "2021-07-30T05:06:15+00:00"

tags:
  - diy
  - electronics
  - repairs

title: How to fix SE error on a Samsung Microwave Oven?
---
Our microwave oven a [Samsung MW103H](https://www.samsung.com/nz/support/model/MW103H/XSA/#link) started turning off randomly with an `SE` error. Sometimes, it totally even refused to start and would lock up all the buttons, rendering it useless.😑

This [page](https://www.samsung.com/us/support/troubleshooting/TSG01110365/) on Samsung lists all the error codes and what it means. `SE` is short for _Key Short Error_. This means that the some of the keys are stuck and as a safety measure the microwave has switched itself off.

I couldn't find a service guide for the microwave so I had no choice but to open it up and check. The primary reason buttons stop working could be that the flat film cable which connects the keypad to the board might have corroded. So I opened up everything carefully and took extra care not to go anywhere near those high voltage capacitors which would probably be fully charged and thus fatal. 😅

![](@assets/wp-content/uploads/2021/07/microwave.jpg)

I disconnected the earth line that was also connected to the body and took out the flexible flat cable (FFC). The metal connections at the end looked oxidized. Rubbing it with an eraser didn't bring back the shine. Next, I used IPA on the film and the lustre was almost back. I reinserted it back into the connector and closed the enclosure and powered it up.

The display lit up, but none of the buttons worked nor was I getting any error. When I rechecked the FFC this is what I found:

![](@assets/wp-content/uploads/2021/07/ffc_2.jpg)

The connection was broken at the point where the FFC was locked into the connector. It could have been a result of me taking it out too or it was at the brink of corrosion and I just accelerated it.

![](@assets/wp-content/uploads/2021/07/ffc_1.jpg)

I knew bridging that connection would be enough to bring it back to life. The bigger question was HOW?

I asked this on the [r/AskElectronics](https://www.reddit.com/r/AskElectronics/) subreddit and people generously poured in their views and all of it is good and long enough for another post. There were two suggestions that received the most upvotes.

1. Use conductive paint to bridge the gap
1. Cut the FFC exactly at the point where it breaks

Now both these suggestions are really good, but they have their own demerits too. Since I could still go with the second suggestion even if the first one fails, I decided to first give the conductive paint a shot.

Amazon only had a carbon based conductive paint that came as a pen. Carbon is not very conductive and it's resistance will probably be several hundred ohms. Also, the black substance only adheres to porous materials like paper, wasn't sure if it would even stick onto a plastic film. None of the other electronic component dealers had silver conductive paint and most only had the carbon based paint. [RS components](https://in.rsdelivers.com/product/rs-pro//rs-pro-conductive-paint-5-g/1239911) had silver paint but the cost came to more than Rs 3000 (without taxes) just for 5g. Finally, I found a US company - Chip Quik who recently started manufacturing [silver conductive paint](http://www.chipquik.com/store/product_info.php?products_id=480001) and a 5g syringe was available for about $16 which was reasonable compared to RS Components. Thankfully, Mouser had this product listed and I use a third party distributor to import it. I've ordered it and it the total came to about Rs 1700 thanks to the import duties, tax and shipping. 😅

More updates once I receive it! 😁

![](@assets/wp-content/uploads/2021/08/chip_quik_silver_paste.jpg)

I got the product in about 12 days.

Thanks to my not so steady hands, building the connections took long and it was messy. There was too little room for error and wiping any excess paste would only make it spread to the adjacent pins. In the end it turned out like this:

![](@assets/wp-content/uploads/2021/08/ffc_repaired.jpg)

I checked the connections visibly under the light and also tested for shorts using a multimeter. Turns out it was enough. The microwave oven started working fine! Yay! 😁
