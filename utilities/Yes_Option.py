class SelectYesOption:
    textview_yes_xpath = '//android.widget.TextView[@text="Yes"]'

    def __init__(self, driver):
        self.driver = driver

    def select_yes(self):
        self.driver.find_element_by_xpath(self.textview_yes_xpath).click()
