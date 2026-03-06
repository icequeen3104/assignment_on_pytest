from playwright.sync_api import Page

class LoginPage():
    def __init__(self, page: Page):
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"

    def goto_saucedemo_web(self):
        self.page.goto("https://www.saucedemo.com/")

    def fill_login_form(self, username: str, password: str):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)

    def click_login_btn(self):
        self.page.click(self.login_button)

    def login(self, username, password):
        self.fill_login_form(username, password)
        self.click_login_btn()