
class CustomerPage:

    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("#fname")
        self.last_name = page.locator("#lname")
        self.email = page.locator("#email")
        self.addr = page.locator("[name='addr']")
        self.phno = page.locator("#telephoneno")
        self.submit_button = page.locator("[name='submit']")

    def fill_form(self, data):
        self.first_name.fill(data["fname"])
        self.last_name.fill(data["lname"])
        self.email.fill(data["email"])
        self.addr.fill(data["addr"])
        self.phno.fill(data["phno"])

    def submit_form(self):
        self.submit_button.click()
