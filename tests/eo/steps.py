import allure
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.webdriver import ActionChains, Keys

from dit.qa.pages.eo.eo_auth_page import EOAuthPage
from dit.qa.pages.eo.eo_main_page import EOMainPage

__all__ = [
    'open_auth_page',
    'sign_in',
    'open_eo_main_page',
    'logout',
    'click_grid_cell',
    'fill_in_grid_cell',
    'create_event',
    'save_event_by_enter',
    'editing_grid_cell',
    'move_event',
]


def open_auth_page(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Auth page'):
        try:
            page = EOAuthPage(app)
            page.base_url = f'https://{request.config.option.ui_url_eo}'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'eo_auth_page')
        except Exception as e:
            screenshot_attach(app, 'eo_auth_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = EOAuthPage(app)
            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise e

        page.submit.click()


def open_eo_main_page(app: Application) -> None:
    with allure.step('Opening EO main page'):
        try:
            EOMainPage(app).wait_for_loading()

            screenshot_attach(app, 'eo_main_page')
        except Exception as e:
            screenshot_attach(app, 'eo_main_page_error')

            raise e


def logout(app: Application) -> None:
    with allure.step('Logout'):
        try:
            page = EOMainPage(app)
            page.header.logout.click()
            page.ok.click()

            EOAuthPage(app).wait_for_loading()

            screenshot_attach(app, 'logout')
        except Exception as e:
            screenshot_attach(app, 'logout_error')

            raise e


def click_grid_cell(app: Application, coord_x: int, coord_y: int) -> None:
    with allure.step('Clicking on grid cell'):
        try:
            page = EOMainPage(app)
            page.activate_grid_cell(coord_x, coord_y)

            page.wait_for_activating_event()

            screenshot_attach(app, 'grid_cell_click')
        except Exception as e:
            screenshot_attach(app, 'grid_cell_click_error')

            raise e


def fill_in_grid_cell(app: Application, text: str) -> None:
    with allure.step('Filling in grid cell'):
        try:
            page = EOMainPage(app)
            page.events_textarea[-1].webelement.send_keys(text)

            page.wait_for_filling_in_grid_cell(text)

            screenshot_attach(app, 'grid_cell_fill_in')
        except Exception as e:
            screenshot_attach(app, 'grid_cell_fill_in_error')

            raise e


def create_event(app: Application, text: str) -> None:
    with allure.step('Creating an event'):
        try:
            page = EOMainPage(app)
            page.header.webelement.click()

            page.wait_for_saving_event(text)

            screenshot_attach(app, 'event')
        except Exception as e:
            screenshot_attach(app, 'event_error')

            raise e


def save_event_by_enter(app: Application, text: str) -> None:
    with allure.step('Saving an event by enter button'):
        try:
            page = EOMainPage(app)
            page.events_textarea[-1].webelement.send_keys(Keys.ENTER)

            page.wait_for_saving_event(text)

            screenshot_attach(app, 'event')
        except Exception as e:
            screenshot_attach(app, 'event_error')

            raise e


def editing_grid_cell(app: Application, text: str) -> None:
    with allure.step('Editing grid cell'):
        try:
            page = EOMainPage(app)
            page.events_cell[-1].webelement.click()
            page.events_textarea[-1].webelement.clear()
            page.events_textarea[-1].webelement.send_keys(text)

            page.wait_for_filling_in_grid_cell(text)

            screenshot_attach(app, 'grid_cell')
        except Exception as e:
            screenshot_attach(app, 'grid_cell_error')

            raise e


def move_event(app: Application, text: str, x_coord: int, y_coord: int) -> None:
    with allure.step('Moving event to another grid cell'):
        try:
            page = EOMainPage(app)
            ActionChains(app.driver).drag_and_drop_by_offset(page.events_cell[-1].webelement, x_coord, y_coord).perform()

            page.wait_for_saving_event(text)

            screenshot_attach(app, 'grid_cell')
        except Exception as e:
            screenshot_attach(app, 'grid_cell_error')

            raise e
