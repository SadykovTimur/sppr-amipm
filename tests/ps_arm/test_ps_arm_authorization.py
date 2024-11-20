from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.ps_arm.steps import open_auth_page, open_main_page, sign_in


@allure.epic('SPPR AMIPM')
@allure.title('Авторизация пользователя ПС АРМ')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_ps_arm_authorization(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_auth_page(app, request)

    sign_in(app, request.config.option.username_ps_arm, request.config.option.password_ps_arm)
    open_main_page(app)
