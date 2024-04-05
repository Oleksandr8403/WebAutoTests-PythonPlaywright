import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_context_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def browser_chromium():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def browser_firefox():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def browser_webkit():
    with sync_playwright() as playwright:
        browser = playwright.webkit.launch(headless=False)
        yield browser
        browser.close()
