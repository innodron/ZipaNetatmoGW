#!/usr/bin/python
# encoding=utf-8

# This module will synchronise a Zipabox Home Automation Controller to a Netatmo Weather Station
# Published December 2015
# Author : innodron - Innodron Technology - support@innodron.com

import lnetatmo
from urllib2 import urlopen

# HTTP device base URL
ZIPABOX_URL         = 'http://my.zipato.com/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&%s='

##
### USER SPECIFIC INFO
###############################################################################

# Do not forget to set your Netatmo Developer OAUTH setting, my.netatmo.com Username and Password in lnetatmo.py

# Zipabox serial
ZIPABOX_SERIAL      = '0123456789012345'

# APIKey and Endpoint UUID of the Zipabox Virtual Meter and Virtual Sensor that will present Netatmo measures
METER_APIKEY        = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
METER_EP            = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
SENSOR_APIKEY       = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
SENSOR_EP           = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

# netatmo module names as seen at https://my.netatmo.com/app/station
indoor_modl_name    = 'indoor'
oudoor_modl_name    = 'outdoor'

# Netatmo sensor names as seen at https://my.netatmo.com/app/station
indoor_temp_sensor  = 'Temperature'     # Temperature (ºC)
oudoor_temp_sensor  = 'Temperature'     # Temperature (ºC)
indoor_humi_sensor  = 'Humidity'        # Humidity (%)
oudoor_humi_sensor  = 'Humidity'        # Humidity (%)
indoor_co2l_sensor  = 'CO2'             # CO2 Level (ppm)
indoor_co2l_limit   = 1000              # CO2 level threshold for sensor trigger
indoor_pres_sensor  = 'Pressure'        # Pressure (mb)
indoor_sndl_sensor  = 'Noise'           # Sound level (dB)

# Corresponding Zipato Virtual endpoints
indoor_temp_zipaurl = ZIPABOX_URL % (ZIPABOX_SERIAL, METER_EP, METER_APIKEY, 'value1')      # Temperature (ºC)
oudoor_temp_zipaurl = ZIPABOX_URL % (ZIPABOX_SERIAL, METER_EP, METER_APIKEY, 'value2')      # Temperature (ºC)
indoor_humi_zipaurl = ZIPABOX_URL % (ZIPABOX_SERIAL, METER_EP, METER_APIKEY, 'value3')      # Humidity (%)
oudoor_humi_zipaurl = ZIPABOX_URL % (ZIPABOX_SERIAL, METER_EP, METER_APIKEY, 'value4')      # Humidity (%)
indoor_co2l_zipaurl = ZIPABOX_URL % (ZIPABOX_SERIAL, METER_EP, METER_APIKEY, 'value5')      # CO2 Level (ppm)
indoor_pres_zipaurl = ZIPABOX_URL % (ZIPABOX_SERIAL, METER_EP, METER_APIKEY, 'value6')      # Pressure (mb)
indoor_sndl_zipaurl = ZIPABOX_URL % (ZIPABOX_SERIAL, METER_EP, METER_APIKEY, 'value7')      # Sound level (dB)
indoor_co2s_zipaurl = ZIPABOX_URL % (ZIPABOX_SERIAL, SENSOR_EP, SENSOR_APIKEY, 'state')     # CO2 Sensor (true/false)

###############################################################################
### END USER SPECIFIC INFO
##

# Read the most recent values from Netatmo
print ('Reading from Netatmo...')
authorization = lnetatmo.ClientAuth()
devList = lnetatmo.DeviceList(authorization)
indoor_temp_value   = "%.2f" % devList.lastData()[indoor_modl_name][indoor_temp_sensor]
indoor_humi_value   = "%.2f" % devList.lastData()[indoor_modl_name][indoor_humi_sensor]
indoor_co2l_value   = "%.2f" % devList.lastData()[indoor_modl_name][indoor_co2l_sensor]
indoor_co2s_value   = '1' if devList.lastData()[indoor_modl_name][indoor_co2l_sensor] > indoor_co2l_limit else '0'
indoor_pres_value   = "%.2f" % devList.lastData()[indoor_modl_name][indoor_pres_sensor]
indoor_sndl_value   = "%.2f" % devList.lastData()[indoor_modl_name][indoor_sndl_sensor]
oudoor_temp_value   = "%.2f" % devList.lastData()[oudoor_modl_name][oudoor_temp_sensor]
oudoor_humi_value   = "%.2f" % devList.lastData()[oudoor_modl_name][oudoor_humi_sensor]

print ('Pushing to Zipabox...')
# Write the parameters to Zipabox Virtual Meter and Virtual Sensor
urlopen(indoor_temp_zipaurl + indoor_temp_value)
urlopen(indoor_humi_zipaurl + indoor_humi_value)
urlopen(indoor_co2l_zipaurl + indoor_co2l_value)
urlopen(indoor_co2s_zipaurl + indoor_co2s_value)
urlopen(indoor_pres_zipaurl + indoor_pres_value)
urlopen(indoor_sndl_zipaurl + indoor_sndl_value)
urlopen(oudoor_temp_zipaurl + oudoor_temp_value)
urlopen(oudoor_humi_zipaurl + oudoor_humi_value)
print ('Zipabox successfully updated')


