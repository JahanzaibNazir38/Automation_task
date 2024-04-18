class FinishButton:
    # button_finish_id = 'com.attech.attech_android_1.driq:id/relative_layout_next'
    button_finish_id = 'com.attech.attech_android_1.driq:id/btn_next'

    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        self.driver.find_element_by_id(self.button_finish_id).click()
