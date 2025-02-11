import allure
from playwright.sync_api import Page
from page_factory.link import Link
from page_factory.section import Section


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.about_link = Link(page, locator="//a[text()='[ О нас ]']", name='О нас')
        self.services_link = Link(page, locator="//a[text()='[ Услуги ]']", name='Услуги')
        self.projects_link = Link(page, locator="//a[text()='[ Проекты ]']", name='Проекты')
        self.reviews_link = Link(page, locator="//a[text()='[ Отзывы ]']", name='Отзывы')
        self.contacts_link = Link(page, locator="//a[text()='[ Контакты ]']", name='Контакты')

        self.choose_specialist_link = Link(
            page, locator="//a[text()='Выбрать специалиста']", name='Выбрать специалиста')

        self.about_section = Section(page, locator='//*[@id="rec572359627"]/div', name='О нас')
        self.services_section = Section(page, locator='//*[@id="rec572392832"]/div', name='Услуги')
        self.projects_section = Section(page, locator='//*[@id="rec572838727"]/div', name='Проекты')
        self.reviews_section = Section(page, locator='//*[@id="rec699930013"]/div', name='Отзывы')
        self.contacts_section = Section(page, locator='//*[@id="rec572455122"]/div', name='Контакты')
        self.choose_specialist_section = Section(page, locator='//*[@id="rec660927810"]', name='Выбрать специалиста')

    def _scroll_to_section(self, link: Link, section: Section):
        link.click()
        allure.attach(
            self.page.screenshot(),
            name=f'Screenshot of {section.name}',
            attachment_type=allure.attachment_type.PNG
        )
        section.should_be_visible()

    def scroll_to_about(self):
        self._scroll_to_section(self.about_link, self.about_section)

    def scroll_to_services(self):
        self._scroll_to_section(self.services_link, self.services_section)

    def scroll_to_projects(self):
        self._scroll_to_section(self.projects_link, self.projects_section)

    def scroll_to_reviews(self):
        self._scroll_to_section(self.reviews_link, self.reviews_section)

    def scroll_to_contacts(self):
        self._scroll_to_section(self.contacts_link, self.contacts_section)

    def scroll_to_choose_specialist(self):
        self._scroll_to_section(self.choose_specialist_link, self.choose_specialist_section)
