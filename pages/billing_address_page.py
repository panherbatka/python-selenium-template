from selenium.webdriver.support.select import Select

from locators.locators import BillingAddressLocators


# Direct locators approach
class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver

    def open_edit_billing_address(self):
        self.driver.find_element(*BillingAddressLocators.link_addresses).click()
        self.driver.find_element(*BillingAddressLocators.btn_edit).click()

    def set_personal_data(self, first_name, last_name):
        self.driver.find_element(*BillingAddressLocators.input_first_name).send_keys(first_name)
        self.driver.find_element(*BillingAddressLocators.input_last_name).send_keys(last_name)

    def select_country(self, country):
        select = Select(self.driver.find_element(*BillingAddressLocators.select_country))
        select.select_by_visible_text(country)

    def set_address(self, address, postcode, city):
        self.driver.find_element(*BillingAddressLocators.input_address).send_keys(address)
        self.driver.find_element(*BillingAddressLocators.input_postcode).send_keys(postcode)
        self.driver.find_element(*BillingAddressLocators.input_city).send_keys(city)

    def set_phone_number(self, phone):
        self.driver.find_element(*BillingAddressLocators.input_phone).send_keys(phone)

    def save_billing_address(self):
        self.driver.find_element(*BillingAddressLocators.button_save).click()

    def get_message_text(self):
        return self.driver.find_element(*BillingAddressLocators.message_success).text
