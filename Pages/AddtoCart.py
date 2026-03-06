from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = ".inventory_item_name"
        self.cart_prices = ".inventory_item_price"
        self.cart_quantity = ".cart_quantity"
        self.remove_button = "button:has-text('Remove')"
        self.checkout_btn = "#checkout"

    def get_cart_items(self):
        return self.page.locator(self.cart_items).all_inner_texts()

    def get_cart_prices(self):
        prices = self.page.locator(self.cart_prices).all_inner_texts()
        return [float(p.replace("$", "")) for p in prices]

    def get_cart_quantities(self):
        return self.page.locator(self.cart_quantity).all_inner_texts()

    def remove_first_item(self):
        self.page.locator(self.remove_button).first.click()

    def proceed_to_checkout(self):
        self.page.click(self.checkout_btn)

    def is_cart_empty(self):
        return self.page.locator(self.cart_items).count() == 0
