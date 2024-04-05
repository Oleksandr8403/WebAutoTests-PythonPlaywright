from playwright.sync_api import expect
from general_page import GeneralPageLinks


class StatisticsPages(GeneralPageLinks):
    # goto pvp statistics
    def goto_pvp_x51(self):
        self.page.goto(self.link_sait + 'pvp-x51')

    def goto_pvp_x30(self):
        self.page.goto(self.link_sait + 'pvp-x30')

    def goto_pvp_x1001(self):
        self.page.goto(self.link_sait + 'pvp-x1001')

    def goto_pvp_x5(self):
        self.page.goto(self.link_sait + 'pvp-x5')

    # goto pk statistics
    def goto_pk_x51(self):
        self.page.goto(self.link_sait + 'pk-x51')

    def goto_pk_x30(self):
        self.page.goto(self.link_sait + 'pk-x30')

    def goto_pk_x1001(self):
        self.page.goto(self.link_sait + 'pk-x1001')

    def goto_pk_x5(self):
        self.page.goto(self.link_sait + 'pk-x5')

    # goto time statistics
    def goto_time_x51(self):
        self.page.goto(self.link_sait + 'time-x51')

    def goto_time_x30(self):
        self.page.goto(self.link_sait + 'time-x30')

    def goto_time_x1001(self):
        self.page.goto(self.link_sait + 'time-x1001')

    def goto_time_x5(self):
        self.page.goto(self.link_sait + 'time-x5')

    # goto clans statistics
    def goto_clans_x51(self):
        self.page.goto(self.link_sait + 'clans-x51')

    def goto_clans_x30(self):
        self.page.goto(self.link_sait + 'clans-x30')

    def goto_clans_x1001(self):
        self.page.goto(self.link_sait + 'clans-x1001')

    def goto_clans_x5(self):
        self.page.goto(self.link_sait + 'clans-x5')

    # goto castle statistics
    def goto_castle_x51(self):
        self.page.goto(self.link_sait + 'castle-x51')

    def goto_castle_x30(self):
        self.page.goto(self.link_sait + 'castle-x30')

    def goto_castle_x1001(self):
        self.page.goto(self.link_sait + 'castle-x1001')

    def goto_castle_x5(self):
        self.page.goto(self.link_sait + 'castle-x5')

    # pvp statistics
    def verify_statistics_pvp_x51(self):
        self.goto_pvp_x51()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_pvp_x30(self):
        self.goto_pvp_x30()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_pvp_x1001(self):
        self.goto_pvp_x1001()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_pvp_x5(self):
        self.goto_pvp_x5()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    # pk statistics
    def verify_statistics_pk_x51(self):
        self.goto_pk_x51()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_pk_x30(self):
        self.goto_pk_x30()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_pk_x1001(self):
        self.goto_pk_x1001()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_pk_x5(self):
        self.goto_pk_x5()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    # time statistics
    def verify_statistics_time_x51(self):
        self.goto_time_x51()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_time_x30(self):
        self.goto_time_x30()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_time_x1001(self):
        self.goto_time_x1001()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_time_x5(self):
        self.goto_time_x5()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    # clans statistics
    def verify_statistics_clans_x51(self):
        self.goto_clans_x51()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_clans_x30(self):
        self.goto_clans_x30()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_clans_x1001(self):
        self.goto_clans_x1001()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    def verify_statistics_clans_x5(self):
        self.goto_clans_x5()
        link = self.page.locator('table.top > tbody > tr:nth-child(2)')
        expect(link).to_be_visible()

    # castle statistics
    def verify_statistics_castle_x51(self):
        self.goto_castle_x51()
        link = self.page.locator("img:nth-child(7)")
        expect(link).to_be_visible()

    def verify_statistics_castle_x30(self):
        self.goto_castle_x30()
        link = self.page.locator("img:nth-child(7)")
        expect(link).to_be_visible()

    def verify_statistics_castle_x1001(self):
        self.goto_castle_x1001()
        link = self.page.locator("img:nth-child(7)")
        expect(link).to_be_visible()

    def verify_statistics_castle_x5(self):
        self.goto_castle_x5()
        link = self.page.locator("img:nth-child(7)")
        expect(link).to_be_visible()

