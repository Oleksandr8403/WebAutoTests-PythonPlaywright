from registration_page import RegistrationPage

link_page = 'https://deiceland.org/reg'


def test_reg_new_acc(browser_context_page):
    reg_page = RegistrationPage(browser_context_page, link_page)
    reg_page.reg_new_test_account()
