
# Set up logging
import logging
from solar_logger import setup_logging
setup_logging()
logger = logging.getLogger(__name__)



import shelly
import fusionsolar
import time
import json

global counter


# Make selenium less verbose
logging.getLogger('urllib3.connectionpool').setLevel(logging.WARNING)
logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.WARNING)



def main():
    print(shelly.ShellyPlug.is_online())
    # logger.info(shelly_control.ShellyPlug().get_status())
    
    # kioskapp = fusionsolar.KioskApp()
    # while not kioskapp.has_loaded():
    #     logger.info("Starting selenium!")
    #     time.sleep(1)
        
    # while True:
    #     print(kioskapp.get_prod())
    #     if is_within_params(kioskapp.get_prod()):
    #         #shelly_control.ShellyPlug().relay('on')
    #         print("Turn on")
    #     else:
    #         #shelly_control.ShellyPlug().relay('off')
    #         print("Turn off")

        
    #     # Sleep 5 minutes
    #     time.sleep(900)
        

def is_within_params(curr_prod):
    if curr_prod > 2:
         return True
    else:
         return False
    

     

if __name__ == "__main__":
    main()
    