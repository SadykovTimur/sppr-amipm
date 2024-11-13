from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.eo.eo_main_page.componetns.header import Header

__all__ = ['EOMainPage']


class EOMainPage(Page):
    header = Header(tag='header')
    calendars = Components(css='[class*="DateCalendar-root"]')
    main = Component(css='[class*="media-screen"]')
    ok = Button(xpath='//button[text()="Ок"]')

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
