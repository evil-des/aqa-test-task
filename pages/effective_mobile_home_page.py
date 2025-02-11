from playwright.sync_api import Page
from .base_page import BasePage


class EffectiveMobileHomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
