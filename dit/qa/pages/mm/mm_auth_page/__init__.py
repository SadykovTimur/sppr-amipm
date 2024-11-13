from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['MMAuthPage']


class MMAuthPage(Page):
    title = Component(
        xpath='//p[contains(text(), "Система поддержки принятия решений и ' 'управления информационными рисками")]'
    )
    login = TextField(id='login')
    password = TextField(id='password')
    remember = Button(id='remember')
    submit = Button(css='[class*="btnLogin"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.login.visible
                assert self.password.visible
                assert self.remember.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Страница ММ авторизации не загружена', timeout=40)
        self.app.restore_implicitly_wait()
