---
author: glenzac
categories:
  - "random-views"
cover:
  alt: MSP430
  image: "@assets/wp-content/uploads/2020/07/msp430.jpg"
date: "2021-04-29T08:30:19+00:00"

tags:
  - embedded
  - "msp430-series"
  - ti

title: 1.1 Dual_LED_Blink
---
This example is pretty self explanatory. The MSP430F5529 has 2 User LED's (Green and Red). This example simply toggles both the LED's together. Thus they turn on and off at the same time.

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
	WDTCTL = WDTPW | WDTHOLD;	// stop watchdog timer
	P1DIR |= BIT0; // configure P1.0 as output
	P4DIR |= BIT7; // configure P4.7 as output

	volatile unsigned int i;

	while(1)
	{
	    P1OUT ^= BIT0; // toggle P1.0
	    P4OUT ^= BIT7; // toggle P4.7
	    for(i=50000; i>0; i--);     // delay
	}

	return 0;
}

```
