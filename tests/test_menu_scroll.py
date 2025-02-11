import pytest

from pages.effective_mobile_home_page import EffectiveMobileHomePage
from settings import settings


class TestMenuScroll:
    def test_menu_scroll(
        self,
        effective_mobile_home_page: EffectiveMobileHomePage,
    ):
        effective_mobile_home_page.visit(settings.BASE_URL)
        effective_mobile_home_page.navbar.scroll_to_about()
        effective_mobile_home_page.navbar.scroll_to_services()
        effective_mobile_home_page.navbar.scroll_to_projects()
        effective_mobile_home_page.navbar.scroll_to_reviews()
        effective_mobile_home_page.navbar.scroll_to_contacts()
        effective_mobile_home_page.navbar.scroll_to_choose_specialist()
