from autorization_page import AutorizPage

link_page = 'https://deiceland.org/autoriz'


def test_autorization_right_data(browser_context_page):
    autorization_page = AutorizPage(browser_context_page, link_page)
    autorization_page.check_submit_right_account_data()


def test_autorization_not_right_password(browser_context_page):
    autorization_page = AutorizPage(browser_context_page, link_page)
    autorization_page.check_submit_not_right_password()


def test_autorization_not_right_login(browser_context_page):
    autorization_page = AutorizPage(browser_context_page, link_page)
    autorization_page.check_submit_not_right_login()


def test_autorization_not_right_login_not_right_pass(browser_context_page):
    autorization_page = AutorizPage(browser_context_page, link_page)
    autorization_page.check_submit_not_right_login_not_right_pass()


def test_autorization_not_right_picture_code(browser_context_page):
    autorization_page = AutorizPage(browser_context_page, link_page)
    autorization_page.check_submit_not_right_picture_code()


def test_visible_forgot_link(browser_context_page):
    autorization_page = AutorizPage(browser_context_page, link_page)
    autorization_page.check_forgot_link_is_visible()

