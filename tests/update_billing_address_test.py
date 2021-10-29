import pytest
from selenium.webdriver.common.by import By

from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage
from providers.random_char import random_email


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = random_email(10)
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "python@python.com")

        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("John", "Doe")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Warszawska 10", "01-001", "Warszawa")
        billing_address_page.set_phone_number("123456789")
        billing_address_page.save_billing_address()

        msg = "Address changed successfully."
        assert msg in billing_address_page.get_message_text()
