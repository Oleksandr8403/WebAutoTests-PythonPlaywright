from lostpass_page import LostpassPage

link_page = 'https://deiceland.org/lostpass'


def test_losstpass_right_data(browser_context_page):
    lostpass_page = LostpassPage(browser_context_page, link_page)
    lostpass_page.check_submit_right_data()


def test_losstpass_not_right_login(browser_context_page):
    lostpass_page = LostpassPage(browser_context_page, link_page)
    lostpass_page.check_submit_not_right_login()


def test_losstpass_not_right_mail(browser_context_page):
    lostpass_page = LostpassPage(browser_context_page, link_page)
    lostpass_page.check_submit_not_right_mail()
