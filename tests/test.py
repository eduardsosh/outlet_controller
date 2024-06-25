import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import controller.shelly as shelly
import controller.fusionsolar as fusionsolar
import controller.csv_writer as csv_writer



class Test(unittest.TestCase):

    def test_can_connect(self):
        self.assertTrue(shelly.ShellyPlug.is_online())

    
    # def test_latest_prod(self):
    #     with fusionsolar.KioskApp() as app:
    #         self.assertIsNotNone(app.get_prod())

    def test_write_csv(self):
        #os.remove("data.csv")
        csv_writer.write_data(2.4,True)
        

    


if __name__ == '__main__':
    unittest.main()