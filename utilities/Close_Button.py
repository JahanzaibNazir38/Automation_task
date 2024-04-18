class CloseButton:
    textview_close_id = "com.attech.attech_android_1.driq:id/close"

    def __init__(self, driver):
        self.driver = driver

    def click_close(self):
        self.driver.find_element_by_id(self.textview_close_id).click()
