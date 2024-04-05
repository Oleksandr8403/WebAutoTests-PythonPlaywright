from playwright.sync_api import expect
from general_page import GeneralPageLinks


class BeginPage(GeneralPageLinks):
    def verify_download_client_link_on_begin_page(self):
        self.goto()
        link = self.page.get_by_role("link", name="Завантажити гру", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', 'https://deiceland.org/update/deiceUA20022024.rar')

    def verify_upper_reg_link_on_page(self):
        self.goto()
        link = self.page.get_by_role("link", name="Зареєструватися тут")
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=reg')

    def verify_lower_reg_link_on_page(self):
        self.goto()
        link = self.page.get_by_role("link", name="ЗАРЕЄСТРУВАТИСЯ", exact=True)
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=reg')

    def verify_file_link_on_page(self):
        self.goto()
        link = self.page.locator("p").filter(has_text="Якщо Ви раніше грали в").get_by_role("link")
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', '/index.php?act=file')

