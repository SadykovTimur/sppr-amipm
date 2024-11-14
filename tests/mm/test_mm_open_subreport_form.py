from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.mm.steps import open_auth_page, open_mm_main_page, sign_in, open_subreport


@allure.epic('SPPR AMIPM')
@allure.title('Открытие формы создания подотчета')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_mm_open_subreport_form(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_auth_page(app, request)

    sign_in(app, request.config.option.username_mm, request.config.option.password_mm)
    open_mm_main_page(app)

    open_subreport(app)
