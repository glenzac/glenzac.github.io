---
author: glenzac
categories:
  - "random-views"
cover:
  alt: MSP430
  image: "@assets/wp-content/uploads/2020/07/msp430.jpg"
date: "2020-07-15T06:34:10+00:00"

tags:
  - embedded
  - msp430
  - ti

title: 1.4 Button Interrupts
---
All the GPIO ports on the MSP430F5529 have interrupt capability. The concept of interrupts is very widely covered in online guides and videos. Here's a random [reference](https://en.wikibooks.org/wiki/Embedded_Systems/Interrupts).

Now that I can safely assume that you understand interrupts, we need to go back and look at the register table we saw in lesson1( [1.0 Blink](/2020/07/11/1-0-blink/)). The following image is what we saw there:

![](@assets/wp-content/uploads/2020/07/373-topzr5w.png)

We already covered the registers shaded in purple in the previous lessons. Now, we shall look at the ones shaded in red, at the bottom. The table above is quite self-explanatory. We need to enable the interrupts by setting the PxIE register. We also need to choose if we want the interrupt to trigger on a rising or a falling edge. So once we have configured both these registers we also need to enable interrupts globally on the device. It is more like a gateway for all interrupts. If it is turned off then, none of the interrupts can reach through to the system. Global interrupts can be enabled by using the following line of code:   
 \_\_ `bis_SR_register(GIE);` The `bis ` keyword is short for 'bit set', this enables the appropriate register. All these registers are defined in the `msp430.h` header file that you call in every program. To give you an idea, here's the definition snippet from the device specific header file:

![](@assets/wp-content/uploads/2020/07/403-blys4gi.png)

This sets the right bits in the status registers to enable global interrupts. The moment we push down the button, the corresponding pin goes from HIGH to LOW and there is a falling edge, if we have configured the PxIES registers to trigger on the falling edge, an interrupt is generated and this sets the PxIFG or the interrupt flag. When an interrupt occurs, the controller stops what it's executing, saves the context (all the current state of some registers) and jumps to the respective ISR. The GPIO pins have an interrupt vector associated with it that can be used to find out the right pin that caused the interrupt.

The interrupt vector in this case is called the `PORT1_VECTOR`. This is the vector that all the pins in Port 1 uses. `pragma vector=PORT1_VECTOR` tells the compiler where to look for when an interrupt on **PORT1** occurs and it executes the corresponding ISR.

`pragma vector=PORT1_VECTOR`

`__interrupt void myISR(void)`

The above snippet defines that if an interrupt occurs on **PORT1** the ISR called `myISR ` has to be executed. By default, ISRs can take no input arguments nor should it return any.

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

int main(void) {
    WDTCTL = WDTPW | WDTHOLD;   // Stop watchdog timer

    // ------------- Configure on-board LEDs and Buttons --------------- //

    P1DIR |= BIT0;              // Set P1.0 as OUTPUT
    P4DIR |= BIT7;              // Set P4.7 as OUTPUT
    P2DIR &= ~BIT1;             // Set P2.1 as INPUT
    P2REN |= BIT1;              // Enable P2.1 pull up/down configuration
    P2OUT |= BIT1;              // Set P2.1 as INPUT
    P1DIR &= ~BIT1;             // Set P1.1 as INPUT
    P1REN |= BIT1;              // Enable P1.1 pull up/down configuration
    P1OUT |= BIT1;              // Enable pull up on P1.1

    // ----------------------------------------------------------------- //

    P1IES &= ~BIT1; // Set low to high interrupt on P1.1
    P1IE |= BIT1; // Enable P1.1 as interrupt
    __bis_SR_register(GIE); //Set GIE bit in Status Register to enable Global Interrupts

    return 0;
}

#pragma vector=PORT1_VECTOR
__interrupt void myISR(void)
{
    //_even_in_range: tells compiler to only worry about even interrupts up to 0x10
    // useful in creating optimized ISRs
    switch(__even_in_range( P1IV, 0x10 ))
    {
        case 0x00: break;   // None
        case 0x02: break;   // Interrupt on Pin 0
        case 0x04: P4OUT ^= BIT7;   // Interrupt on Pin 1
                   break;
        case 0x06: break;   // Interrupt on  Pin 2
        case 0x08: break;   // Interrupt on Pin 3
        case 0x0A: break;   // Interrupt on Pin 4
        case 0x0C: break;   // Interrupt on Pin 5
        case 0x0E: break;   // Interrupt on Pin 6
        case 0x10: break;   // Interrupt on Pin 7
        //_never_executed(): tells compiler that default case will never occur
        // useful in creating optimized ISRs
        default: _never_executed();
    }
}

```
