import time

import allure
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException, ElementNotVisibleException

from pageObjects.AutomationTask.TripShepherdAutomation import TripShepherdAutomation
from utilities.customlogger import LogGen


class Test_TripShepherd:
    # baseURL = ReadConfig.getApplicationURL()
    baseURL = 'https://www.tripshepherd.com/'
    city = 'Austin'
    date = '2024-04-19'
    name = 'Johan Smith'
    email = 'johansmith54@gmail.com'
    num = '512 555 0143'
    card = '4234543233454432'
    exp = '0225'
    cvc_code = '100'

    log = LogGen.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    def test_TripShepherd(self, setup):
        try:
            self.driver = setup
            self.driver.maximize_window()

            self.driver.get(self.baseURL)
            self.lp = TripShepherdAutomation(self.driver)
            self.log.info("Website is launching")
            time.sleep(3)
            self.lp.clickFindYourCity()
            self.log.info("Select Find Your City")
            self.log.info("Multiple city is displayed on page")
            time.sleep(7)
            self.lp.setCity(self.city)
            time.sleep(3)
            self.lp.clickAustinCity()
            self.log.info("Select Austin City")
            time.sleep(5)
            self.lp.clickPrivateTourofAustinCity()
            self.log.info("Select Private Tour of Austin City")
            time.sleep(3)
            self.lp.clickExclusivePrivateTourofAustin()
            self.log.info("Exclusive Private Tour of Austin City")
            time.sleep(4)

            # element = self.driver.find_element_by_id('whatsincluded')
            # self.log.info("I am here - Jahanzaib ")
            # self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
            time.sleep(5)
            self.lp.selectCalendar(self.date)
            self.log.info("***** The date 19 has been chosen on the calendar. ***** ")
            time.sleep(3)
            self.lp.selectPassenger()
            self.log.info("***** From the passengers dropdown, five passengers are selected. ***** ")
            time.sleep(3)
            self.lp.verifyPrice()
            self.log.info("***** Verify price remains the same ***** ")
            # time.sleep(3)
            # self.lp.verifyBookNow()
            time.sleep(3)
            self.lp.clickBookNow()
            self.log.info("***** Select on Book Now Button ***** ")
            self.log.info("***** The checkout page appears. ***** ")
            time.sleep(5)
            self.lp.setNameField(self.name)
            self.log.info("***** Enter Name Field ***** ")
            time.sleep(3)
            self.lp.setEmailField(self.email)
            self.log.info("***** Enter Email Field ***** ")
            time.sleep(3)
            self.lp.setPhoneNumberField(self.num)
            self.log.info("***** Enter Phone Number ***** ")

            element = self.driver.find_element_by_xpath('//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div[2]/h3')
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
            time.sleep(3)
            self.lp.setCardNumber(self.card)
            self.log.info("***** Enter Card Number ***** ")

            # wait = WebDriverWait(self.driver, 30)
            # element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.text_cardno_css_selector)))
            # element.send_keys("1234123412341234")
            time.sleep(3)
            self.lp.setExpiryDate(self.exp)
            self.log.info("***** Enter Expiry Date ***** ")
            time.sleep(3)
            self.lp.setCVCCode(self.cvc_code)
            self.log.info("***** Enter CVS code ***** ")
            time.sleep(3)
            verifyErrorMsg: str = self.lp.verifyCardNumberErrorMessage()
            print(verifyErrorMsg)
            if verifyErrorMsg == "Your card number is invalid.":
                self.log.info(" The Card Number Field Error Message appears is verified. ")
            else:
                self.log.warning("The Card Number Field Error Message isn't verified.")

            # time.sleep(3)
            # verifyCardExpiryMsg: str = self.lp.verifyCardNumberExpiryMessage()
            # print(verifyCardExpiryMsg)
            # if verifyCardExpiryMsg == "Your card's expiry date is in the past.":
            #     self.log.info(" The Card Expire Error Message appears is verified. ")
            # else:
            #     self.log.warning("The Card Expiry Error Message isn't verified.")

            # self.lp.clickPay()
            # self.log.info("***** Select Pay Button ***** ")

        except NoSuchElementException:
            self.log.warning('Element not found on Web end')
        # print("Element not found")
        except TimeoutException:
            self.log.warning('Session Timed Out!')

        except ElementNotInteractableException:
            self.log.warning('Element is not intractable.')

        except StaleElementReferenceException:
            self.log.warning('Element is no longer attached to the DOM')

        except ElementNotVisibleException:
            self.log.warning('Element is present on the page, but it is not visible.')
