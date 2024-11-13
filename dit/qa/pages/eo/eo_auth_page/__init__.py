from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['EOAuthPage']


class EOAuthPage(Page):
    logo = Component(css='[class*="MuiBox"]')
    title = Component(xpath='//p[text()="Электронный офис"]')
    login = TextField(name='username')
    password = TextField(name='password')
    remember = Component(xpath='//span[text()="Запомнить меня"]')
    submit = Button(xpath='//button[text()="Войти"]')
    support = Button(css='[class*="MuiLink"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.title.visible
                assert self.login.visible
                assert self.password.visible
                assert self.remember.visible
                assert self.submit.visible

                return self.support.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Страница ЭО авторизации не загружена')
        self.app.restore_implicitly_wait()
