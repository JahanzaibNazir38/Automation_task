from selenium import webdriver
import pytest


@pytest.fixture()
def setup():

    driver = webdriver.Chrome(executable_path=r"C:\\Users\\Jahanzaib Ch\\Downloads\chromedriver-win64\\chromedriver.exe")
    return driver

# @pytest.fixture()
# def setup1():
#     desired_cap ={
#             "appium:deviceName": "Android Emulator",
#             "platformName": "Android",
#             "appium:udid": "ce061716b3a3e0490d7e",
#             "appium:platformVersion": "9",
#             "appium:appPackage": "com.attech.attech_android_1.driq",
#             "appium:appWaitActivity": "com.attech.attech_android_1.driq.RegistrationModule.activities.SplashScreen",
#             "appium:app": "C:\\Users\\Taimoor Khan\\Downloads\\Release73-Staging.apk"
#     }
#
#     driver1 = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
#     return driver1
# driver1.implicitly_wait(50)
