class BackButton:
    button_back_xpath = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    button_back_class_name = '//android.widget.ImageButton'


    def __init__(self, driver):
        self.driver = driver

    def click_back(self):
        self.driver.find_element_by_xpath(self.button_back_xpath).click()

    def click_back_button(self):
        self.driver.find_element_by_class_name(self.button_back_class_name).click()



