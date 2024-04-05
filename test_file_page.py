from file_page import FilePage

link_page = "https://deiceland.org/file"


def test_file_page_check_download_client_link(browser_context_page):
    file_page = FilePage(browser_context_page, link_page)
    file_page.verify_download_client_link_on_file_page()


def test_file_page_check_download_patch_link(browser_context_page):
    file_page = FilePage(browser_context_page, link_page)
    file_page.verify_download_patch_link_on_file_page()


def test_file_page_check_download_updater_link(browser_context_page):
    file_page = FilePage(browser_context_page, link_page)
    file_page.verify_download_patch_link_on_file_page()

