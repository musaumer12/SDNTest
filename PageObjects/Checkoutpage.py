from selenium.webdriver.common.by import By


class Checkout:

    cart = (By.XPATH, "//div[@class='header_icon cart_icon']")
    review = (By.XPATH, "//a[@href='/cart']")
    proceed = (By.XPATH, "//a[@href='/checkout']")





    def __init__(self, driver):
        self.driver = driver

    def Get_cart(self):
        return self.driver.find_element(*Checkout.cart)

    def Get_review(self):
        return self.driver.find_element(*Checkout.review)

    def Get_proceed(self):
        return self.driver.find_element(*Checkout.proceed)