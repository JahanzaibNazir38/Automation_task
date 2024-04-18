from DriQ.pageObjects import Notifications


class TestOrderMedicationTestCase53:
    username = "aimantest@yopmail.com"
    password = "@Aiman@123"
    quantity = "One month"
    medication = "Panadol"
    postcode = "SW21HT"

    def test_case_53_order_medication(self, setup):
        self.driver = setup

        self.om = Notifications(self.driver)
        self.om.click_open_notifications_settings()
        self.om.enable_switch()
