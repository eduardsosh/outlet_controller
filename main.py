
# Set up logging
import logging
from controller.solar_logger import setup_logging
setup_logging()
logger = logging.getLogger(__name__)



import controller.shelly as shelly
import controller.fusionsolar as fusionsolar


global counter


# Make selenium less verbose
logging.getLogger('urllib3.connectionpool').setLevel(logging.WARNING)
logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.WARNING)



def main():

    with fusionsolar.KioskApp() as app:
        app.get_prod()
        

        

def is_within_params(curr_prod):
    if curr_prod > 2:
         return True
    else:
         return False
    

     

if __name__ == "__main__":
    main()
    