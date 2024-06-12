from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import os
import solar_logger

import asyncio
from concurrent.futures import ThreadPoolExecutor


class KioskApp:
    def __init__(self, DEBUG=False):
        await 


    async def launch_browser(self):
        try:
            logger = solar_logger.Logger()
        except Exception as e:
            return
        
        kiosk_link = os.environ.get('SOLAR_LINK')
        if kiosk_link == None:
            print("No kiosk link found!")
            return
        
        options = Options()
        if not DEBUG:
            options.add_argument("--headless")

    def get_power_prod(self):


        
        




def main():





    #TODO Add asynchronus get of the power generation and other data

    try:
        driver = webdriver.Firefox(options=options)
        driver.get(kiosk_link)

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "station-name"),"Zemenu19"))

        element = driver.find_element(By.CSS_SELECTOR , ".nco-kiosk-overview-data")
        
        production_kw = element.text.replace("kW","")
        production_kw = float(production_kw)

        print(production_kw)



    except Exception as e:
        print(e)
    finally:
        driver.quit()



    
    


        
if __name__ == "__main__":
    main()