---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: pVgYxoC
  image: "@assets/wp-content/uploads/2020/06/pvgyxoc.jpg"
date: "2020-12-07T16:58:24+00:00"

tags:
  - automation
  - charger
  - particle-photon
  - wifi

title: Auto-charging for Wireless dongles
---
I don't live in a city and the wired broadband connections on the outskirts are very unreliable and takes days to fix if something goes wrong. So we totally rely on Wireless dongles from Jio and Airtel. They are built to be used as portable devices and needs to be charged every six hours or so.

Jio dongles work even without the batteries and I just use it directly. The batteries are put in only when traveling. Some dongles like those from Airtel don't turn on without a battery and so it has to be constantly charged every few hours. You can't just leave it plugged in forever. Kills the battery! 💀

I had a spare [Particle Photon](https://store.particle.io/products/photon) lying around and so decided to make a device to do this boring job of turning on the WiFi dongle at specific intervals of the day.

The task at hand was simple, but I ended up adding a lot of bells and whistles 🤦‍♂️and coding it to meet different scenarios.

In the end the device had:

- Three modes of operation : Automatic, Manual, Timer
  - **automatic**\--turn-the-device-on-and-off-automatically-at-specific-times-during-the-day.-its-not-a-delay-or-timer-based-control-but-it-fetches-the-actual-time-from-the-particle-cloud-server-and-does-the-switching-accordingly.
  - **manual**\--in-this-mode-you-can-toggle-the-charging-state-manually-using-the-particle-photon-app
  - **timer**\--use-this-when-the-device-needs-to-be-turned-on-and-charged-for-a-specific-duration-of-time.
- remember its state after every shut-down (using EEPROM)
- record temperatures of the device (using an LM35)
- Checks for the state changes every 15mins

**Alternate use cases:** To switch on and off anything and everything around the home without moving a finger😛.

## The code:

Feel free to modify and re-use as needed!

```
int lm35_pin = A1;	// LM35 output pin
int relay_ctl = D1; // relay control pin
int adc_value; // ADC reading
double temp_val; // temperature value
int time_hour; // variable to store the current hour value
int mode_select = 1; // 0 => Manual and 1=> Auto and 2=> Timer mode
int changeMode(String mode);
int state = 0; // state of the relay 0=> OFF and 1=> ON
int shift = 0; // shift type : 0 => morning and 1 => evening
int timer_duration; //Duration of the timer in Timer mode
String last_checked_time; // variable to store last checked time
int address_shift = 0; //EEPROM address to store state of shift
int address_mode = 20; //EEPROM address to store state of mode
int address_state = 40;//EEPROM address to store state of relay
int eeprom_shift_val; // Temporary variable to store current value of EEPROM shift
int eeprom_mode_val;  // Temporary variable to store current value of EEPROM mode
int eeprom_state_val;  // Temporary variable to store current value of EEPROM state
Timer mode_timer(3600000*timer_duration,timer_mode,true); // A timer for timer mode that runs only once
Timer timer_main(900000,check_time,false); // Starts main timer (checks time every 15mins)

void setup()
{
  Time.zone(5.5); // set timezone to +5.5 (IST)
  pinMode(lm35_pin,INPUT); // set LM35 pin as input
  pinMode(relay_ctl,OUTPUT); // set relay pin as output
  Particle.function("Shift", changeShift);
  Particle.function("Mode", changeMode); // Particle cloud function to change the mode manually
  Particle.function("Timer Duration:", setTimer); // Particle cloud function to give in interval for Timer mode
  time_hour = Time.hour(); // retrieves the current hour value
  check_time(); // run the check_time function
  timer_main.start(); // start the main timer
  Particle.variable("Hotspot state",state);  // Particle cloud variable to store the state of relay : 0 or 1
  Particle.variable("Shift",shift);  // Particle cloud variable to store the state of relay : 0 or 1
  Particle.variable("Mode",mode_select);  // Particle cloud variable to store the mode
  Particle.variable("Temperature", temp_val); // Particle cloud variable to store temperature value
  Particle.variable("Last checked:",last_checked_time);  // Particle cloud variable to store the last checked timestamp
  Particle.variable("Current Timer Duration:",timer_duration); // Particle variable to store the current time interval for Timer mode
  Particle.variable("EEPROM shift:",eeprom_shift_val);
  Particle.variable("EEPROM mode:",eeprom_mode_val);
  Particle.variable("EEPROM state:",eeprom_state_val);
}

// Function to turn relay on
void on_relay()
{
    state = 1;
    digitalWrite(relay_ctl,state);
}

// Function to turn relay off
void off_relay()
{
    state = 0;
    digitalWrite(relay_ctl,state);
}

void int_into_EEPROM(int address, int number)
{
  EEPROM.write(address, (number >> 24) & 0xFF);
  EEPROM.write(address + 1, (number >> 16) & 0xFF);
  EEPROM.write(address + 2, (number >> 8) & 0xFF);
  EEPROM.write(address + 3, number & 0xFF);
}

int int_from_EEPROM(int address)
{
  return ((int)EEPROM.read(address) << 24) +
         ((int)EEPROM.read(address + 1) << 16) +
         ((int)EEPROM.read(address + 2) << 8) +
         (int)EEPROM.read(address + 3);
}

// Cloud Function that gets called when shift change is updated
int changeShift(String shift_string)
{
    if(shift_string == "m") // morning shift
    {
        shift = 0;
        int_into_EEPROM(address_shift, shift);
        check_time();
        return 1;
    }
    else if(shift_string == "e") //evening shift
    {
        shift = 1;
        int_into_EEPROM(address_shift, shift);
        check_time();
        return 1;
    }
    else return -1;
}

// Cloud Function that gets called when mode is changed
int changeMode(String mode)
{
  if(mode == "auto") // automatic mode (1)
  {
    mode_select = 1;
    int_into_EEPROM(address_mode,mode_select);
    check_time();
    return 1;
  }

  else if (mode == "on") // manual mode(0) - on
  {
    mode_select = 0;
    state = 1;
    int_into_EEPROM(address_mode,mode_select);
    int_into_EEPROM(address_state,state);
    check_time();
    return 1;
  }

  else if (mode == "off") // manual mode (0) - off
  {
    mode_select = 0;
    state = 0;
    int_into_EEPROM(address_mode,mode_select);
    int_into_EEPROM(address_state,state);
    check_time();
    return 1;
  }

  else if (mode == "timer") // timer mode(2)
  {
    mode_select = 2;
    int_into_EEPROM(address_mode,mode_select);
    return 1;
  }
  else return -1;
}

// Cloud Function that gets called when timer duration is updated
int setTimer(String timer_string)
{
    if(mode_select == 2) // first ensure timer mode is active
    {
        timer_duration = timer_string.toInt(); // convert input string to integer duration
        mode_timer.changePeriod(3600000*timer_duration); // changing the time period of a dormant timer also starts it
        on_relay();
        return 1;
    }
    else return -1;
}

// Function that is run when the timer mode duration expires
void timer_mode()
{
    mode_select = 1; // switch back to auto mode
    int_into_EEPROM(address_mode,mode_select); // update value in EEPROM
    check_time();
}

// Function that is run every 15mins by the software timer to check for changes
void check_time()
{
    last_checked_time = Time.timeStr(); // Format: Wed May 21 01:08:47 2014
    time_hour = Time.hour(); // Get current hour
    adc_value = analogRead(lm35_pin);	// read temperature
    temp_val = (adc_value * 0.80);	// convert adc value to equivalent voltage // 3.3V/4095= 0.80
    temp_val = (temp_val/10);	// LM35 gives output of 10mv/°C
    eeprom_shift_val = int_from_EEPROM(address_shift);// retrieve stored shift value from EEPROM
    eeprom_mode_val = int_from_EEPROM(address_mode);// retrieve stored mode value from EEPROM
    eeprom_state_val = int_from_EEPROM(address_state);// retrieve stored state value from EEPROM

    if (eeprom_shift_val == 0) // morning shift
    {
        if (eeprom_mode_val == 0) // manual mode
        {
            if (eeprom_state_val == 1) // if state was previously on
            {
                on_relay();
            }
            else if (eeprom_state_val == 0) // if state was previously off
            {
                off_relay();
            }
        }

        else if (eeprom_mode_val == 1) // auto mode
        {
            if ((time_hour == 6)||(time_hour == 7)||(time_hour == 8)||(time_hour == 11)||(time_hour == 12)||(time_hour == 13)||(time_hour == 16)||(time_hour == 17)||(time_hour == 18)) // set timings
            {
                on_relay();
            }
            else // relay off at all other times
            {
                off_relay();
            }
        }

        else if (eeprom_mode_val == 2) // timer mode
        {
            if (!(mode_timer.isActive())) // If timer_mode timer is not active (usually after a power down event)
            {
                mode_select = 1; // switch back to auto mode
                int_into_EEPROM(address_mode,mode_select); // update value in EEPROM
                check_time();
            }

        }

    }

    else if (eeprom_shift_val == 1) // evening shift
    {
        if (eeprom_mode_val == 0) // manual mode
        {
            if (eeprom_state_val == 1) // if state was previously on
            {
                on_relay();
            }
            else if (eeprom_state_val == 0) // if state was previously off
            {
                off_relay();
            }
        }

        else if (eeprom_mode_val == 1) // auto mode
        {
            if ((time_hour == 13)||(time_hour == 14)||(time_hour == 15)||(time_hour == 18)||(time_hour == 19)||(time_hour == 20)||(time_hour == 21)) // set timings
            {
                on_relay();
            }
            else // relay off at all other times
            {
                off_relay();
            }
        }

        else if (eeprom_mode_val == 2) // timer mode
        {
            if (!(mode_timer.isActive())) // If timer_mode timer is not active (usually after a power down event)
            {
                mode_select = 1; // switch back to auto mode
                int_into_EEPROM(address_mode,mode_select); // update value in EEPROM
                check_time();
            }

        }

    }
}

// Empty void loop since all the action happens withing the functions and timer-calls
void loop()
{

}

```
