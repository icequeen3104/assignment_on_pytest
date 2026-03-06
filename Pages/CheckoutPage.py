from playwright.sync_api import Page

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_btn = "#continue"
        self.finish_btn = "#finish"

        self.summary_items = ".inventory_item_name"
        self.item_total = ".summary_subtotal_label"
        self.tax = ".summary_tax_label"
        self.total = ".summary_total_label"

        self.confirm_msg = ".complete-header"
        self.order_number = ".complete-text"

    def fill_shipping_details(self):
        self.page.fill(self.first_name, "Saujanya")
        self.page.fill(self.last_name, "Srivastava")
        self.page.fill(self.postal_code, "167843")
        self.page.click(self.continue_btn)

    def get_summary_items(self):
        return self.page.locator(self.summary_items).all_inner_texts()

    def get_item_total(self):
        text = self.page.locator(self.item_total).inner_text()
        return float(text.replace("Item total: $", ""))

    def get_tax(self):
        text = self.page.locator(self.tax).inner_text()
        return float(text.replace("Tax: $", ""))

    def get_total(self):
        text = self.page.locator(self.total).inner_text()
        return float(text.replace("Total: $", ""))

    def complete_order(self):
        self.page.click(self.finish_btn)

    def get_confirmation_message(self):
        return self.page.locator(self.confirm_msg).inner_text()

    def get_order_text(self):
        return self.page.locator(self.order_number).inner_text()
