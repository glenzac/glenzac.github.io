---
author: glenzac
comments: true
date: 2020-05-26 07:30:58+00:00
layout: post
link: https://glenzac.wordpress.com/2020/05/26/youtube-tv-using-the-raspberry-pi-on-raspbian-with-hdmi-cec/
slug: youtube-tv-using-the-raspberry-pi-on-raspbian-with-hdmi-cec
title: YouTube TV using the Raspberry Pi on Raspberry Pi OS with HDMI-CEC
wordpress_id: 1983
categories:
- Tinkering 🛠️
tags:
- osmc
- raspberrypi
- raspbian
- ssh
- YouTube TV
- youtube-dl
---




<!-- more -->





Note: If you're here just for the installation part, click the link to skip to the " YouTube on Raspberry Pi OS " section







Find all source files [here](https://github.com/glenzac/raspberrypi-tv)







I've been using the raspberry pi for about 4 years and never have I written a single post on it. Mostly because I'm only trying out things that I find on the internet.







So this post is about turning your Rpi into a dedicated media centre or YouTube TV. (I know that there are tons of guides out there on the internet, but I've tried most of them and it just doesn't work without issues )







My Hardware : [Raspberry Pi 3B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)








https://www.raspberrypi.org/homepage-9df4b/static/be658fef8c4d492bb6d85187f678cf89/a0db7/42a30d80d90dcfbde51468383beaa4c5cbefc962_raspberry-pi-3-hero-1-1571x1080.jpg








Pinout : [https://pinout.xyz/#](https://pinout.xyz/#)







## Why? 







I have a SONY Bravia TV that is internet enabled and I have been watching YouTube on it for more than 5 years now. SONY kept pushing updates and updating the YouTube app to ensure compatibility whenever Google decided to make changes. If at all the app stopped working, factory resetting the device helped to fetch the latest updates. But recently, I've begun to see more occurrences of page not found errors. Also when it starts playing I can't access the settings to set the required video resolution.  
I see all these as signs of discontinuing support for old YouTube clients. So I decided to put the Rpi to good use - to play YouTube videos and live streams.







## 💿Top OS choices for media applications







  * OSMC
  * LibreELEC






After reading a lot of forum posts, I decided to go with installing OSMC - it apparently had more features and was more customizable than LibreELEC. It took a while to set everything up and update my library. This was how it looked then: 








https://i.imgur.com/GHRwuy2.jpg?1.jpg








Then I followed an online guide and installed the YouTube addon. I logged into my Google console and got all the API keys and fully signed in and also completed the 2 step device registration. Videos played fine then. Next time I decided to reboot and then when I opened the addon it was asking me to signin again, but the other options like 'My Recommendations' and locations based videos were all visible. Videos only played for 2 seconds and kept on buffering. Tweaking the cache settings didn't help. It took me two days to go through all the kodi osmc forums and try out different solutions. Nothing worked in my case. So I decided to scrap OSMC. I had no intentions of switching to LibreELEC as it too was only a lighter version of kodi.







I've always used Raspberry Pi OS and the UI was too old school for a media centre. Additionally, I'd read about Ubuntu Mate playing YouTube better than Raspberry Pi OS and without heating up in some forums. In just a day, I was convinced that Ubuntu Mate was sluggish and had too many unnecessary applications preinstalled. I'm not sure if the substandard performance was because the latest Firefox didn't run well on Ubuntu, anyways having more than 5 tabs open literally made the RPi crawl. 







## YouTube on Raspberry Pi OS







The next obvious choice was using the latest Raspberry Pi OS Buster with just the barebones desktop and no recommended software. (This is one thing I always hated about Raspberry Pi OS - filled with bloatware that one had to manually remove later). The latest lite package was just perfect.  







Chromium browser came pre-installed and YouTube videos worked fine in it. Though, I don't think it's not going to throw up heating issues once continuous HD playback happens. This is mostly because the in-browser process is not hardware accelerated by the GPU. Using external players is the best way to go about achieving hardware acceleration for YouTube videos. Most tutorials on the internet refer to using youtube-dl and omxplayer. [YouTube-dl](https://github.com/ytdl-org/youtube-dl) to extract the videofile's link and [omxplayer ](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md)is the inbuilt commandline video player in Raspberry Pi OS. I tried all these. My issue was identical to the one someone posted on reddit - as shown below:








https://www.reddit.com/r/raspberry_pi/comments/8jfl5n/how_do_i_play_a_youtube_live_stream_full_screen/








So Streamplayer worked for me. 






    
    sudo apt install git python-setuptools
    git clone https://github.com/streamlink/streamlink
    cd streamlink/
    sudo python3 setup.py install







I was able to play videos using omxplayer but I couldn't turn it off without killing the script using the Ctrl-C or Alt-F4. The q button didn't work. Several attempts to make it work failed and I ended up switching to the much user friendly VLC media player. 







Streamlink uses VLC as the default player. Hence a separate player need not be specified with the `-p` parameter. Additionally you may use appropriate network and file caching to not see any buffering.






    
    streamlink --player "vlc --file-caching=5000 --network-caching=5000" https://www.youtube.com/watch?v={}







Once I had stream function set up, I wanted to control and select things on the Rpi using the TV's remote. I found a recent [guide](https://pimylifeup.com/raspberrypi-hdmi-cec/) to setting up HDMI-CEC on Raspberry Pi OS using the _cec-utils_ package. 







Follow the installation given in the guide linked above to setup and verify your HDMI-CEC connection. 







A [user](https://ubuntu-mate.community/u/GizmoXomziG) on the Ubuntu-mate community had created an extensive script to control the Rpi using the TV remote. Here's the link to the [post](https://ubuntu-mate.community/t/controlling-raspberry-pi-with-tv-remote-using-hdmi-cec/4250). 







Do not install the cec-client again as we already installed the whole cec-utils package earlier. 







Simply install just the [xdotools](http://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html) for controlling the mouse and sending keystrokes on the Rpi :






    
    sudo apt-get install xdotool







Follow rest of the guide to make the executable script and also check out the updated code found in one of the [replies ](https://ubuntu-mate.community/t/controlling-raspberry-pi-with-tv-remote-using-hdmi-cec/4250/4)- try and check which one works fine. You need not have the exact same remote so you'll have the change the code based on specific remote that you have. 







I also followed another reply on the post to get a virtual onscreen keyboard.






    
    sudo apt-get install xvkbd







To make it run at boot I tried using the [crontab](https://www.raspberrypi.org/documentation/linux/usage/cron.md) command and using [systemd](https://www.raspberrypi.org/documentation/linux/usage/systemd.md) both of it didn't work properly. systemd was running the program too early in boot and waiting for `graphical.target` or `network.target` didn't work. So in order to make it work after the desktop is loaded I did the following:






    
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart







To the above file added the startup script as follows:






    
    @ sudo /home/pi/start.sh







Make sure to specify the full path to the file and also convert the start.sh script into an executable using the following command:






    
    sudo chmod +x /home/pi/start.sh







My `start.sh` script contains the scripts I want to run at startup. Here's the custom remote code that I use for the SONY remote. 






    
    #!/bin/bash
    
    #!/bin/bash
    
    #-------------------- use to access GPIO and set status LEDs -----------------
    
    #using GPIO makes it mandatory to use sudo in calls
    
    #   Exports GPIO pin to userspace
    #echo "21" > /sys/class/gpio/export                  
    
    # Sets pin 21 as an output
    #echo "out" > /sys/class/gpio/gpio21/direction
    
    # Sets pin 21 to high
    #echo "0" > /sys/class/gpio/gpio21/value
    
    # Sets pin 18 to low
    #echo "0" > /sys/class/gpio/gpio18/value 
    
    #   Exports GPIO pin to userspace
    #echo "20" > /sys/class/gpio/export                  
    
    # Sets pin 20 as an output
    #echo "out" > /sys/class/gpio/gpio20/direction
    
    # Sets pin 20 to high
    #echo "1" > /sys/class/gpio/gpio20/value
    
    # Sets pin 18 to low
    #echo "0" > /sys/class/gpio/gpio18/value 
    
    
    #------------------main function --------------------------------
    # Original script of Simon Murgelj - https://ubuntu-mate.community/u/GizmoXomziG
    # Modified for use with SONY remote by glenzac
    
    
    
    function keychar {
        parin1=$1 #first param; abc1
        parin2=$2 #second param; 0=a, 1=b, 2=c, 3=1, 4=a, ...
        parin2=$((parin2)) #convert to numeric
        parin1len=${#parin1} #length of parin1
        parin2pos=$((parin2 % parin1len)) #position mod
        char=${parin1:parin2pos:1} #char key to simulate
        if [ "$parin2" -gt 0 ]; then #if same key pressed multiple times, delete previous char; write a, delete a write b, delete b write c, ...
            xdotool key "BackSpace"
        fi
        #special cases for xdotool ( X Keysyms )
        if [ "$char" = " " ]; then char="space"; fi
        if [ "$char" = "." ]; then char="period"; fi
        if [ "$char" = "-" ]; then char="minus"; fi
        xdotool key $char
    }
    datlastkey=$(date +%s%N)
    strlastkey=""
    strlastid=""
    intkeychar=0
    intmsbetweenkeys=1000 #two presses of a key sooner that this makes it delete previous key and write the next one (a->b->c->1->a->...)
    intmousestartspeed=15 #mouse starts moving at this speed (pixels per key press)
    intmouseacc=15 #added to the mouse speed for each key press (while holding down key, more key presses are sent from the remote)
    intmousespeed=15
    
    while read oneline
    do
        keyline=$(echo $oneline | grep " key ")
        echo $keyline --- debugAllLines
        if [ -n "$keyline" ]; then
            datnow=$(date +%s%N)
            datdiff=$((($datnow - $datlastkey) / 1000000)) #bla bla key pressed: previous channel (123)
            strkey=$(grep -oP '(?<=sed: ).*?(?= \()' <<< "$keyline") #bla bla key pres-->sed: >>previous channel<< (<--123)
            strstat=$(grep -oP '(?<=key ).*?(?=:)' <<< "$keyline") #bla bla -->key >>pressed<<:<-- previous channel (123)
            strpressed=$(echo $strstat | grep "pressed")
            strreleased=$(echo $strstat | grep "released")
            if [ -n "$strpressed" ]; then
                strid=$(grep -oP '(\[ ).*?(\])' <<< "$keyline") # get the id from the debug line to ingnore dupe detection.
                #echo $keyline --- debug
                if [ "$strkey" = "$strlastkey" ] && [ "$datdiff" -lt "$intmsbetweenkeys" ]; then
                    intkeychar=$((intkeychar + 1)) #same key pressed for a different char
                else
                    intkeychar=0 #different key / too far apart
                fi
                datlastkey=$datnow
                strlastkey=$strkey
                if [ "$strid" != "$strlastid" ]; then
                    case "$strkey" in
                        "1")
                            xdotool key "BackSpace"
                            ;;
                        "2")
                            keychar "abc2" intkeychar
                            ;;
                        "3")
                            keychar "def3" intkeychar
                            ;;
                        "4")
                            keychar "ghi4" intkeychar
                            ;;
                        "5")
                            keychar "jkl5" intkeychar
                            ;;
                        "6")
                            keychar "mno6" intkeychar
                            ;;
                        "7")
                            keychar "pqrs7" intkeychar
                            ;;
                        "8")
                            keychar "tuv8" intkeychar
                            ;;
                        "9")
                            keychar "wxyz9" intkeychar
                            ;;
                        "0")
                            keychar " 0.-" intkeychar
                            ;;
                        "previous channel")
                            xdotool key "Return" #Enter
                            ;;
                        "electronic program guide")
                            xdotool click 4 #mouse scroll up
                            ;;
                        "setup menu")
                            xdotool click 5 #mouse scroll down
                            ;;
                        "channels list")
                            xdotool click 3 #right mouse button click
                            ;;
                        "up")
                            intpixels=$((-1 * intmousespeed))
                            xdotool mousemove_relative -- 0 $intpixels #move mouse up
                            intmousespeed=$((intmousespeed + intmouseacc)) #speed up
                            ;;
                        "down")
                            intpixels=$(( 1 * intmousespeed))
                            xdotool mousemove_relative -- 0 $intpixels #move mouse down
                            intmousespeed=$((intmousespeed + intmouseacc)) #speed up
                            ;;
                        "left")
                            intpixels=$((-1 * intmousespeed))
                            xdotool mousemove_relative -- $intpixels 0 #move mouse left
                            intmousespeed=$((intmousespeed + intmouseacc)) #speed up
                            ;;
                        "right")
                            intpixels=$(( 1 * intmousespeed))
                            xdotool mousemove_relative -- $intpixels 0 #move mouse right
                            intmousespeed=$((intmousespeed + intmouseacc)) #speed up
                            ;;
                        "select")
                            xdotool click 1 #left mouse button click
                            ;;
                        "root menu")                        
    			killall vlc
    			
                            ;;
                        "sub picture")
                            echo Key Pressed: SUB PICTURE
    			sync;sync;shutdown -h now
                            ;;
                        "F2")
    			killall vlc
                            ;;
                        "F3")
    			python3 gui_test.py &
                            ;;
                        "F4")
                            #echo Key Pressed: YELLOW C
                            #sync;sync;shutdown -h now
    			chromium-browser "https://www.youtube.com" 
                            ;;
                        "F1")  
                        	((xvkbd++))
                        	switch=0
                        	xdotool mousemove 1100 750 
                        	xvkbd -no-keypad  -geometry 1920x350+0-20  &
                        	test $xvkbd -eq 2 && killall xvkbd && xvkbd=0 
                        	;;
                            #chromium-browser --incognito "https://www.google.com" &
                            #;;
                        "rewind")
                            echo Key Pressed: REWIND
                            ;;
                        "pause")
                            echo Key Pressed: PAUSE
                            ;;
                        "Fast forward")
                            echo Key Pressed: FAST FORWARD
                            ;;
                        "play")
                            echo Key Pressed: PLAY
                            ;;
                        "stop")
                            ## with my remote I only got "STOP" as key released (auto-released), not as key pressed; see below
                            echo Key Pressed: STOP
                            ;;
                        *)
                            echo Unrecognized Key Pressed: $strkey ; CEC Line: $keyline
                            ;;
    
                    esac
                else
                    echo Ignoring key $strkey with duplicate id $strid
                fi
                # store the id of the keypress to check for duplicate press count.
                strlastid=$strid
            fi
            if [ -n "$strreleased" ]; then
                #echo $keyline --- debug
                case "$strkey" in
                    "stop")
                        echo Key Released: STOP
                        ;;
                    "up")
                        intmousespeed=$intmousestartspeed #reset mouse speed
                        ;;
                    "down")
                        intmousespeed=$intmousestartspeed #reset mouse speed
                        ;;
                    "left")
                        intmousespeed=$intmousestartspeed #reset mouse speed
                        ;;
                    "right")
                        intmousespeed=$intmousestartspeed #reset mouse speed
                        ;;
                esac
            fi
        fi
    done
    







