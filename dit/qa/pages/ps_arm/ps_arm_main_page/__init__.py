from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.ps_arm.ps_arm_main_page.components.header import Header
from dit.qa.pages.ps_arm.ps_arm_main_page.components.user_chart import UserChart

__all__ = ['PsArmMainPage']


class PsArmMainPage(Page):
    header = Header(tag='header')
    common_statistics = Component(xpath='//div[text()="Общая статистика"]')
    statistics_by_users = Component(xpath='//div[text()="Статистика по пользователям"]')
    doc_menu = Component(class_name='document-folder-tree')
    doc_content = Component(class_name='document-list')
    footer = Component(class_name='layout-footer')
    charts = Components(class_name='highcharts-background')
    date_picker = Button(css='[class*="ant-picker ant-picker-range"]')
    start_date = Button(css='[class*="ant-picker-cell ant-picker-cell-start"]')
    users_chart = UserChart(xpath='.//*[text()="Количество уникальных посетителей"]/parent::*')
    statistics_by_users_title = Component(xpath='//div[text()="Входы"]')
    user_select = Component(class_name='dropdown')
    reset = Button(xpath='//div[text()="Сбросить"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.visible
                assert self.doc_menu.visible
                assert self.doc_content.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Главная страница ПС_АРМ не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_statistics(self) -> None:
        def condition() -> bool:
            try:
                assert self.common_statistics.visible
                assert self.statistics_by_users.visible
                assert len(self.users_chart.points) == 1

                return self.charts[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Раздел "Статистика" не загружен')
        self.app.restore_implicitly_wait()

    def wait_for_loading_statistics_after_setting_date(self) -> None:
        def condition() -> bool:
            try:
                assert len(self.users_chart.points) > 1

                return self.charts[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Раздел "Статистика" за период не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_statistics_by_users(self) -> None:
        def condition() -> bool:
            try:
                assert self.statistics_by_users_title.visible
                assert self.user_select.visible
                assert self.reset.visible

                return self.charts[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Раздел "Статистика по пользователям" не загружена')
        self.app.restore_implicitly_wait()
