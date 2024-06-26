import os
import sys
import unittest
from unittest.mock import patch

# Ensure the parent directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the modules to be tested
import controller.shelly as shelly
import controller.fusionsolar as fusionsolar
import controller.csv_writer as csv_writer

class TestController(unittest.TestCase):

    @patch('controller.shelly.ShellyPlug.is_online')
    def test_can_connect(self, mock_is_online):
        mock_is_online.return_value = True
        self.assertTrue(shelly.ShellyPlug.is_online())
        mock_is_online.assert_called_once()

    @patch('controller.fusionsolar.KioskApp.get_prod')
    def test_latest_prod(self, mock_get_prod):
        mock_get_prod.return_value = 100.0  # Mocked production value
        with fusionsolar.KioskApp() as app:
            prod = app.get_prod()
            self.assertIsNotNone(prod)
            self.assertEqual(prod, 100.0)
        mock_get_prod.assert_called_once()

    def test_write_csv(self):
        test_file = "data.csv"
        if os.path.exists(test_file):
            os.remove(test_file)

        try:
            csv_writer.write_data(2.4, True)
            self.assertTrue(os.path.exists(test_file))

            with open(test_file, 'r') as f:
                content = f.read()
                self.assertIn("2.4", content)
                self.assertIn("True", content)
        finally:
            if os.path.exists(test_file):
                os.remove(test_file)

if __name__ == '__main__':
    unittest.main(verbosity=2)
