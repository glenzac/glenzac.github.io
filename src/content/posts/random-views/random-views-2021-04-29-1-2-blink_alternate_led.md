---
author: glenzac
categories:
  - "random-views"
cover:
  alt: MSP430
  image: "@assets/wp-content/uploads/2020/07/msp430.jpg"
date: "2021-04-29T08:30:22+00:00"

tags:
  - embedded
  - "msp430-series"
  - ti

title: 1.2 Blink_Alternate_LED
---
This just involves a slight modification of example 1.1. Here instead of toggling the LEDs we first set LED1 as HIGH and LED2 as LOW. Then after a delay, we set the first LED as LOW and the second LED as HIGH. This is again followed by a delay. Finally, we have 2 LEDs that blink alternately.

```
/*
 * Created on Sat Jul 11 2020
 *
 * Created by: Glen Zachariah
 * For more: https://glenzac.wordpress.com
 * License: CC0 1.0 Universal
 *
 * For MSP430F5529LP
 * --------Hardware------
---
 * LED1 -> P1.0 (Red)
 * LED2 -> P4.7 (Green)
 * Button S1 -> P2.1
 * Button S2 -> P1.1
 * ----------------------
---
 */

#include <msp430.h>

/**
 * main.c
 */
int main(void)
{
    WDTCTL = WDTPW | WDTHOLD;   // stop watchdog timer
    P1DIR |= BIT0; // configure P1.0 as output
    P4DIR |= BIT7; // configure P4.7 as output

    volatile unsigned int i;

    while(1)
    {
        P1OUT |= BIT0; //set P1.0 as HIGH
        P4OUT &= ~BIT7; //set P4.7 as LOW
        for(i=25000; i>0; i--);     // delay
        P1OUT &= ~BIT0; //set P1.0 as LOW
        P4OUT |= BIT7; //set P4.7 as HIGH
        for(i=25000; i>0; i--);     // delay

    }

    return 0;
}

```
