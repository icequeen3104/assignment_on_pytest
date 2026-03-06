from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = ".shopping_cart_link"
        self.success_badge = ".shopping_cart_badge"
        self.item_description = ".inventory_item_desc"

    def add_item_to_cart(self, item_name: str):
        formatted = item_name.lower().replace(" ", "-")
        self.page.click(f"#add-to-cart-{formatted}")

    def open_cart(self):
        self.page.click(self.cart_icon)

    def get_cart_count(self):
        return self.page.locator(self.success_badge).inner_text()

    def get_item_descriptions(self):
        return self.page.locator(self.item_description).all_inner_texts()
