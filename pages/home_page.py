from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.add_customer_link = page.get_by_role("link", name="Add Customer")

    def click_add_customer(self):
        self.add_customer_link.click()
