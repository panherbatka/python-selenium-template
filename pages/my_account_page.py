from locators import locators


# Define locators in init class
class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

        # my account page elements
        self.input_login_username = locators.MyAccountPage.input_login_username
        self.input_login_password = locators.MyAccountPage.input_login_password
        self.input_reg_email = locators.MyAccountPage.input_reg_username
        self.input_reg_password = locators.MyAccountPage.input_reg_password
        self.link_logout = locators.MyAccountPage.link_logout
        self.message_failed = locators.MyAccountPage.message_failed
        self.btn_login = locators.MyAccountPage.btn_login
        self.btn_register = locators.MyAccountPage.btn_register

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        self.driver.find_element(*self.input_login_username).send_keys(username)
        self.driver.find_element(*self.input_login_password).send_keys(password)
        self.driver.find_element(*self.btn_login).click()

    def create_account(self, email, password):
        self.driver.find_element(*self.input_reg_email).send_keys(email)
        self.driver.find_element(*self.input_reg_password).send_keys(password)
        self.driver.find_element(*self.btn_register).click()

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.link_logout).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*self.message_failed).text
