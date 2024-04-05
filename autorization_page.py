from playwright.sync_api import expect
from general_page import GeneralPageLinks


class AutorizPage(GeneralPageLinks):
    def check_submit_right_account_data(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testlogin")
        self.page.locator("input[name=\"login\"]").press("Tab")
        self.page.locator("input[name=\"pass\"]").fill("rightpassword")
        self.page.locator("input[name=\"keystring\"]").click()
        self.page.locator("input[name=\"keystring\"]").fill("testcode")
        self.page.get_by_role("button", name="Увійти").click()
        # expect(page.get_by_role("heading", name="Информация о аккаунте")).to_be_visible()

    def check_submit_not_right_password(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testlogin")
        self.page.locator("input[name=\"login\"]").press("Tab")
        self.page.locator("input[name=\"pass\"]").fill("failpassword")
        self.page.locator("input[name=\"keystring\"]").click()
        self.page.locator("input[name=\"keystring\"]").fill("testcode")
        self.page.get_by_role("button", name="Увійти").click()
        expect(self.page.get_by_role("heading", name="Вхід у кабінет")).to_be_visible()

    def check_submit_not_right_login(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testfaillogin")
        self.page.locator("input[name=\"login\"]").press("Tab")
        self.page.locator("input[name=\"pass\"]").fill("rightpassword")
        self.page.locator("input[name=\"keystring\"]").click()
        self.page.locator("input[name=\"keystring\"]").fill("testcode")
        self.page.get_by_role("button", name="Увійти").click()
        expect(self.page.get_by_role("heading", name="Вхід у кабінет")).to_be_visible()

    def check_submit_not_right_login_not_right_pass(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testfaillogin")
        self.page.locator("input[name=\"login\"]").press("Tab")
        self.page.locator("input[name=\"pass\"]").fill("failpassword")
        self.page.locator("input[name=\"keystring\"]").click()
        self.page.locator("input[name=\"keystring\"]").fill("testcode")
        self.page.get_by_role("button", name="Увійти").click()
        expect(self.page.get_by_role("heading", name="Вхід у кабінет")).to_be_visible()

    def check_submit_not_right_picture_code(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testlogin")
        self.page.locator("input[name=\"login\"]").press("Tab")
        self.page.locator("input[name=\"pass\"]").fill("testpassword")
        self.page.locator("input[name=\"keystring\"]").click()
        self.page.locator("input[name=\"keystring\"]").fill("failcode")
        self.page.get_by_role("button", name="Увійти").click()
        expect(self.page.get_by_role("heading", name="Вхід у кабінет")).to_be_visible()

    def check_forgot_link_is_visible(self):
        self.goto()
        expect(self.page.locator('tbody > tr:nth-child(1) > td.text > div > a')).to_be_visible()
