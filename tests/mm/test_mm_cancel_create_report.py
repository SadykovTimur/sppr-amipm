from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from dit.qa.constans import AUTHORS, SOURCES
from tests.mm.steps import (
    cancel_create_report,
    create_report,
    open_auth_page,
    open_mm_main_page,
    open_mm_search_report,
    set_authors_filter,
    set_context_query_filter,
    set_objects_filter,
    set_period_filter,
    set_sources_filter,
    sign_in,
)


@allure.epic('SPPR AMIPM')
@allure.title('Отмена создания отчета')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_mm_cancel_create_report(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_auth_page(app, request)

    sign_in(app, request.config.option.username_mm, request.config.option.password_mm)
    open_mm_main_page(app)

    open_mm_search_report(app)

    set_context_query_filter(app, 'Собянин & Москва')
    set_period_filter(app)
    set_authors_filter(app, AUTHORS)
    set_sources_filter(app, SOURCES)
    set_objects_filter(app, 'Российская Федерация')

    create_report(app)
    cancel_create_report(app)
