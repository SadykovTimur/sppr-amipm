from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from dit.qa.pages.eo.eo_main_page.components.header import Header

__all__ = ['EOMainPage']


class EOMainPage(Page):
    loader = Component(css='[class*="hKGepO"]')
    header = Header(tag='header')
    calendars = Components(css='[class*="DateCalendar-root"]')
    main = Component(css='[class*="media-screen"]')
    ok = Button(xpath='//button[text()="Ок"]')
    create_event = Button(xpath='//button[text()="Создать событие"]')
    events_textarea = Components(css='[class*="event-harness"] textarea')
    events_cell = Component(css='[class*="event-harness"]')
    time_event = Text(xpath='//div[text()="Тест"]/parent::div//child::p')
    edit = Button(xpath='//button[text()="Редактирование"]')
    files = Components(xpath='//p[contains(text(), "test_file")]')
    save = Button(xpath='//button[text()="Сохранить"]')
    close = Button(xpath='//button[text()="Закрыть"]')
    event_delete = Button(xpath='//div[text()="Удалить"]')
    modal_delete = Button(xpath='//button[text()="Удалить"]')

    @property
    def is_loader_hidden(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    @property
    def is_event_deleted(self) -> bool:
        try:
            return not self.events_cell.visible
        except NoSuchElementException:
            return True

    def activate_grid_cell(self, x: int, y: int) -> None:
        ac = ActionChains(self.driver)  # type: ignore[no-untyped-call]
        ac.move_to_element(self.create_event.webelement)  # type: ignore[no-untyped-call]
        location = self.create_event.webelement.location
        ac.move_by_offset(x - location['x'], y - location['y']).click().perform()  # type: ignore[no-untyped-call]

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.is_loader_hidden
                assert self.header.visible
                assert self.calendars[0].visible

                return self.main.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Главная страница ЭО не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_activating_event(self) -> None:
        def condition() -> bool:
            try:
                return "#b4e5b8" == self.events_textarea[0].webelement.get_attribute('bgcolor')

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Ячейка события не была активирована')
        self.app.restore_implicitly_wait()

    def wait_for_filling_in_grid_cell(self, text: str) -> None:
        def condition() -> bool:
            try:
                return text == self.events_textarea[0].webelement.text

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Ячейка события не была заполнена текстом')
        self.app.restore_implicitly_wait()

    def wait_for_saving_event(self, text: str) -> None:
        def condition() -> bool:
            try:
                return self.events_cell.webelement.text == text

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Событие не было сохранено')
        self.app.restore_implicitly_wait()

    def wait_for_uploading_files(self) -> None:
        def condition() -> bool:
            try:
                return len(self.files) == 5

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Файлы не были загружены')
        self.app.restore_implicitly_wait()

    def wait_for_deleting_event(self) -> None:
        def condition() -> bool:
            try:
                return self.is_event_deleted

            except NoSuchElementException:

                return True

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Событие не было удалено')
        self.app.restore_implicitly_wait()
