from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from dit.qa.pages.eo.eo_main_page.components.header import Header


__all__ = ['EOMainPage']


class EOMainPage(Page):
    header = Header(tag='header')
    calendars = Components(css='[class*="DateCalendar-root"]')
    main = Component(css='[class*="media-screen"]')
    ok = Button(xpath='//button[text()="Ок"]')
    create_event = Button(xpath='//button[text()="Создать событие"]')
    events = Components(css='[class*="event-harness"] textarea')

    def activate_grid_cell(self, x: int, y: int) -> None:
        ac = ActionChains(self.driver)  # type: ignore[no-untyped-call]
        ac.move_to_element(self.create_event.webelement)  # type: ignore[no-untyped-call]
        location = self.create_event.webelement.location
        ac.move_by_offset(x - location['x'], y - location['y']).click().perform()  # type: ignore[no-untyped-call]

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
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
                return "#b4e5b8" == self.events[0].webelement.get_attribute('bgcolor')

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Ячейка события не была активирована')
        self.app.restore_implicitly_wait()

    def wait_for_filling_in_grid_cell(self, text: str) -> None:
        def condition() -> bool:
            try:
                return text == self.events[0].webelement.text

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Ячейка события не была заполнена текстом')
        self.app.restore_implicitly_wait()
