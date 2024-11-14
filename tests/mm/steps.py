from time import sleep

import allure
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.webdriver import ActionChains

from dit.qa.constans import NEWSPAPERS
from dit.qa.pages.mm.mm_auth_page import MMAuthPage
from dit.qa.pages.mm.mm_main_page import MmMainPage

__all__ = [
    'open_auth_page',
    'sign_in',
    'open_mm_main_page',
    'open_mm_search_report',
    'set_context_query_filter',
    'set_period_filter',
    'set_authors_filter',
    'set_sources_filter',
    'set_objects_filter',
    'create_report',
    'cancel_create_report',
    'open_newspapers_section',
    'open_newspaper_pdf',
    'open_subreport',
    'close_subreport'
]


def open_auth_page(app: Application, request: FixtureRequest) -> None:
    with allure.step('Opening Auth page'):
        try:
            page = MMAuthPage(app)
            page.base_url = f'https://{request.config.option.ui_url_mm}'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'mm_auth_page')
        except Exception as e:
            screenshot_attach(app, 'auth_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = MMAuthPage(app)
            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise e

        page.submit.click()


def open_mm_main_page(app: Application) -> None:
    with allure.step('Opening MM main page'):
        try:
            MmMainPage(app).wait_for_loading()

            screenshot_attach(app, 'mm_main_page')
        except Exception as e:
            screenshot_attach(app, 'mm_main_page_error')

            raise e


def open_mm_search_report(app: Application) -> None:
    with allure.step('Opening MM search report'):
        try:
            page = MmMainPage(app)
            page.header.new_search.click()

            page.wait_for_loading_search_report()

            screenshot_attach(app, 'mm_search_report')
        except Exception as e:
            screenshot_attach(app, 'mm_search_report_error')

            raise e


def set_context_query_filter(app: Application, text: str) -> None:
    with allure.step('Setting Context query filter'):
        try:
            page = MmMainPage(app)
            page.main.search_options_bar.context_query.click()
            page.main.context_query_field.webelement.send_keys(text)

            page.wait_for_adding_context_query_filter()

            screenshot_attach(app, 'context_query_filter')
        except Exception as e:
            screenshot_attach(app, 'context_query_filter_error')

            raise e


def set_period_filter(app: Application) -> None:
    with allure.step('Setting Period filter'):
        try:
            page = MmMainPage(app)
            page.main.search_options_bar.period.click()

            page.wait_for_adding_period_filter()

            screenshot_attach(app, 'period_filter')
        except Exception as e:
            screenshot_attach(app, 'period_filter_error')

            raise e


def set_authors_filter(app: Application, authors: list) -> None:
    with allure.step('Setting Authors filter'):
        try:
            page = MmMainPage(app)
            page.main.search_options_bar.authors.click()
            page.main.authors_field.webelement.click()

            for author in authors:
                page.main.authors_field.webelement.send_keys(author)
                page.main.field_dropdown.webelement.click()

            page.wait_for_adding_authors_filter()

            screenshot_attach(app, 'authors_filter')
        except Exception as e:
            screenshot_attach(app, 'authors_filter_error')

            raise e


def set_sources_filter(app: Application, sources: list) -> None:
    with allure.step('Setting Sources filter'):
        try:
            page = MmMainPage(app)
            page.main.search_options_bar.sources.click()
            ActionChains(app.driver).scroll_to_element(page.main.search.webelement).perform()
            page.main.sources_field.webelement.click()

            for source in sources:
                page.main.sources_field.webelement.send_keys(source)
                page.main.field_dropdown.webelement.click()

            page.wait_for_adding_sources_filter()

            screenshot_attach(app, 'sources_filter')
        except Exception as e:
            screenshot_attach(app, 'sources_filter_error')

            raise e


def set_objects_filter(app: Application, text: str) -> None:
    with allure.step('Setting Objects filter'):
        try:
            page = MmMainPage(app)
            page.main.search_options_bar.objects.click()
            ActionChains(app.driver).scroll_to_element(page.main.search.webelement).perform()
            page.main.objects_field.webelement.send_keys(text)
            page.main.field_dropdown.webelement.click()

            page.wait_for_adding_objects_filter()

            screenshot_attach(app, 'objects_filter')
        except Exception as e:
            screenshot_attach(app, 'objects_filter_error')

            raise e


def create_report(app: Application) -> None:
    with allure.step('Creating Report'):
        try:
            page = MmMainPage(app)
            page.main.search.click()

            page.wait_for_create_report_error_message()

            screenshot_attach(app, 'create_report')
        except Exception as e:
            screenshot_attach(app, 'create_report_error')

            raise e


def cancel_create_report(app: Application) -> None:
    with allure.step('Canceling Creating report'):
        try:
            page = MmMainPage(app)
            page.main.cancel.click()

            page.wait_for_loading()

            screenshot_attach(app, 'cancel_create_report')
        except Exception as e:
            screenshot_attach(app, 'cancel_create_report_error')

            raise e


def open_newspapers_section(app: Application) -> None:
    with allure.step('Opening Newspapers section'):
        try:
            page = MmMainPage(app)
            page.menu.newspapers.click()

            page.wait_for_loading_newspapers_pdf()

            titles = [t.webelement.text for t in page.main.newspapers_titles]

            for newspaper in NEWSPAPERS:
                assert newspaper in titles, 'Искомой газеты нет в списке'

            screenshot_attach(app, 'newspapers_section')
        except Exception as e:
            screenshot_attach(app, 'newspapers_section_error')

            raise e


def open_newspaper_pdf(app: Application) -> None:
    with allure.step('Opening Newspapers pdf'):
        try:
            page = MmMainPage(app)
            page.main.newspapers_titles[5].click()

            page.wait_for_loading_newspapers_pdf()

            screenshot_attach(app, 'open_newspaper_pdf')
        except Exception as e:
            screenshot_attach(app, 'open_newspaper_pdf_error')

            raise e


def open_subreport(app: Application) -> None:
    with allure.step('Opening Subreport'):
        try:
            page = MmMainPage(app)
            page.create_subreport.click()

            page.wait_for_loading_subreport()

            screenshot_attach(app, 'subreport')
        except Exception as e:
            screenshot_attach(app, 'subreport_error')

            raise e


def close_subreport(app: Application) -> None:
    with allure.step('Closing Subreport'):
        try:
            page = MmMainPage(app)
            page.main.cancel.click()

            page.wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise e
