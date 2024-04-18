import os
import time
import allure
from pageObjects.EZWeb.ComplaintForm import Complaint
from utilities.customlogger import LogGen
from utilities.readConfig import ReadConfig
from pageObjects.EZWeb.PPGForm import PPG


@allure.severity(allure.severity_level.NORMAL)
class TestPPG:
    # Reading Variables from Config File
    admin_baseURL = ReadConfig.getbaseURL()
    admin_username = ReadConfig.getusername()
    admin_password = ReadConfig.getpassword()

    # Initializing Logger
    log = LogGen.loggen()

    baseURL = "https://newhampractice.attech.london/about-us/patient-reference-group/ppg-joiner-form/"
    full_name = "Aiman Test"
    email_id = "abc@yopmail.com"
    mobile_id = "034000000000"
    postcode_id = "SW21HT"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("To verify the submission of PPG Joiner form")
    #@allure.label(label_type="EndtoEnd")

    #@pytest.mark.sanity
    def test_ppg_form(self, setup):
        # Wordpress Forms - Form Submission

        self.log.info("***** Starting Testing of TestCase: PPG Joiner Form - Form Submission ***** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.log.info("***** PPG JOINER: Driver Initialized ***** ")

        #self.com = Complaint(self.driver)
        #self.com.close_popup()
        #self.log.info("***** PPG JOINER FORM: Cookies Pop-up closed ***** ")
        #time.sleep(4)

        self.ppg = PPG(self.driver)
        self.ppg.select_practice()
        self.log.info("***** PPG JOINER FORM: Practice Selected ***** ")

        self.ppg.set_fullname(self.full_name)
        self.log.info("***** PPG JOINER FORM: Adding Full name ***** ")

        self.ppg.set_email_id(self.email_id)
        self.log.info("***** PPG JOINER FORM: Adding Email address *****")

        self.ppg.set_mobile_id(self.mobile_id)
        self.log.info("***** PPG JOINER FORM: Adding Mobile Number *****")

        self.ppg.set_postcode_id(self.postcode_id)
        self.log.info("***** PPG JOINER FORM: Adding Postcode *****")

        self.ppg.select_gender()
        self.log.info("***** PPG JOINER FORM: Selecting Gender *****")

        self.ppg.select_age_group()
        self.log.info("***** PPG JOINER FORM: Selecting Age Group *****")

        self.ppg.select_come_to_practice()
        self.log.info("***** PPG JOINER FORM: How would you describe how often you come to the practice? *****")

        self.ppg.select_dropdown_ethnicity_id()
        self.log.info("***** PPG JOINER FORM: Selecting Ethnicity *****")

        self.ppg.button_ppg_attend()
        self.log.info("***** PPG JOINER FORM: How would you like to be involved?: Become a member of the PPG and attend meetings? *****")

        self.ppg.select_checkbox_one()
        self.log.info("***** PPG JOINER FORM: How would you like to be involved?: Fill in questionnaires by:(Select all applicable) *****")

        self.ppg.select_checkbox_keep_educational()
        self.log.info("***** PPG JOINER FORM: How would you like to be involved?: Be kept informed of educational or other events or changes in the practice by:(Select all applicable)  *****")

        self.ppg.select_checkbox_attend_meeting()
        self.log.info("***** PPG JOINER FORM: How would you like to be involved?: I would prefer to attend meetings in the: (Select all applicable) *****")

        self.ppg.submit_form()
        self.log.info("***** Submitting PPG Joiner form *****")
        #self.driver.close()

        #os.system('cmd /k "allure serve .\\PPG_Form_TestReport"')
