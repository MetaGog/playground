import unittest
from testscript import get_devices, update_device_price, create_user, check_user_credentials, add_device_submission

class TestDatabaseFunctions(unittest.TestCase):

    def test_create_user(self):
        create_user('testuser', 'testpassword')
        self.assertTrue(check_user_credentials('testuser', 'testpassword'))

    def test_update_device_price(self):
        update_device_price(1, 99.99)
        devices = get_devices()
        self.assertEqual(devices['price'], 99.99)

    def test_add_device_submission(self):
        add_device_submission('testuser', 'TestBrand', 'TestModel')
        # Add code to verify the submission was added correctly

if __name__ == '__main__':
    unittest.main()
