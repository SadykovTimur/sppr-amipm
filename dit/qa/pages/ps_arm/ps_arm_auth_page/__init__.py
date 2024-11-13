from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['PsArmAuthPage']


class PsArmAuthPage(Page):
    logo = Component(class_name='form-body')
    login = TextField(id='Login')
    password = TextField(name='Password')
    remember = Component(tag='label')
    submit = Button(id='LoginButton')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.login.visible
                assert self.password.visible
                assert self.remember.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Страница ПС_АРМ авторизации не загружена')
        self.app.restore_implicitly_wait()
