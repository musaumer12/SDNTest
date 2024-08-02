from selenium import webdriver
import time
import pytest

from PageObjects.InventoryPage import Inventory
from PageObjects.SignInpage import Signin
from testdata.SigninData import SigninData
from testdata.productData import ProductInfo


@pytest.mark.usefixtures("setup")
class Test_Signin():

    def test_signin(self, GetData, Getinfo):
        signin = Signin(self.driver)
        inventory = Inventory(self.driver)
        signin.Get_user().send_keys(GetData["Username"])
        signin.Get_pass().send_keys(GetData["Password"])
        signin.Get_login().click()
        time.sleep(5)
        inventory.Get_inventory().click()
        inventory.Get_Proudcts().click()
        time.sleep(5)
        inventory.New_Product().click()
        inventory.Set_Product_name().send_keys(Getinfo["ProductName"])
        inventory.Set_SKU().send_keys(Getinfo["SKU"])
        inventory.Set_Category().select_by_value("78")
        time.sleep(3)
        inventory.Set_Yuxi().select_by_value("109")
        inventory.Set_SalePrice().send_keys(Getinfo["Saleprice"])
        inventory.Set_Cost().send_keys(Getinfo["CostofGoods"])
        inventory.Set_Rent().send_keys(Getinfo["Rent"])
        inventory.Rentable().click()
        inventory.Set_Description().send_keys(Getinfo["Description"])
        inventory.Get_image().send_keys(Getinfo["Image_URL"])
        inventory.Save_button().click()
        time.sleep(5)



    @pytest.fixture(params= SigninData.test_signin_data)
    def GetData(self, request):
        return request.param

    @pytest.fixture(params= ProductInfo.pdt)
    def Getinfo(self, request):
        return request.param
