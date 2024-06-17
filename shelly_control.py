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

import solar_logger

CLOUD_STATUS = "https://shelly-111-eu.shelly.cloud/device/status"
CLOUD_POWER = "https://shelly-111-eu.shelly.cloud/device/relay/control"
#CLOUD_STATUS = "https://shelly-111-eu.shelly.cloud"




class ShellyCloud(object):
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
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTPs error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
            
        return data
    
    @classmethod
    def relay(self, power):
        """
        power = <'on'|'off'>
        """
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
            print(f'HTTPs error occurred: {http_err}')
            return -1
        except Exception as err:
            print(f'Other error occurred: {err}')
            return -1
            
        return 0
            
        
