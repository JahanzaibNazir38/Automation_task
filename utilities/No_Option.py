class SelectNoOption:
    textview_no_xpath = '//android.widget.TextView[@text="No"]'

    def __init__(self, driver):
        self.driver = driver

    def select_no(self):
        self.driver.find_element_by_xpath(self.textview_no_xpath).click()