from general_page import GeneralPageLinks


class RegistrationPage(GeneralPageLinks):
    def reg_new_test_account(self):
        self.goto()
        self.page.locator("input[name=\"login\"]").click()
        self.page.locator("input[name=\"login\"]").fill("testaccount")
        self.page.locator("input[name=\"pass1\"]").click()
        self.page.locator("input[name=\"pass1\"]").fill("testpassword")
        self.page.locator("input[name=\"pass2\"]").click()
        self.page.locator("input[name=\"pass2\"]").fill("testpassword")
        self.page.get_by_placeholder("Не обов'язково").click()
        self.page.get_by_placeholder("Не обов'язково").fill("testmail@testmail")
        self.page.locator("input[name=\"keystring\"]").click()
        self.page.locator("input[name=\"keystring\"]").fill("testcode")
        self.page.get_by_role("button", name="Реєстрація").click()
        assert True, ('In this place we should write assertion after registration new account that registration was '
                      'successful')
