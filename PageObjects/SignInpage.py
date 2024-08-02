from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class Signin:
    username = (By.ID, "username")
    password = (By.ID, "password")
    button = (By.XPATH, "//button[@class = 'btn green']")
    def __init__(self, driver):
        self.driver  = driver

    def Get_user(self):

        return self.driver.find_element(*Signin.username)
    def Get_pass(self):
        return self.driver.find_element(*Signin.password)

    def Get_login(self):
        return self.driver.find_element(*Signin.button)

class Resolved_signin:

    inventory = (By.XPATH, "//div[@class ='inventory-drop with_arrow_down']")
    email = (By.XPATH, "(//input[@id='email'])[3]")
    password = (By.XPATH, "(//input[@id='password'])[3]")
    login = (By.XPATH, "(//button[text()='LOGIN'])[2]")



    def __init__(self, driver):
        self.driver =driver

    def Get_inventory(self):
        return self.driver.find_element(*Resolved_signin.inventory)

    def Get_Email(self):
        return self.driver.find_element(*Resolved_signin.email)

    def Get_password(self):
        return self.driver.find_element(*Resolved_signin.password)

    def Get_Login(self):
        return self.driver.find_element(*Resolved_signin.login)






