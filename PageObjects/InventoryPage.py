from select import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# ****************Report Inventory Objects*********
class Inventory:

    dropdown_inventory = (By.XPATH, "//span[text()='Inventory']")
    products = (By.XPATH, "//span[text()='Products']")
    AddProduct = (By.XPATH, "//a[@class='btn btn-info pull-right']")
    name = (By.ID, "inputProductName")
    Sku = (By.ID, "inputProductSKU")
    cat_dropdown = (By.ID, "inputCategory") #inputCategory Select
    yuxi = (By.ID, "inputYUXICategory")
    sale = (By.ID, "inputSalePrice")
    cog = (By.ID, "inputSDNCost")
    rent = (By.ID, "inputRentPerMonth")
    rentable = (By.ID, "inputRentable")
    saleable = (By.ID, "inputSaleable")
    description = (By.ID, "inputLongDescription")
    image = (By.XPATH, "//input[@id='product_image']")
    save = (By.ID, "saveProductButton")


    def __init__(self, driver):
        self.driver = driver

    def Get_inventory(self):
        return self.driver.find_element(*Inventory.dropdown_inventory)

    def Get_Proudcts(self):
        return self.driver.find_element(*Inventory.products)

    def New_Product(self):
        return self.driver.find_element(*Inventory.AddProduct)

    def Set_Product_name(self):
        return self.driver.find_element(*Inventory.name)

    def Set_SKU(self):
        return self.driver.find_element(*Inventory.Sku)

    def Set_Category(self):
        dropdown = Select(self.driver.find_element(*Inventory.cat_dropdown))
        return dropdown

    def Set_Yuxi(self):
        dropdown1 = Select(self.driver.find_element(*Inventory.yuxi))
        return dropdown1

    def Set_SalePrice(self):
        return self.driver.find_element(*Inventory.sale)


    def Set_Cost(self):
        return self.driver.find_element(*Inventory.cog)

    def Set_Rent(self):
        return self.driver.find_element(*Inventory.rent)

    def Rentable(self):
        return self.driver.find_element(*Inventory.rentable)


    def Set_Description(self):
        return self.driver.find_element(*Inventory.description)


    def Get_image(self):
        return self.driver.find_element(*Inventory.image)


    def Save_button(self):
        return self.driver.find_element(*Inventory.save)

# ****************Resolved Inventory Objects*********

class Resolved_Items:

    # //ul/li/div[@class='product-name product_title'] need to use this for dynamic use
    item = (By.XPATH, "//a[text()='28734 Marie Dining Chairs   Set Of 2']")
    room = (By.ID, "room_id")
    rent = (By.XPATH, "//a[@data-intent='rent']")
    success = (By.XPATH, "//div[@class='alert alert-success']")


    def __init__(self, driver):
        self.driver = driver

    def Get_item(self):
        return self.driver.find_element(*Resolved_Items.item)

    def Get_room(self):
        dropdown = Select(self.driver.find_element(*Resolved_Items.room))
        return dropdown

    def Rent_item(self):
        return self.driver.find_element(*Resolved_Items.rent)


    def Get_message(self):
        return self.driver.find_element(*Resolved_Items.success)
