class OkButton:
    textview_ok_xpath = '//XCUIElementTypeButton[@id="Ok"]'

    def __init__(self, driver):
        self.driver = driver

    def click_ok(self):
        self.driver.find_element_by_xpath(self.textview_ok_xpath).click()
