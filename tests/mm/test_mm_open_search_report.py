from time import sleep
from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.mm.steps import open_auth_page, open_mm_main_page, open_mm_search_report, sign_in


@allure.epic('SPPR AMIPM')
@allure.title('Открытие формы создания отчета')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_mm_open_search_report(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_auth_page(app, request)

    sign_in(app, request.config.option.username_mm, request.config.option.password_mm)
    open_mm_main_page(app)

    open_mm_search_report(app)
