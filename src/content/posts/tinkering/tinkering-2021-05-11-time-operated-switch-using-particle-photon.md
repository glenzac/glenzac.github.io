---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: creative internet computer display
  image: "@assets/wp-content/uploads/2020/06/pexels-photo-2004161.jpeg"
date: "2021-05-11T16:02:40+00:00"

tags:
  - automation
  - particle-photon

title: Time operated switch using Particle Photon
---
A while back I'd written a script that was used to [charge dongles](/2020/12/07/auto-charging-for-wireless-dongles/) at fixed intervals of time. The Airtel dongle that it was used with, developed a snag and it would turn off in 10 mins once the supply is cut. So, it's always plugged-in and I've added a thick metal heat sink to keep it cool.

The spare [Photon](https://store.particle.io/products/photon) had to go somewhere. 😂 I ended up writing some code for the outdoor lights to turn on everyday at night. This is a significant improvement over the earlier version of the code I'd written in [this](/2020/12/07/auto-charging-for-wireless-dongles/) post.

I've written some new Particle cloud functions to change the timing using their app. The device also no longer checks the time every 15 mins, it instead checks the current time and runs a software timer that runs out only when it's turn-on time. Software timers use an unsigned integer and is specified in milliseconds. Even after factoring in all this, a software timer can easily run for more than a day without overflowing. I also added a CR2032 coin cell to keep the backup registers and the RTC running even when the power goes down. Thus the Photon is right now an always on device. I hope the coin cell lasts at least a couple of years.

```
SYSTEM_MODE(SEMI_AUTOMATIC); // To bypass the cloud-dependance
SYSTEM_THREAD(ENABLED);
STARTUP(WiFi.selectAntenna(ANT_EXTERNAL)); // selects the u.FL antenna

int lm35_pin = A1;	// LM35 output pin
int adc_value; // ADC reading
double temp_val; // temperature value

int relay_ctl = D1; // relay control pin

int time_hour; // variable to store the current hour value
int time_minute; // variable to store the current minute value
int current_time; // variable to store current (hour)*60+(min)
int mode_select = 1; // 0 => Manual and 1=> Auto
int start_hour; // Auto start hour: 0-24
int start_minute; // Auto start minute: 0-59
int stop_hour; // Auto stop hour: 0-24
int stop_minute; // Auto stop minute: 0-59
int changeMode(String mode);
int startHour(String start_hour);
int startMinute(String start_minute);
int stopHour(String stop_hour);
int stopMinute(String stop_minute);
int state = 0; // state of the relay 0=> OFF and 1=> ON

String last_checked_time; // variable to store last checked time

int address_mode = 0; //EEPROM address to store state of mode
int address_state = 20;//EEPROM address to store state of relay
int address_start_hour = 40; //EEPROM address to store start hour
int address_start_minute = 60; //EEPROM address to store start minute
int address_stop_hour = 80; //EEPROM address to store stop hour
int address_stop_minute = 100; //EEPROM address to store stop minute
int address_start_time = 120; //EEPROM address to store the start: (hour)*60+(min)
int address_stop_time = 140; //EEPROM address to store the stop: (hour)*60+(min)

int eeprom_mode_val;    // Temporary variable to store current value of EEPROM mode
int eeprom_state_val;   // Temporary variable to store current value of EEPROM state
int eeprom_start_hour;  // Temporary variable to store current value of EEPROM start_hour
int eeprom_start_minute;// Temporary variable to store current value of EEPROM start_minute
int eeprom_stop_hour;   // Temporary variable to store current value of EEPROM stop_hour
int eeprom_stop_minute; // Temporary variable to store current value of EEPROM stop_minute
int eeprom_start_time;  // Temporary variable to store current value of EEPROM start_time
int eeprom_stop_time;   // Temporary variable to store current value of EEPROM stop_time

int count_time = 900000; // Duration of 15mins as default

Timer timer_main(count_time,check_time,false); // Starts main timer (initially checks time every 15mins)

void setup()
{
  Time.zone(5.5); // set timezone to +5.5 (IST)
  pinMode(lm35_pin,INPUT); // set LM35 pin as input
  pinMode(relay_ctl,OUTPUT); // set relay pin as output

  Particle.function("Mode", changeMode); // cloud function to change the mode manually
  Particle.function("Start hour", startHour); // cloud function to change the auto start hour
  Particle.function("Start minute", startMinute); // cloud function to change the auto start minute
  Particle.function("Stop hour", stopHour); // cloud function to change the auto stop hour
  Particle.function("Stop minute", stopMinute); // cloud function to change the auto stop minute

  Particle.variable("Switch state",state);  // cloud variable to store the state of relay : 0 or 1
  Particle.variable("Mode",mode_select);  // cloud variable to store the mode
  Particle.variable("Temperature", temp_val); // cloud variable to store temperature value
  Particle.variable("Last checked:",last_checked_time);  // cloud variable to store the last checked timestamp

  // Cloud variables to fetch the values in the EEPROM
  Particle.variable("EEPROM mode:",eeprom_mode_val);
  Particle.variable("EEPROM state:",eeprom_state_val);
  Particle.variable("Start hour",eeprom_start_hour);
  Particle.variable("Start minute",eeprom_start_minute);
  Particle.variable("Stop hour",eeprom_stop_hour);
  Particle.variable("Stop minute",eeprom_stop_minute);

  time_hour = Time.hour(); // retrieves the current hour value
  time_minute = Time.minute(); // retrieves the current minute value
  run(); // run the main function
  timer_main.start(); // start the main timer
}

// Function to turn relay on
void on_relay()
{
    state = 1;
    digitalWrite(relay_ctl,state);
    if (Particle.connected() == true)
    {
        Particle.publish("Turned on at:",last_checked_time);
    }
}

// Function to turn relay off
void off_relay()
{
    state = 0;
    digitalWrite(relay_ctl,state);
    if (Particle.connected() == true)
    {
        Particle.publish("Turned off at:",last_checked_time);
    }
}

// function for proper write addressing
void int_into_EEPROM(int address, int number)
{
  EEPROM.write(address, (number >> 24) & 0xFF);
  EEPROM.write(address + 1, (number >> 16) & 0xFF);
  EEPROM.write(address + 2, (number >> 8) & 0xFF);
  EEPROM.write(address + 3, number & 0xFF);
}

// function for proper read addressing
int int_from_EEPROM(int address)
{
  return ((int)EEPROM.read(address) << 24) +
         ((int)EEPROM.read(address + 1) << 16) +
         ((int)EEPROM.read(address + 2) << 8) +
         (int)EEPROM.read(address + 3);
}

// Cloud Function that gets called when mode is changed
int changeMode(String mode)
{
  if(mode == "auto") // automatic mode (1) - auto
  {
    mode_select = 1;
    int_into_EEPROM(address_mode,mode_select);
    run();
    return 1;
  }

  else if (mode == "on") // manual mode(0) - on
  {
    mode_select = 0;
    state = 1;
    int_into_EEPROM(address_mode,mode_select);
    int_into_EEPROM(address_state,state);
    run();
    return 1;
  }

  else if (mode == "off") // manual mode (0) - off
  {
    mode_select = 0;
    state = 0;
    int_into_EEPROM(address_mode,mode_select);
    int_into_EEPROM(address_state,state);
    run();
    return 1;
  }

  else return -1;
}

// Particle cloud function to change the auto start hour
int startHour(String start_hour)
{
    eeprom_start_hour = start_hour.toInt();
    int_into_EEPROM(address_start_hour,eeprom_start_hour);
    return 1;
}

// Particle cloud function to change the auto start minute
int startMinute(String start_minute)
{
    eeprom_start_minute = start_minute.toInt();
    int_into_EEPROM(address_start_minute,eeprom_start_minute);
    eeprom_start_time = (eeprom_start_hour*60)+(eeprom_start_minute);
    int_into_EEPROM(address_start_time,eeprom_start_time);
    return 1;
}

// Particle cloud function to change the auto stop hour
int stopHour(String stop_hour)
{
    eeprom_stop_hour = stop_hour.toInt();
    int_into_EEPROM(address_stop_hour,eeprom_stop_hour);
    return 1;
}

// Particle cloud function to change the auto stop minute
int stopMinute(String stop_minute)
{
    eeprom_stop_minute = stop_minute.toInt();
    int_into_EEPROM(address_stop_minute,eeprom_stop_minute);
    eeprom_stop_time = (eeprom_stop_hour*60)+(eeprom_stop_minute);
    int_into_EEPROM(address_stop_time,eeprom_stop_time);
    return 1;
}

// Main timer call-back function
void check_time()
{
    last_checked_time = Time.timeStr(); // Format: Wed May 21 01:08:47 2014
    time_hour = Time.hour(); // Get current hour
    time_minute = Time.minute(); // Get current minute
    current_time = (time_hour)*60 + (time_minute);
    eeprom_start_time = int_from_EEPROM(address_start_time);// retrieve start time from EEPROM
    eeprom_stop_time = int_from_EEPROM(address_stop_time);// retrieve stop time from EEPROM

    if((current_time < eeprom_start_time) && (current_time > eeprom_stop_time))
    {
        int diff = eeprom_start_time - current_time;
        run();
        timer_main.changePeriod(((diff+1)*60*1000));
    }
    else if(current_time >= eeprom_start_time)
    {
        int diff = (1440 - current_time) + eeprom_stop_time;
        run();
        timer_main.changePeriod(((diff+1)*60*1000));
    }
    else if(current_time <= eeprom_stop_time)
    {
        int diff = eeprom_stop_time - current_time;
        run();
        timer_main.changePeriod(((diff+1)*60*1000));
    }

}

// function that actually switches the relay
void run()
{
    last_checked_time = Time.timeStr(); // Format: Wed May 21 01:08:47 2014
    time_hour = Time.hour(); // Get current hour
    time_minute = Time.minute(); // Get current minute

    adc_value = analogRead(lm35_pin);	// read temperature
    temp_val = (adc_value * 0.80);	// convert adc value to equivalent voltage // 3.3V/4095= 0.80
    temp_val = (temp_val/10);	// LM35 gives output of 10mv/°C

    if (Particle.connected() == true)
    {
        Particle.publish("Temperature:",String(temp_val));
    }

    eeprom_mode_val = int_from_EEPROM(address_mode);// retrieve mode value from EEPROM
    eeprom_state_val = int_from_EEPROM(address_state);// retrieve state value from EEPROM
    eeprom_start_hour = int_from_EEPROM(address_start_hour);// retrieve start hour from EEPROM
    eeprom_start_minute = int_from_EEPROM(address_start_minute);// retrieve start minute from EEPROM
    eeprom_stop_hour = int_from_EEPROM(address_stop_hour);// retrieve stop hour from EEPROM
    eeprom_stop_minute = int_from_EEPROM(address_stop_minute);// retrieve stop minute from EEPROM

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
        if (time_hour > eeprom_start_hour || time_hour < eeprom_stop_hour) // set timings
        {
            on_relay();
        }
        else if (time_hour == eeprom_start_hour)
        {
            if (time_minute >= eeprom_start_minute)
            {
                on_relay();
            }
            else
            {
                off_relay();
            }
        }
        else if (time_hour == eeprom_stop_hour)
        {
            if (time_minute >= eeprom_stop_minute)
            {
                off_relay();
            }
            else
            {
                on_relay();
            }
        }
        else // relay off at all other times
        {
            off_relay();
        }
    }
}

// void loop that only checks for a cloud connection
// This is needed to run particle fucntions to change parameters remotely
void loop()
{
    if (Particle.connected() == false)
    {
        Particle.connect();
    }
}
```
