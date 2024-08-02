from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Payment:
    name = (By.NAME, "project_name")
    contact = (By.NAME, "shipping_contact_phone")
    flag = (By.NAME, "new_construction")
    address = (By.NAME, "shipping_address")
    city = (By.NAME, "shipping_city")
    state = (By.NAME, "shipping_state")  # select
    zipcode = (By.NAME, "shipping_zipcode")
    home = (By.NAME, "delivery_home_type")
    levels = (By.NAME, "delivery_home_type")
    date = (By.NAME, "delivery_date")
    payment = (By.NAME, "payment_method")
    account = (By.NAME, "charge_account")
    parking = (By.XPATH, "(//input[@type='radio'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def Set_name(self):
        return self.driver.find_element(*Payment.name)

    def Set_Contact(self):
        return self.driver.find_element(*Payment.contact)

    def Set_constructionflag(self):
        return self.driver.find_element(*Payment.flag)

    def Set_address(self):
        return self.driver.find_element(*Payment.address)

    def Set_city(self):
        return self.driver.find_element(*Payment.city)

    def Set_state(self):
        dropdown = Select(self.driver.find_element(*Payment.state))
        return dropdown

    def Set_zipcode(self):
        return self.driver.find_element(*Payment.zipcode)

    def Set_parkingflag(self):
        return self.driver.find_element(*Payment.parking)


    def Set_home(self):
        dropdown = Select(self.driver.find_element(*Payment.home))
        return dropdown

    def Set_levels(self):
        return self.driver.find_element(*Payment.levels)

    def Set_date(self):
        return self.driver.find_element(*Payment.date)


    def Set_Payment_Method(self):
        dropdown = Select(self.driver.find_element(*Payment.payment))
        return dropdown


    def Set_Account(self):
        return self.driver.find_element(*Payment.account)











