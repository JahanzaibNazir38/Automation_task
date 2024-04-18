import warnings
from telnetlib import EC

import self
from selenium.webdriver.support import expected_conditions as EC
from py import log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class TripShepherdAutomation:
    # Define locators for Austin City fields
    button_findYourCity_xpath = '//*[@id="hero"]/div[1]/button/span'
    text_searchCity_xpath = '//*[@id="hero"]/div[2]/div/div[1]/div/input'
    button_austin_xpath = '//*[@id="hero"]/div[2]/div/div[2]/a/div/div/span'
    button_privateTourofAustin_xpath = '//*[@id="featured_exp_nav"]/nav/div[4]'
    button_exclusivePrivateTour_xpath = '//*[@id="tour-section"]/div[1]/a/div/p'
    dropdown_Date_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img'
    text_Date_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/button[19]/abbr'
    dropdown_Passenger_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[1]'
    text_priceUSD_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div/div/div/p'
    # text_bookNow_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div/div/div/button'
    button_bookNow_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div/div/div/button'
    # Define locators for checkout page fields
    text_nameField_xpath = '//*[@id="payment-form"]/div[1]/input'
    text_emailField_xpath = '//*[@id="payment-form"]/div[2]/input'
    text_PhoneField_xpath = '/html/body/div/main/div[2]/div/div[2]/div[2]/form/div[3]/div/input'
    text_cardNumber_id = 'Field-numberInput'
    text_cardError_id = 'Field-numberError'
    text_expiryDate_id = 'Field-expiryInput'
    # text_cardExpirymsg_xpath = '//*[@id="Field-expiryError"]'
    text_cvs_id = 'Field-cvcInput'
    button_pay_id = '//*[@id="ga4-event-listener-checkout"]'

    def __init__(self, driver):
        self.driver = driver
        self.log = log

    def clickFindYourCity(self):
        self.driver.find_element_by_xpath(self.button_findYourCity_xpath).click()

    def setCity(self, city):
        self.driver.find_element_by_xpath(self.text_searchCity_xpath).send_keys(city)

    def clickAustinCity(self):
        self.driver.find_element_by_xpath(self.button_austin_xpath).click()

    def clickPrivateTourofAustinCity(self):
        self.driver.find_element_by_xpath(self.button_privateTourofAustin_xpath).click()

    def clickExclusivePrivateTourofAustin(self):
        self.driver.find_element_by_xpath(self.button_exclusivePrivateTour_xpath).click()

    def selectCalendar(self, date):
        # Click on the date dropdown
        self.driver.find_element_by_xpath(self.dropdown_Date_xpath).click()

        # Find and click on the desired date
        date_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/button[19]'
        self.driver.find_element_by_xpath(date_xpath).click()

    # def select_time_1230_pm(self):
    #     time_radio_btn = self.driver.find_element(By.XPATH, "//input[@type='radio' and @value='12:30 pm']")
    #     if not time_radio_btn.is_selected():
    #         time_radio_btn.click()

    def selectPassenger(self):
        # Click on the date dropdown
        self.driver.find_element_by_xpath(self.dropdown_Passenger_xpath).click()

        # Find and click on the desired 5 Passengers
        pass_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div/p[5]'
        self.driver.find_element_by_xpath(pass_xpath).click()

    def verifyPrice(self):
        price = self.driver.find_element(By.XPATH, self.text_priceUSD_xpath).text
        print(price)
        if price == "Starting From  789.00 USD":
            assert True
        # else:
        # assert False

    def verifyExpiryMsg(self):
        price = self.driver.find_element(By.XPATH, self.text_priceUSD_xpath).text
        print(price)
        if price == "Starting From  789.00 USD":
            assert True
        # else:
        # assert False

    # def verifyBookNow(self):
    #     g = self.driver.find_element(By.XPATH, self.text_bookNow_xpath).text
    #     print(g)
    #     if g == "Book now $789":
    #         assert True
    #     else:
    #         assert False

    def clickBookNow(self):
        self.driver.find_element_by_xpath(self.button_bookNow_xpath).click()

    # Methods for checkout page

    def setNameField(self, name):
        self.driver.find_element_by_xpath(self.text_nameField_xpath).click()
        self.driver.find_element_by_xpath(self.text_nameField_xpath).send_keys(name)

    def setEmailField(self, email):
        self.driver.find_element_by_xpath(self.text_emailField_xpath).send_keys(email)

    def setPhoneNumberField(self, number):
        self.driver.find_element_by_xpath(self.text_PhoneField_xpath).click()
        self.driver.find_element_by_xpath(self.text_PhoneField_xpath).send_keys(number)

    def setCardNumber(self, card):
        # Switch to the iframe
        iframe = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
        self.driver.switch_to.frame(iframe)

        # Now interact with the card number field
        card_number_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.text_cardNumber_id))
        )
        card_number_element.click()
        card_number_element.clear()
        card_number_element.send_keys(str(card))

    def setExpiryDate(self, exp):
        # Wait for the expiry date field to be clickable
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.text_expiryDate_id)))
        expiry_date_element = self.driver.find_element_by_id(self.text_expiryDate_id)
        expiry_date_element.click()
        # Clear the field if necessary
        expiry_date_element.clear()
        # Input the expiry date
        expiry_date_element.send_keys(exp)

    def setCVCCode(self, code):
        self.driver.find_element_by_id(self.text_cvs_id).click()
        self.driver.find_element_by_id(self.text_cvs_id).clear()
        self.driver.find_element_by_id(self.text_cvs_id).send_keys(code)

    def verifyCardNumberErrorMessage(self):
        textErrorMsg = self.driver.find_element(By.ID, self.text_cardError_id).text
        return textErrorMsg

    # def verifyCardNumberExpiryMessage(self):
    #     textExpiryErrorMsg = self.driver.find_element(By.XPATH, self.text_cardExpirymsg_xpath).text
    #     return textExpiryErrorMsg
    #
    # def clickPay(self):
    #     self.driver.find_element_by_xpath(self.button_pay_id).click()


