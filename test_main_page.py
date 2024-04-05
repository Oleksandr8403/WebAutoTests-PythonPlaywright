from main_page import MainPage

link_page = "https://deiceland.org/"


def test_main_page_body_begin_upper_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_upper_begin_link_on_page()


def test_main_page_body_begin_lower_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_lower_begin_link_on_page()


def test_main_page_body_first_server_description(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_first_server_description()


def test_main_page_body_second_server_description(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_second_server_description()


def test_main_page_body_third_server_description(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_third_server_description()


def test_main_page_body_fourth_server_description(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_fourth_server_description()
