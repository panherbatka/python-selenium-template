import pytest

from pages.my_account_page import MyAccountPage
from providers.random_char import random_email


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("test@python.com", "test@python.com")

        msg = "An account is already registered with your email address. Please log in."
        assert msg in my_account_page.get_error_message()

    def test_create_account_success(self):
        email = random_email(10)
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "test@python.com")

        assert my_account_page.is_logout_link_displayed()
