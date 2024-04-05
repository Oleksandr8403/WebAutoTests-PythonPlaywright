from playwright.sync_api import expect
from general_page import GeneralPageLinks


class MainPage(GeneralPageLinks):
    def verify_and_click_upper_begin_link_on_page(self):
        self.goto()
        link = self.page.get_by_role("link", name="Розпочати гру").first
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=begin')
        link.click()
        expect(self.page).to_have_url(self.link_sait + 'begin')

    def verify_and_click_lower_begin_link_on_page(self):
        self.goto()
        link = self.page.get_by_role("link", name="Розпочати гру").nth(1)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=begin')
        link.click()
        expect(self.page).to_have_url(self.link_sait + 'begin')

    def verify_and_click_first_server_description(self):
        self.goto()
        link = self.page.locator('tbody > tr:nth-child(1) > td.text > div > a:nth-child(18)')
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=serv30')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "serv30")

    def verify_and_click_second_server_description(self):
        self.goto()
        link = self.page.locator('tbody > tr:nth-child(1) > td.text > div > a:nth-child(25)')
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=serv51')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "serv51")

    def verify_and_click_third_server_description(self):
        self.goto()
        link = self.page.locator('tbody > tr:nth-child(1) > td.text > div > a:nth-child(29)')
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=serv5')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "serv5")

    def verify_and_click_fourth_server_description(self):
        self.goto()
        link = self.page.locator('tbody > tr:nth-child(1) > td.text > div > a:nth-child(33)')
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=serv1k')
        link.click()
        expect(self.page).to_have_url(self.link_sait + "serv1k")
