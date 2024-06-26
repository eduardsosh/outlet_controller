# outlet_controller
A programm to control a smart electricity plug depending on data from FusionSolar solar panel data.


---
## How it works

A cron job will be set to execute main.py every 5 minutes.
The programm will retrieve solar panel production data and shelly status and log this info.
If the conditions are satisfied, the ShellyPlug relay will be set to switch on, else, switch off.

Program was initially written to work constantly, but to save system resources as the intended machine doesn't have many a cron job will be made to take care of it.

Usage:
TODO

