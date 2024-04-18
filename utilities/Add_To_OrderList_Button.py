class AddToOrderList:
    button_add_to_order_list_id = "com.attech.attech_android_1.driq:id/relative_layout_next"

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_order_list(self):
        self.driver.find_element_by_id(self.button_add_to_order_list_id).click()
