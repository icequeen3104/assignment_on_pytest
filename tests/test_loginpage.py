
from Pages.Login import LoginPage
import pytest


def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto_saucedemo_web()
    print("the webpage is opened")
    page.wait_for_timeout(1000)
    login_page.fill_login_form('standard_user', 'secret_sauce')
    print("Filled the login form")
    login_page.click_login_btn()
    print("clicked login btn")