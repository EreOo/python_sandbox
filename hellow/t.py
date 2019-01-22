import unittest
from zipfile import ZipFile
import json
import os
import random
from time import sleep


from appium.webdriver.applicationstate import ApplicationState
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from appium import webdriver


# the emulator is sometimes slow and needs time to think

SLEEPY_TIME = 1

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppiumTests(unittest.TestCase):

    def test(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = '73QDU16B30000847'
        desired_caps['app'] = PATH('/Users/shekhavtsov/Desktop/bank.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        from hellow.locator import xSelector
        self.driver.find_element_by_android_uiautomator(xSelector('ru.alfabank.mobile.android:id/sign_up_demo'))
        self.driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"ru.alfabank.mobile.android:id/sign_up_demo\")").click()
        self.driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"ru.alfabank.mobile.android:id/all_payments_widget_payments\")").click()
        self.driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"ru.alfabank.mobile.android:id/sign_up_demo\")").click()

    def tearDown(self):
        self.driver.quit()

        # remove zipped file from `test_pull_folder`
        if hasattr(self, 'zipfilename') and os.path.isfile(self.zipfilename):
            os.remove(self.zipfilename)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

