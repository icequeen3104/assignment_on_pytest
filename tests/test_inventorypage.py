from Pages.Login import LoginPage
from Pages.InventoryPage import InventoryPage

def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com")

    login = LoginPage(page)
    login.fill_login_form("standard_user", "secret_sauce")
    login.click_login_btn()
    #login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_item_to_cart("Sauce Labs Bike Light")

    assert "inventory" in page.url