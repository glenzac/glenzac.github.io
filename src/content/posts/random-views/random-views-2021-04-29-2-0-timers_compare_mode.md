---
author: glenzac
categories:
  - "random-views"
cover:
  alt: MSP430
  image: "@assets/wp-content/uploads/2020/07/msp430.jpg"
date: "2021-04-29T08:30:36+00:00"

tags:
  - embedded
  - msp430
  - ti

title: 2.0 Timers_Compare_Mode
---
Timers are specific hardware that is used to well run timers! The **MSP430F5529** has several timers as shown in the figure below:

![](@assets/images/2021/ZXWm9ar.jpeg)

Also do read the text at the lower half of the above image. We will learn about Capture/Compare Registers soon. So there are three types of Timer\_A in the **MSP430F5529**.

## Timer Nomenclature

![](@assets/images/2021/H5gvL6B.jpg)

The convention followed for naming the timers are shown on the left. You can use the 'short name' as the prefix while writing values to the specific registers. This applies only to the Timer\_A block as the other blocks only have one timer instance.

In this post we'll cover everything that is needed to understand timers with Timer A as reference. Timer B too works in a similar fashion but offers more options for customization.

## How does it work?

The following block diagram is directly taken from the user's guide and **shows only one half of the Timer Block**(Compare mode only). The other part will be discussed in the next post.

![](@assets/images/2021/H2FwvrT.jpeg)

If you covered the [last lesson](/2020/07/14/understanding-the-clocks/) the inputs to this Timer Block will be obvious. First thing to do then is select the required clock signal using the **TASSEL** MUX this is followed by two stages of dividers (note that Timers have additional dividers). The input signal is divided based on the bits set in the **ID** and **IDEX** register. **TAxR** is the 16-bit timer/counter register that increments or decrements (based on the mode) with every rising/falling edge of the input signal. It can have values from `0x0000 ` to `0xFFFF`.

**TAxR** may be cleared by setting the **TACLR** bit. The Timer has the following modes of operation:

![](@assets/images/2021/ZkeM2LR.jpg)

In the continuous mode ( **MC** = 10) the timer runs repeatedly and every time it reaches 0xFFFF (or 0FFFFh) it overflows and goes back to 0x0000 this sets an Interrupt flag **TAIFG**. We can use this ISR to run some quick tasks periodically. Now, what if we don't want to wait till 0xFFFF for it overflow and generate an interrupt to do our tasks? What if the time it takes to overflow is too long?

In this case we can use the **TAxCCR0** or the Timer A Capture/Compare register 0.

![](@assets/images/2021/3BqivOE.jpg)

In the Up mode ( **MC** = 01) the timer counts up to the value present in **TAxCCR0** then it resets back to zero and sets the **CCIFG** interrupt flag. **Note:** The **TAxCCR0 CCIFG** interrupt flag is set when the timer counts to the **TAxCCR0** value.The **TAIFG** interrupt flag is set when the timer counts from **TAxCCR0** to zero.

![](@assets/images/2021/MxtaF2Z.jpg)

In the Up/Down mode (MC = 11) which can be visualized as follows:

![](@assets/images/2021/DhuQREp.jpeg)

In up/down mode,the **TAxCCR0 CCIFG** interrupt flag and the **TAIFG** interrupt flag are set only once during a period, separated by one-half the timer period.The **TAxCCR0 CCIFG** interrupt flag is set when the timer counts from `TAxCCR0-1` to `TAxCCR0`, and **TAIFG** is set when the timer completes counting down from `0001h ` to `0000h`.

One final note about the MSP430 timers: they do not generate interrupts (or other actions) when  
you write to the counter register directly. For example, writing “0” to the counter won’t generate the **TAIFG** interrupt. The Timer\_A0 has 5 such **CCRn** registers that can be used to create the required time intervals.

## Timer A Registers

Now let's look at the appropriate registers and bits we need to set to start our timer:

![](@assets/images/2021/DhMmJI5.jpeg)

All of the registers have been covered in detail above. If you were observant enough you might have noticed that you don't see IDEX in any of the registers. In fact it comes in another register called the **TAxEX0**(Timer\_Ax Expansion 0 Register).

![](@assets/images/2021/conKkEm.jpeg)

The odd divider values allow for a wide range of timer frequencies to be set. This makes the Timers on the MSP430 very flexible for different use cases.

Additionally there is one more big and important register in the Timer\_A block which is the Timer\_A Capture/Compare Control register. This will be dealt with in detail, in the next lesson. For this lesson we need to understand that for Timer\_A interrupts to work we need to set the **CCIE** (Capture/Compare interrupt enable) bit in the **TAxCCTLn** register.

## Timer A Interrupt Vector

Two interrupt vectors are associated with the 16-bit Timer\_A module:  
• **TAxCCR0** interrupt vector for **TAxCCR0 CCIFG**  
• **TAxIV** interrupt vector for all other **CCIFG** flags and **TAIFG**

The **TAxCCR0 CCIFG** flag has the highest Timer\_A interrupt priority and has a dedicated interrupt vector. The **TAxCCR0 CCIFG** flag is automatically reset when the **TAxCCR0** interrupt request is serviced.

For all other **TAxCCRn** registers flags and for the **TAIFG** flag we have a separate **TAxIV** interrupt vector as shown below:

![](@assets/images/2021/moPoAmK.jpg)

## Coding time!

Let's learn to configure the timer.

```
  TA0CCTL0 = CCIE;                          // Enable CCR0 interrupt
```

We can simply use the = sign to set bits here instead of bitwise \|= operator (both are correct). We enable the interrupts first. Thus we'll soon need to write its ISR too.

```
 TA0CCR0 = 50000;                          // Set compare value of 50,000 in CCR0
```

Next, we need to set a value in CCR0 up to which we want our timer to count. On reaching the required count the timer gets back to 0x0000 and generates an interrupt.

```
  TA0CTL = TASSEL_2 + MC_1 + TACLR;       // Source = SMCLK, In Upmode, clear counter (TAR)
```

Using `TASSEL_2 ` implies it is set to `10 `(means 2 in binary) which selects the SMCLK clock source see the diagram [above](#working) to understand it better. Similarly, mode is set as `01`, we want the timer to count up to 50,000 (the max count is 65535) and then get back to 0 and fire an interrupt. We'll then be using the ISR to toggle our LED.

Also, don't forget to enable Global Interrupts as we had seen in the [1.4 Button Interrupts](/2020/07/11/1-4-button-interrupts/) lesson.