## Recommendations for the Rpi







  * change GPU allocation in [raspi-config](https://www.raspberrypi.org/documentation/configuration/raspi-config.md) to at least 128MB. I use 256MB for GPU.
  * [change default python to python3](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux) for best compatibility with streamlink when the command is executed as a script
  * use the modern [subprocess](https://docs.python.org/3/library/subprocess.html#subprocess-replacements) module instead of os.system call to run bash scripts within python
  * to wake a raspberry pi from the halt state (i.e after a shutdown with only the red light) simply connect a pushbutton in between board pins 5 and 6 on the pi. When the button is pressed the pin is shorted to ground and this triggers a boot on the Rpi
  * Power cycling can also be achieved by shorting the onboard RUN pins on the RPI. Note that no connections are soldered onto the pins. If you need to use it you have to manually solder header pins to it.
  * Also checkout this [one button halt and restart circuit](https://www.raspberrypi.org/forums/viewtopic.php?t=140994)
  * Set up a watchdog on Rpi to reboot it whenever it freezes or crashes this way you don't have to keep pulling the plug every time it crashes. I used the answer [here](https://raspberrypi.stackexchange.com/questions/99584/rpi-freezes-every-now-and-then-how-to-fix-it-with-a-watchdog). For my use-case I set the time to 20sec.
  * add cooling fan -- link to the post of power supply build 🔴🔴🔴
  * Added following commands to /boot/cmdline.txt to turn off network boost mode `smsc95xx.turbo_mode=N`
  * Run [Rpi diagnostics](https://www.raspberrypi.org/blog/sd-card-speed-test/) to check the speed of your SD card. I have a class 10 card but still it fared well in the speed test.







https://i.imgur.com/7AOXqSk.jpg








## Fetching YouTube live links and streams







The main purpose of this build is to watch live YouTube streams, especially news channels. The problem here is that different YouTube channels keep changing their live video links from time to time. Some channels change it after a couple of months. Some change it every few days. To not painstakingly find links each time we need to play something we need to use the YouTube API to fetch live links. 







  * First get the [channel ID](https://stackoverflow.com/questions/14366648/how-can-i-get-a-channel-id-from-youtube)
  * Use YouTube API calls to [fetch links to the live](https://stackoverflow.com/questions/37521853/how-to-get-youtube-live-stream-by-channel-id-in-youtube-api-v3-in-android) playback 






Here is the python program to fetch links automatically and save it to a file `links.txt` This needs your Google YouTube API key in the `api-key.txt` file in the same location. Also find the channel IDs manually as a one time process and add it to the list. Then this python code automatically fetches links to live streams. 






    
    import requests
    
    # List of CHannel ID (asianetnews,manorama,news24,mathrubhumi,kairali,mediaone,NDTV News,CNN Live,Parumala,Reporter,news18,jeevan,janam)
    CHANNEL_ID = ["UCf8w5m0YsRa8MHQ5bwSGmbw","UCP0uG-mcMImgKnJz-VjJZmQ","UCup3etEdjyF1L3sRbU-rKLw","UCwXrBBZnIh2ER4lal6WbAHw","UCkCWitaToNG1_lR-Si1oMrg","UC-f7r46JhYv78q5pGrO6ivA","UCZFMm1mMw0F81Z37aaEzTUA","UCef1-8eOpJgud7szVPlZQAQ","UC8ebJ_anG4byfhC_2hT7eKw","UCFx1nseXKTc1Culiu3neeSQ","UC-mMi78WJST4N5o8_i1FoXw","UCjX2Z1XGWEbKEGgKMACbhkw","UCNVkxRPqsBNejO6B9thG9Xw"]
    
    # Fetching the API Key
    file = open("api-key.txt", "r")
    YOUR_API_KEY = file.readline()
    file.close()
    
    #Defined empty Links array
    Links=[];
    
    # For each Channel Id, updating the channel Links 
    for channel in CHANNEL_ID:
    	URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&eventType=live&type=video&key={}".format(channel,YOUR_API_KEY);
    	req = requests.get(url = URL);
    	data = req.json()
    	try:
    		link = data['items'][0]['snippet']['thumbnails']['default']['url'].split("/")[4];
    		print(link)
    	except:
    		print("Link Not Found")
    		link="404"
    	finally:
    		Links.append(link)
    
    #Links File opened to write
    file2 = open(r"links.txt","w+")
    for link in Links:
    	file2.write(link+"\n")
    file2.close()







## Creating a custom GUI for the raspberry pi







I looked at all the options available for creating a GUI in python on a Rpi. Here are the best ones I found







  * Tkinter (standard GUI application for Python)
  * [guizero ](https://lawsie.github.io/guizero/about/)(simple GUI library based on Tkinter)
  * [kivy](https://kivy.org/#home)
  * [remi](https://github.com/dddomodossola/remi)
  * GTK+
  * PyQT






I chose guizero as it appeared to be very simple to implement and had good beginner friendly documentation.







The GUI looks as shown here: 🔴🔴🔴Insert GUI image 🔴🔴🔴







The python code for the custom GUI is as follows: 🔴🔴🔴













## Adding Kodi on Raspberry Pi OS







Add kodi to Raspberry Pi OS by running the following:






    
    sudo apt-get update
    sudo apt-get install kodi







To run simply execute `kodi` on the terminal. I'll be using kodi to list all the movies and music in the attached drives and to play them easily. If the HTTP server is turned on you can control playback on Kodi using the [Kore ](https://play.google.com/store/apps/details?id=org.xbmc.kore&hl=en_IN)App for KODI. 







## Adding a local Blynk server







Followed the instructions at the blynk.cc website to run a Blynk server on the Rpi. The NodeMCU connects to this server and runs the cooling fan of the pi when a connection is established.







To be done: 







  * send IR commands using ESP8266 or Rpi
  * using lircd or IR functions directly from the ESP8266


