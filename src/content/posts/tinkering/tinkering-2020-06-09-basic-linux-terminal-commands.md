---
author: glenzac
categories:
  - "tinkering"
cover:
  alt: creative internet computer display
  image: "@assets/wp-content/uploads/2020/06/pexels-photo-2004161.jpeg"
date: "2020-06-09T23:16:53+00:00"

summary: ""
tags:
  - code
  - linux
  - raspberrypi
  - raspbian

title: Basic Linux terminal commands
---


After using the Raspberry pi for a really long time now, I've finally begun to love the Linux way of things and the power it gives the user. All the commands listed below are from Linux. The Raspberry Pi itself is Debian. Only some path names mentioned below are specific to the Rpi, everything else is same for any Linux distro.

### Basic Linux Commands

- `ls `---\> list the files in current directory
- `sudo mkdir` ---\> make a new directory (folder)
- `cd /path_to_directory `---\> navigate to certain directory
- `sudo nano /path_to_file` ---\> text editor
- `sudo rm /path_to_file` ---\> delete a file
- `chmod +x /path_to_file` ---\> make script into executable file
- `sudo reboot` ---\> reboot the device
- `shutdown -h now` ---\> shutdown the device
- `chromium-browser www.google.com` ---\> Open Chromium and go to given URL
- `clear `---\> clear the terminal
- `python /path_to_file `---\> run python script
- `sudo pip install package_name `---\> used to install python packages in rpi
- `sudo pip uninstall package_name` ---\> used to uninstall python packages in rpi
- `sudo touch /path_to_file `---\> create a new file at the specified location
- `sudo apt-get update` ---\> fetch information about latest releases
- `sudo apt-get upgrade` ---\> upgrade OS to latest release
- `sudo apt autoremove` ---\> to remove downloaded package files after installation
- `killall name_of_application` ---\> to kill applications
- `apt-list --installed` ---\> view list of all installed packages
- `df -h` ---\> display disk space information
- `lxterminal ./path_to_script `---\> run a bash script in new terminal
- `ifconfig `---\> get IP address and details of network interfaces

### Set watchdog to reboot from a crash

`sudo nano /etc/systemd/system.conf`  
Then edit the following lines to:

`RuntimeWatchdogSec=20`  
`ShutdownWatchdogSec=10min`

### Run a command at startup

Edit the following file and add the full path to your script

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

Add `@sh /full_path_to_script `

### Fetch IP address

```
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    ipdisplay.value = ipaddr
```
