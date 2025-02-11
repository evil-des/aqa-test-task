import pytest
from playwright.sync_api import Page, sync_playwright
from pages.effective_mobile_home_page import EffectiveMobileHomePage


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=True)
        yield chromium.new_page()


@pytest.fixture(scope='function')
def effective_mobile_home_page(chromium_page: Page) -> EffectiveMobileHomePage:
    return EffectiveMobileHomePage(chromium_page)
