from main_page import MainPage

link_page = "https://deiceland.org/"


def test_main_page_main_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_main_link()


def test_main_page_files_upper_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_files_upper_link()


def test_main_page_cabinet_upper_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_cabinet_upper_link()


def test_main_page_donate_upper_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_donate_upper_link()


def test_main_page_begin_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_begin_link()


def test_main_page_registration_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_registration_link()


def test_main_page_files_left_side_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_files_left_side_link()


def test_main_page_security_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_security_link()


def test_main_page_rules_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_rules_link()


def test_main_page_serv30_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_serv30_link()


def test_main_page_serv51_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_serv51_link()


def test_main_page_serv1k_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_serv51_link()


def test_main_page_serv5_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_serv51_link()


def test_main_page_donate_left_side_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_donate_left_side_link()


def test_main_page_pvp(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_pvp_link()


def test_main_page_pk(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_pk_link()


def test_main_page_time(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_time_link()


def test_main_page_clans(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_clans_link()


def test_main_page_castle(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_castle_link()


def test_main_page_cabinet_left_side_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_cabinet_left_side_link()


def test_main_page_forgot_pass_link(browser_context_page):
    main_page = MainPage(browser_context_page, link_page)
    main_page.verify_and_click_forgot_pass_link()

