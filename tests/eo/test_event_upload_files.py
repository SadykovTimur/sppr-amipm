from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.eo.steps import (
    click_grid_cell,
    create_event,
    delete_event,
    fill_in_grid_cell,
    open_auth_page,
    open_eo_main_page,
    open_event,
    sign_in,
)


@allure.epic('SPPR AMIPM')
@allure.title('Загрузка материалов в событие')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_event_upload_files(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_auth_page(app, request)

    sign_in(app, request.config.option.username_eo, request.config.option.password_eo)
    open_eo_main_page(app)

    # click_grid_cell(app, 990, 260)
    # fill_in_grid_cell(app, 'Тест')
    # create_event(app, '09:30\nТест')

    open_event(app)

    # delete_event(app)
