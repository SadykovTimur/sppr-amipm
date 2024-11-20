from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.mm.mm_main_page.components.header import Header
from dit.qa.pages.mm.mm_main_page.components.main import Main
from dit.qa.pages.mm.mm_main_page.components.menu import Menu

__all__ = ['MmMainPage']


class MmMainPage(Page):
    loader = Component(css='[class*="LinearProgress-root"]')
    header = Header(id='ms-header')
    menu = Menu(tag='aside')
    main = Main(tag='main')
    pdf = Component(css='[type="application/pdf"]')
    content_pdf = Components(tag='viewer-thumbnail')
    title = Text(id='ms-sub-header-top')
    report_name = TextField(xpath='//label[text()="Название отчета"]/following::div/child::input')
    create_subreport = Button(xpath='//button[text()="Создать подотчет"]')
    pagination = Components(css='[class*="PaginationItem-page"]')

    @property
    def is_loader_hidden(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.is_loader_hidden
                assert self.header.visible
                assert self.menu.visible

                return self.main.articles[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Главная страница АРМ Аналитика не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_search_report(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == "Создание поискового отчета"
                assert self.report_name.visible
                assert self.main.search_options_bar.visible
                assert self.main.search.visible
                assert self.main.cancel.visible

                return self.main.empty_content.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Форма создания поискового отчета не открыта')
        self.app.restore_implicitly_wait()

    def wait_for_adding_context_query_filter(self) -> None:
        def condition() -> bool:
            try:
                return self.main.context_query_field.webelement.text == 'Собянин & Москва'

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Фильтр "Контекстный запрос" не был заполнен')
        self.app.restore_implicitly_wait()

    def wait_for_adding_period_filter(self) -> None:
        def condition() -> bool:
            try:
                return "Период" in self.main.articles[1].webelement.text

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Фильтр "Период" не был заполнен')
        self.app.restore_implicitly_wait()

    def wait_for_adding_authors_filter(self) -> None:
        def condition() -> bool:
            try:
                return len(self.main.filters_fields_labels) == 2

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Фильтр "Авторы" не был заполнен')
        self.app.restore_implicitly_wait()

    def wait_for_adding_sources_filter(self) -> None:
        def condition() -> bool:
            try:
                return len(self.main.filters_fields_labels) == 6

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Фильтр "Источники" не был заполнен')
        self.app.restore_implicitly_wait()

    def wait_for_adding_objects_filter(self) -> None:
        def condition() -> bool:
            try:
                return len(self.main.filters_fields_labels) == 7

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Фильтр "Объекты" не был заполнен')
        self.app.restore_implicitly_wait()

    def wait_for_create_report_error_message(self) -> None:
        def condition() -> bool:
            try:
                return self.main.create_report_error_msg.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Уведомление при попытке создать отчет без названия не было отображено')
        self.app.restore_implicitly_wait()

    def wait_for_loading_newspapers_pdf(self) -> None:
        self.driver.switch_to.frame(self.main.frame.webelement)

        def condition() -> bool:
            try:
                assert self.is_loader_hidden

                return self.pdf.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Газета в блоке PDF-документа не загружена')
        self.app.restore_implicitly_wait()
        self.driver.switch_to.default_content()

    def wait_for_loading_subreport(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == "Создание подотчета"
                assert self.main.articles[0].visible
                assert self.main.search_options_bar.visible
                assert self.main.search.visible

                return self.main.cancel.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Форма создания подотчета не загружена')
        self.app.restore_implicitly_wait()
        self.driver.switch_to.default_content()
