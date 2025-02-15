import os

import allure
from _pytest.fixtures import FixtureRequest
from coms.qa.core.helpers import wait_for
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.webdriver import ActionChains, Keys

from dit.qa.api.upload import get_event_materials_id, save_file, upload
from dit.qa.helpers import filter_logs
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
    'open_event',
    'upload_files',
    'delete_event',
]


def open_auth_page(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening EO Auth page'):
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

            screenshot_attach(app, 'grid_cell')
        except Exception as e:
            screenshot_attach(app, 'grid_cell_error')

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

            screenshot_attach(app, 'event_by_enter')
        except Exception as e:
            screenshot_attach(app, 'event_by_enter_error')

            raise e


def editing_grid_cell(app: Application, text: str) -> None:
    with allure.step('Editing grid cell'):
        try:
            page = EOMainPage(app)
            page.events_cell.webelement.click()
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
            ActionChains(app.driver).drag_and_drop_by_offset(  # type: ignore[no-untyped-call]
                page.events_cell.webelement, x_coord, y_coord
            ).perform()

            page.wait_for_saving_event(text)

            screenshot_attach(app, 'move_event_grid_cell')
        except Exception as e:
            screenshot_attach(app, 'move_event_grid_cell_error')

            raise e


def open_event(app: Application) -> None:
    with allure.step('Opening Event'):
        try:
            page = EOMainPage(app)
            ActionChains(app.driver).double_click(  # type: ignore[no-untyped-call]
                page.events_cell.webelement
            ).perform()

            page.edit.click()

            screenshot_attach(app, 'open_event')
        except Exception as e:
            screenshot_attach(app, 'open_event_error')

            raise e


def upload_files(app: Application) -> None:
    with allure.step('Uploading Files in event'):
        try:
            page = EOMainPage(app)
            token = wait_message_in_logs(app, 'My')
            temp_file_ids = []
            file_names = []
            materials_id = get_event_materials_id(token)

            for number in range(1, 6):
                temp_file_id = upload(
                    'https://office.mos.ru/api/new/Document/Upload',
                    token,
                    f"{os.getcwd()}/test_files/test_file{number}.txt",
                )
                temp_file_ids.append(temp_file_id)
                file_names.append(f"test_file{number}.txt")

            save_file(token, temp_file_ids, materials_id, file_names)

            app.driver.refresh()

            page.wait_for_uploading_files()

            screenshot_attach(app, 'upload_files')
        except Exception as e:
            screenshot_attach(app, 'upload_files_error')

            raise e

        page.close.click()


def delete_event(app: Application) -> None:
    with allure.step('Deleting Event'):
        try:
            page = EOMainPage(app)
            ActionChains(app.driver).context_click(  # type: ignore[no-untyped-call]
                page.events_cell.webelement
            ).perform()

            page.event_delete.click()
            page.modal_delete.click()

            page.wait_for_deleting_event()

            screenshot_attach(app, 'delete_event')
        except Exception as e:
            screenshot_attach(app, 'delete_event_error')

            raise e


def wait_message_in_logs(app: Application, url: str) -> str:
    def condition() -> bool:
        try:
            logs = app.driver.get_log('performance')
            f_logs = filter_logs(logs, 'Network.requestWillBeSentExtraInfo', url)

            assert f_logs
            return f_logs[0]['message']['params']['headers']['authorization']

        except (IndexError, AssertionError):

            return False

    token = wait_for(condition, msg=f'Запрос {url} не был получен')

    return token
