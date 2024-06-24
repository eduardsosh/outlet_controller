"""
Module to access and control Shelly smart plug using Shelly cloud control API
Required environment variables:
SHELLY_API_KEY : cloud api key
SHELLY_PLUG_ID : id from cloud for the device
"""
import os
import requests
import time
import json

import logging
logger = logging.getLogger(__name__)

CLOUD_STATUS = "https://shelly-111-eu.shelly.cloud/device/status"
CLOUD_POWER = "https://shelly-111-eu.shelly.cloud/device/relay/control"
#CLOUD_STATUS = "https://shelly-111-eu.shelly.cloud"




class ShellyPlug(object):
    API_KEY = os.environ.get("SHELLY_API_KEY")
    PLUG_ID = os.environ.get("SHELLY_PLUG_ID")
    

    @classmethod
    def get_status(self):
        payload = { 
            'id': self.PLUG_ID,
            'auth_key': self.API_KEY.strip(),
        }
        try:
            response = requests.post(CLOUD_STATUS,data=payload)
            response.raise_for_status()

            data = response.text

        except Exception as err:
            logger.error(f'Other error occurred: {err}')
            return
            
        return data
    
    @classmethod
    def relay(self, power):
        """Power: <'on'|'off'>"""

        payload = {
            'channel' : '0',
            'turn' : power,
            'id': self.PLUG_ID,
            'auth_key': self.API_KEY,
        }
        
        try:
            response = requests.post(CLOUD_POWER,data=payload)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f'HTTPs error occurred: {http_err}')
            return -1
        except Exception as err:
            logger.error(f'Other error occurred: {err}')
            return -1
            
        return 0
    
    @classmethod
    def is_online(self):
        return self.__get_info("data.online")
    
    @classmethod
    def is_powered(self):
        return self.__get_info("data.device_status.relays.0.ison")
    
    @classmethod
    def __get_info(self,option):
        data = self.get_status()  # Get the status from the ShellyPlug
        data_json = json.loads(data)
        
        keys = option.split(".")  # Split the option by periods
        
        value = data_json
        for key in keys:
            if key.isdigit():  # Check if the key is an index for a list
                key = int(key)  # Convert the key to an integer index
            value = value[key]
        
        return value
            
        
