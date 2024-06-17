import shelly_control
import fusionsolar
import time

global counter

def main():
    print(shelly_control.ShellyCloud().get_status())
    
    kioskapp = fusionsolar.KioskApp()
    while not kioskapp.has_loaded():
        print("Starting selenium")
        time.sleep(1)
        
    while True:
        print(kioskapp.get_prod())
        if kioskapp.get_prod() > 2:
            shelly_control.ShellyCloud().relay('on')
        else:
            shelly_control.ShellyCloud().relay('off')
            
        time.sleep(900)
        
    

if __name__ == "__main__":
    main()
    