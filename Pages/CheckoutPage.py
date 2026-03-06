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
        self.summary_total = ".summary_total_label"
        self.confirm_msg = ".complete-header"

    def fill_shipping_details(self):
        self.page.fill(self.first_name, "Saujanya")
        self.page.fill(self.last_name, "Srivastava")
        self.page.fill(self.postal_code, "167843")
        self.page.click(self.continue_btn)

    def get_summary_items(self):
        return self.page.locator(self.summary_items).all_inner_texts()

    def get_total_amount(self):
        text = self.page.locator(self.summary_total).inner_text()
        return float(text.replace("Total: $", ""))

    def complete_order(self):
        self.page.click(self.finish_btn)

    def get_confirmation_message(self):
        return self.page.locator(self.confirm_msg).inner_text()