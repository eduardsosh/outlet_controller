import logging
logger = logging.getLogger(__name__)

import csv
import os
from datetime import datetime





def write_data(data1,data2):
    """Write two data columns to a file"""

    file_exists = os.path.isfile("data.csv")
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Define the row to be added
    row = [current_time, data1, data2]

    # Open the CSV file in append mode and write the new row
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(['Current Time', 'Prod KW', 'Shelly relay'])
        writer.writerow(row)

    logger.info(f"Append csv: {row}")