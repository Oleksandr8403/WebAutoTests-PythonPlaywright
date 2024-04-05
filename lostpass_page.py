from playwright.sync_api import expect
from general_page import GeneralPageLinks


class LostpassPage(GeneralPageLinks):
    def check_submit_right_data(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testlogin1")
        self.page.locator("input[name=\"login\"]").press("Tab")
        self.page.locator("input[name=\"mail\"]").fill("testmail@test.mail")
        self.page.get_by_role("button", name="Отправить запрос").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("newpassword")
        self.page.get_by_role("button", name="Отправить запрос").click()
        # in this place we need add right assertion that was sent mail
        assert True

    def check_submit_not_right_mail(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testlogin1")
        self.page.locator("input[name=\"mail\"]").click()
        self.page.locator("input[name=\"mail\"]").fill("fail@test.mail")
        self.page.get_by_role("button", name="Отправить запрос").click()
        expect(self.page.get_by_text("Комбинации Логин/Почта не существует")).to_be_visible()

    def check_submit_not_right_login(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testfaillogin")
        self.page.locator("input[name=\"mail\"]").click()
        self.page.locator("input[name=\"mail\"]").fill("testmail@test.mail")
        self.page.get_by_role("button", name="Отправить запрос").click()
        expect(self.page.get_by_text("Комбинации Логин/Почта не существует")).to_be_visible()
