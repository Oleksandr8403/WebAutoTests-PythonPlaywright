from statistics_page import StatisticsPages

link_page = "https://deiceland.org/"


# tests pvp statistics
def test_pvp_x51_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_pvp_x51()


def test_pvp_x30_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_pvp_x30()


def test_pvp_x1001_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_pvp_x1001()


def test_pvp_x5_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_pvp_x5()


# tests pk statistics
def test_pk_x51_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_pk_x51()


def test_pk_x30_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_pk_x30()


def test_pk_1001_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_pk_x1001()


def test_pk_x5_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_pk_x5()


# tests time statistics
def test_time_x51_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_time_x51()


def test_time_x30_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_time_x30()


def test_time_1001_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_time_x1001()


def test_time_x5_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_time_x5()


# clans time statistics
def test_clans_x51_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_clans_x51()


def test_clans_x30_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_clans_x30()


def test_clans_1001_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_clans_x1001()


def test_clans_x5_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_clans_x5()


# castle time statistics
def test_castle_x51_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_castle_x51()


def test_castle_x30_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_castle_x30()


def test_castle_1001_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_castle_x1001()


def test_castle_x5_not_null(browser_context_page):
    statistics_page = StatisticsPages(browser_context_page, link_page)
    statistics_page.verify_statistics_castle_x5()
