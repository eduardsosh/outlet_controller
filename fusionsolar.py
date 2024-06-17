"""
Utility to retrieve latest solar energy production data from fusion solar kiosk webpage.
Required environment variables: 
SOLAR_LINK : Fusion solar kiosk url
STATION_NAME : Fusion solar station name

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import os
import solar_logger

import threading
import time

class KioskApp:
    def __init__(self, DEBUG=False): 
        self.logger = solar_logger.Logger()
        
        # Get environment variables and check their existance
        self.kiosk_link = os.environ.get('SOLAR_LINK')
        self.station_name = os.environ.get('STATION_NAME')
        
        if not self.kiosk_link:
            print("Error: Missing solar url!")
            return
        if not self.station_name:
            print("Error: Missing station name!")
            return
        
        self.active = threading.Event()
        self.loaded = threading.Event()

        # Start selenium driver thread
        self.driver_thread = threading.Thread(target=self.start_browser)
        self.driver_thread.start()
        self.active.set()
        

    def start_browser(self):
        self.logger.info("Starting driver")

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--detach")
        self.driver = webdriver.Firefox(options=options)
        
        self.loaded.set()


        try:
            while self.active.is_set():
                time.sleep(1)
        except Exception as e:
            self.logger.error(f"Error in browser thread: {e}")
        finally:
            self.logger.info("Stopping driver")
            self.driver.quit()

    def get_prod(self):
        try:
            if self.driver and self.active.is_set():
                self.driver.get(self.kiosk_link)
                WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "station-name"),self.station_name))

                element = self.driver.find_element(By.CSS_SELECTOR , ".nco-kiosk-overview-data")
                production_kw = element.text.replace("kW","")
                production_kw = float(production_kw)
                return production_kw
        except Exception as e:
            self.logger.error(f"Cannot get recent data: {e}")
            return None
        
    

    def stop_browser(self):
        self.logger.info("Stopping driver")
        self.active.clear()
        self.driver_thread.join()
        
    def is_active(self):
        return self.active.is_set()
    
    def has_loaded(self):
        return self.loaded.is_set()



