class NextButton:
    button_next_id = 'com.attech.attech_android_1.driq:id/relative_layout_next'

    def __init__(self, driver):
        self.driver = driver

    def click_next(self):
        self.driver.find_element_by_id(self.button_next_id).click()
