import pytest

from pages.my_account_page import MyAccountPage
from providers.random_char import random_email


@pytest.mark.usefixtures("setup")
class TestLogIn:
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test@python.com", "test@python.com")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        email = random_email(10)
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in(email, "test@python.com")

        msg = "ERROR: Incorrect username or password."
        assert msg in my_account_page.get_error_message()
