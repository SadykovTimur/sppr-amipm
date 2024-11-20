import allure
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach

from dit.qa.pages.ps_arm.ps_arm_auth_page import PsArmAuthPage
from dit.qa.pages.ps_arm.ps_arm_main_page import PsArmMainPage

__all__ = [
    'open_auth_page',
    'sign_in',
    'open_main_page',
    'open_statistics',
    'set_statistics_date',
    'check_statistics_by_users',
]


def open_auth_page(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Auth page'):
        try:
            page = PsArmAuthPage(app)
            page.base_url = f'https://{request.config.option.ui_url_ps_arm}'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'auth_page')
        except Exception as e:
            screenshot_attach(app, 'auth_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = PsArmAuthPage(app)
            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise e

        page.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            PsArmMainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise e


def open_statistics(app: Application) -> None:
    with allure.step('Opening Statistics'):
        try:
            page = PsArmMainPage(app)
            page.header.statistics.click()

            page.wait_for_loading_statistics()

            screenshot_attach(app, 'statistics')
        except Exception as e:
            screenshot_attach(app, 'statistics_error')

            raise e


def set_statistics_date(app: Application) -> None:
    with allure.step('Setting Statistics date'):
        try:
            page = PsArmMainPage(app)
            page.date_picker.click()
            page.start_date.click()

            page.wait_for_loading_statistics_after_setting_date()

            screenshot_attach(app, 'statistics_date')
        except Exception as e:
            screenshot_attach(app, 'statistics_date_error')

            raise e


def check_statistics_by_users(app: Application) -> None:
    with allure.step('Checking Statistics by users'):
        try:
            page = PsArmMainPage(app)
            page.statistics_by_users.webelement.click()

            page.wait_for_loading_statistics_by_users()

            screenshot_attach(app, 'statistics_by_users')
        except Exception as e:
            screenshot_attach(app, 'statistics_by_users_error')

            raise e
