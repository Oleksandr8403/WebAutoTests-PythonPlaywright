from playwright.sync_api import expect
from general_page import GeneralPageLinks


class FilePage(GeneralPageLinks):
    def verify_download_client_link_on_file_page(self):
        self.goto()
        link = self.page.get_by_role("link", name="Скачати клїєнт гри - 5 Гб")
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', 'https://deiceland.org/update/deiceUA20022024.rar')

    def verify_download_patch_link_on_file_page(self):
        self.goto()
        link = self.page.get_by_role("link", name="Патч для Англійського клієнта, з укр. елементами")
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', 'https://deiceland.org/update/deiceUApatch20022024.zip')

    def verify_download_updater_link_on_file_page(self):
        self.goto()
        link = self.page.get_by_role("link", name="Апдейтер для Англійського клієнта, з укр. елементами")
        expect(link).to_be_visible()
        expect(link).to_have_attribute('href', 'https://deiceland.org/update/game_updater20022024.zip')
