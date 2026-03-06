from playwright.sync_api import Page
from Pages.Login import LoginPage
from Pages.AddtoCart import CartPage


def test_add_to_cart(page: Page):
    login_page = LoginPage(page)
    add_to_cart_page = CartPage(page)

    login_page.goto_saucedemo_web()
    page.wait_for_timeout(1000)
    login_page.fill_login_form('standard_user', 'secret_sauce')
    login_page.click_login_btn()
    page.wait_for_timeout(1000)

    add_to_cart_page.click_add_to_cart_btn()
    item_price = add_to_cart_page.get_item_price()
    print(f"The price of the item is: {item_price}")