from selenium import webdriver
import time
import pytest

from PageObjects.Checkoutpage import Checkout
from PageObjects.InventoryPage import Resolved_Items
from PageObjects.PaymentPage import Payment
from PageObjects.SignInpage import Resolved_signin
from testdata.ProjectData import ProjectData
from testdata.SigninData import SigninData


@pytest.mark.usefixtures("Resolved_setup")
class Test_making_project:

    def test_making_project1(self, Get_Data, Get_ProjectData):
        login = Resolved_signin(self.driver)
        inventory = Resolved_Items(self.driver)
        payment = Payment(self.driver)
        cart = Checkout(self.driver)
        login.Get_inventory().click()
        login.Get_Email().send_keys(Get_Data["Email"])
        login.Get_password().send_keys(Get_Data["Pass"])
        login.Get_Login().click()
        inventory.Get_item().click()
        inventory.Get_room().select_by_value("17")
        inventory.Rent_item().click()
        success_message = inventory.Get_message().text
        assert "added to cart" in success_message, "item already added to Cart"
        time.sleep(3)
        cart.Get_cart().click()
        cart.Get_review().click()
        cart.Get_proceed().click()
        payment.Set_name().send_keys(Get_ProjectData["ProjectName"])
        payment.Set_Contact().send_keys(Get_ProjectData["Contact"])
        payment.Set_constructionflag().click()
        payment.Set_address().send_keys(Get_ProjectData["Address"])
        payment.Set_city().send_keys(Get_ProjectData["City"])
        payment.Set_state().select_by_value("WA")
        payment.Set_zipcode().send_keys(Get_ProjectData["Zipcode"])
        payment.Set_parkingflag().click()
        payment.Set_home().select_by_value("house")
        payment.Set_levels().send_keys(Get_ProjectData["Units"])
        payment.Set_date().send_keys(Get_ProjectData["Date"])
        payment.Set_Payment_Method().select_by_value("charge_account")
        payment.Set_Account().send_keys(Get_ProjectData["Account"])
        time.sleep(5)




    @pytest.fixture(params= SigninData.test_resolved_signin)
    def Get_Data(self, request):
        return request.param

    @pytest.fixture(params= ProjectData.Project_Detail)
    def Get_ProjectData(self, request):
        return request.param

