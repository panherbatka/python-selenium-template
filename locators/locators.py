from selenium.webdriver.common.by import By


class BillingAddressLocators:
    input_email = (By.ID, "reg_email")
    input_password = (By.ID, "reg_password")
    link_addresses = (By.LINK_TEXT, "Addresses")
    btn_edit = (By.LINK_TEXT, "Edit")
    input_first_name = (By.ID, "billing_first_name")
    input_last_name = (By.ID, "billing_last_name")
    select_country = (By.ID, "billing_country")
    input_address = (By.ID, "billing_address_1")
    input_postcode = (By.ID, "billing_postcode")
    input_city = (By.ID, "billing_city")
    input_phone = (By.ID, "billing_phone")
    button_save = (By.XPATH, "//button[@value='Save address']")
    message_success = (By.XPATH, "//div[@class='woocommerce-message']")


class MyAccountPage:
    input_login_username = (By.ID, "username")
    input_login_password = (By.ID, "password")
    btn_login = (By.NAME, "login")

    input_reg_username = (By.ID, "reg_email")
    input_reg_password = (By.ID, "reg_password")
    btn_register = (By.NAME, "register")

    link_logout = (By.LINK_TEXT, "Logout")
    message_failed = (By.XPATH, "//ul[@class='woocommerce-error']//li")
