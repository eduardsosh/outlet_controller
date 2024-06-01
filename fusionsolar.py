from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import os
import solar_logger



def main():
    try:
        logger = solar_logger.Logger()
    except Exception as e:
        return

    kiosk_link = os.environ.get('SOLAR_LINK')

    options = Options()
    options.add_argument("--headless")

    #TODO Add asynchronus get of the power generation and other data

    try:
        driver = webdriver.Firefox(options=options)
        driver.get(kiosk_link)
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "nco-kiosk-overview-data"))
        )
        print(element.text[:-2])
    except Exception as e:
        print(e)
    finally:
        driver.quit()



    
    


        
if __name__ == "__main__":
    main()