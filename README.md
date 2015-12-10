# ZipaNetatmoGW
A Python module for synchronizing a Zipabox Home Automation Controller to a Netatmo Weather Station

# Dependencies
This module requires lnetatmo.py from https://github.com/philippelt/netatmo-api-python

# Installation
__Zipabox__

1. Add one Virtual Meter device and one Virtual Sensor device to the Zipabox
1. Name the devices and set their types properly  
   -- for the Sensor, set type to CO sensor  
   -- for Meter values set units to Temperature (ºC), Humidity (%), CO2 Level (ppm), Pressure (mb), Sound level (dB)  
1. Check and note the URL for the Sensor's STATE attribute
1. Check and note the URL for the Meter's VALUE attributes

__Gateway device (python host)__

1. Put the gw.py and lnetatmo.py in a folder - preferably somewhere in user's home folder tree
1. Make gw.py executable  
   ```$ chmod +x gw.py```
1. Edit gw.py to set user specific information with help of URL's above
1. Edit lnetatmo.py to set your Netatmo Developer OAUTH credentials and User my.netatmo.com credentials
1. Run the module  
   ```$ <module location>/gw.py```
1. If you do not see a message with a smiling face, check these instructions again
1. If still no joy, create an issue at https://github.com/innodron/ZipaNetatmoGW/issues

# Running periodically
To run the module periodically, make it executable and add it to cron in your favorite ***nix** environment

__e.g. To run this module in 15 min. intervals with a RaspberryPI:__

1. Open cron editor  
   ```$ crontab -e```  
2. Add the following line (assuming your RaspberryPI user is pi, and script is at ~/scripts/ZipaNetatmoGW)  
   ```*/15 * * * * /home/pi/scripts/ZipaNetatmoGW/gw.py 2>&1 | logger -t [ZipatoNetatmoGW]```  
3. Save and exit cron editor

