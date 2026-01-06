---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: Goal tracker v2
  image: "@assets/wp-content/uploads/2018/08/goal-tracker-v2.png"
date: "2018-08-23T19:02:08+00:00"

summary: |-
  ![](https://img.shields.io/badge/Project-Complete-blue.svg)

  Link to the project : [https://www.instructables.com/id/Goal-Habit-Medication-Tracker-Using-ATTINY85/](https://www.instructables.com/id/Goal-Habit-Medication-Tracker-Using-ATTINY85/)
tags:
  - attiny85
  - medicine
  - tracker

title: 'Simple Medication Tracking: using ATTINY85'
---
![](https://img.shields.io/badge/Project-Complete-blue.svg)

Link to the project : [https://www.instructables.com/id/Goal-Habit-Medication-Tracker-Using-ATTINY85/](https://www.instructables.com/id/Goal-Habit-Medication-Tracker-Using-ATTINY85/)

Will post updates and trials here.

People forget if they had their medication or not and this often leads to an overdose or skipping it. Both are dangerous in most cases.

This project aims to solve that problem. It will be a tiny device with 7 LED's that signify the 7 days of the week.

The LED's turn on one after the other when an increment button is pressed.

that light up sequentially as a potentiometer is turned. The user has to turn the pot and light up one LED daily.

Quite sadly there is hardly any clear documentation on how to burn assembly language code into ATTINY85. Many sites point to avrdude.

I've also downloaded Atmel Studio 7

Three people code assembly code:

```
/*
 *	Shift register demo #1
 *
 *	ATTiny13A Running @9.6MHz
 *	ADC running @150kHz
 *
 *	PIN ASSIGNMENT:
 *		PB0 - Shift Register Clock
 *		PB1 - Shift Register Serial Data
 *		PB2 - Shift Register Latch(Store)
 *		PB3 - ADC3 (Potentiometer input)
 *		PB4 - [NOT USED]
 *		PB5 - RESET
 */
.include "tn13Adef.inc"
.def	A = R16	; g.p. variable and/or function argument
.def	B = R17	; Used in SEND_BYTE and ADC_START as temporary storage
.def	LED1 = R18	; stores current LED1 output
.def	LED2 = R19	; stores current LED2 output
.def	LED3 = R20	; stores current LED3 output
.def	BUT1 = R22	; stores button counter1
.def	BUT2 = R23	; stores button counter2
.def	BUT3 = R24	; stores button counter3

add button code here

.def	BCT = R21	; Bit counter for SEND_BYTE
.equ	SRCK = 0	; PB0 = Clock
.equ	SRDA = 1	; PB1 = Serial Data
.equ	SRLC = 2	; PB2 = Latch

/*	INTERRUPT VECTORS	*/
.org	0x0000
rjmp	RESET		; Reset interrupt
.org	0x0003
rjmp	TC0_OV		; Timer1 interrupt

/*
 *	START!!!
 */
RESET:
        /*	SETUP STACK	*/
	ldi	A, low(RAMEND)	; Set stack pointer
	out	SPL, A
	/*	SETUP PINS	*/
	ldi	A,0b0000_0111	; Set output pins PB0..PB2
	out	DDRB,A
	/*	SETUP TIMER1	*/
	ldi	A,0b0000_0101   ; Set Timer Prescaler (1024)
	out	TCCR0B,A	; This will cause Timer Interrupt every ~27ms
	ldi	A,0b00000010	; Enable Timer0 Overflow Interrupt
	out	TIMSK0,A
	/*	SETUP ADC3	*/
	ldi	A,0
	out	ADCSRB,A	; Disable autotrigger(Free running)
	ldi	A,0b00001000	; Disable Digital Input on PB3(ADC3)
	out	DIDR0,A
	ldi	A,0b00000011
	out	ADMUX,A		; Source:ADC3, Align:RIGHT, Reference:VCC.
	ldi	A,0b10000110
	out	ADCSRA,A	; Enable ADC with prescale 1/64
	/*	RESET REGISTERS	*/
	ldi	A,0x00		; clear A
	ldi	LED1,0xFF	; Set all LED's to OFF(1-off, 0-on)
	ldi	LED2,0xFF	; Set all LED's to OFF(1-off, 0-on)
	ldi	LED3,0xFF	; Set all LED's to OFF(1-off, 0-on)
	rcall	SEND_BYTE1	; Clear display1
	rcall	SEND_BYTE2	; Clear display2
	rcall	SEND_BYTE3	; Clear display3
	sei			; Enable interrupts

/*	Main loop	*/
MAIN:
	rjmp	MAIN

/*
 *	Sends 8-bit data from LED register to Shift Register
 */
SEND_BYTE1:
	ldi	BCT,0b1000_0000	; Set Bit counter
next_bit:
	mov	B,LED1		; Move data byte to temp
	and	B,BCT		; Check bit
	breq	zero		; Set Data to 0
	sbi	PortB,SRDA	; Set Data to 1
	rjmp	shift		; shift
zero:
	cbi	PortB,SRDA
shift:
	sbi	PortB,SRCK	; CLK up
	nop
	cbi	PortB,SRCK	; CLK down
	clc			; Clear Carry flag
	ror	BCT		; Shift bit counter
	brne	next_bit	; Next iteration
	sbi	PortB,SRLC	; When done, Latch
	nop
	cbi	PortB,SRLC
	ret			; Done

SEND_BYTE2:
	ldi	BCT,0b1000_0000	; Set Bit counter
next_bit:
	mov	B,LED2		; Move data byte to temp
	and	B,BCT		; Check bit
	breq	zero		; Set Data to 0
	sbi	PortB,SRDA	; Set Data to 1
	rjmp	shift		; shift
zero:
	cbi	PortB,SRDA
shift:
	sbi	PortB,SRCK	; CLK up
	nop
	cbi	PortB,SRCK	; CLK down
	clc			; Clear Carry flag
	ror	BCT		; Shift bit counter
	brne	next_bit	; Next iteration
	sbi	PortB,SRLC	; When done, Latch
	nop
	cbi	PortB,SRLC
	ret			; Done

SEND_BYTE3:
	ldi	BCT,0b1000_0000	; Set Bit counter
next_bit:
	mov	B,LED3		; Move data byte to temp
	and	B,BCT		; Check bit
	breq	zero		; Set Data to 0
	sbi	PortB,SRDA	; Set Data to 1
	rjmp	shift		; shift
zero:
	cbi	PortB,SRDA
shift:
	sbi	PortB,SRCK	; CLK up
	nop
	cbi	PortB,SRCK	; CLK down
	clc			; Clear Carry flag
	ror	BCT		; Shift bit counter
	brne	next_bit	; Next iteration
	sbi	PortB,SRLC	; When done, Latch
	nop
	cbi	PortB,SRLC
	ret			; Done

/*	Start ADC conversion. Saves result to A	*/
ADC_START:
        sbi	ADCSRA,ADSC	; Start ADC conversion
adc_wait:
	sbic	ADCSRA,ADSC	; Check conversion status
	rjmp	adc_wait	; Skip jump if completed
	in	A,ADCL		; Get low bits
	in	B,ADCH		; Get high bits
	lsr     B		; Shift 2 bits to the right
	ror A			; through Carry
	lsr B
	ror A
	ret

/*	Timer 0 overflow interrupt	*/
TC0_OV:
	rcall	ADC_START	; start ADC0 Conversion
	/* Compare Input, Set output */
	cpi	A,0xC8		; A>=200?
	brlo	gt_80

	ldi	LED1,0b11100000
	rjmp	sr_write1

gt_80:				; A>=80?
	cpi	A,0x50
	brlo	lt_40
	ldi	LED2,0b11111100
	rjmp	sr_write2

lt_40:				; A<40
	ldi	LED3,0b11111111
	rjmp	sr_write3

sr_write1:
	rcall	SEND_BYTE1	; Send byte to shift reg.
	reti			; return

sr_write2:
	rcall	SEND_BYTE2	; Send byte to shift reg.
	reti			; return

sr_write3:
	rcall	SEND_BYTE3	; Send byte to shift reg.
	reti			; return
```
