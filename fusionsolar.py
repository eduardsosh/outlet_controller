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
        self.active = True       
        print("Starting selenium browser!")
        self.driver_thread = threading.Thread(target=self.start_browser)
        self.driver_thread.start()

    def start_browser(self):
        print("starting thread")
        kiosk_link = os.environ.get('SOLAR_LINK')
        if kiosk_link == None:
            print("No kiosk link found!")
            return

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--detach")
        self.driver = webdriver.Firefox(options=options)

        self.driver.get(kiosk_link)

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "station-name"),"Zemenu19"))

        element = self.driver.find_element(By.CSS_SELECTOR , ".nco-kiosk-overview-data")

        print(f"Started driver, current prod: {element.text}")
        while self.active:
            time.sleep(1)

    def get_prod(self):
        element = self.driver.find_element(By.CSS_SELECTOR , ".nco-kiosk-overview-data")
        production_kw = element.text.replace("kW","")
        production_kw = float(production_kw)
        return production_kw
    
    def stop_driver(self):
        self.active = False
        


        
        




def main():
    fusionApp = KioskApp()
    time.sleep(10)
    print(fusionApp.get_prod())
    time.sleep(10)
    print(fusionApp.get_prod())
    


        
if __name__ == "__main__":
    main()