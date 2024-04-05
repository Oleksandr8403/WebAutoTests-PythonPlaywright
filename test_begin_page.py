from begin_page import BeginPage

link_page = "https://deiceland.org/begin"


def test_begin_page_check_body_download_link(browser_context_page):
    begin_page = BeginPage(browser_context_page, link_page)
    begin_page.verify_download_client_link_on_begin_page()


def test_begin_page_check_body_upper_reg_link(browser_context_page):
    begin_page = BeginPage(browser_context_page, link_page)
    begin_page.verify_upper_reg_link_on_page()


def test_begin_page_check_body_lower_reg_link(browser_context_page):
    begin_page = BeginPage(browser_context_page, link_page)
    begin_page.verify_lower_reg_link_on_page()


def test_begin_page_check_body_file_link(browser_context_page):
    begin_page = BeginPage(browser_context_page, link_page)
    begin_page.verify_file_link_on_page()


