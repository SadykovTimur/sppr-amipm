from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

from dit.qa.pages.mm.mm_main_page.components.search_options_bar import SearchOptionsBar

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    search_options_bar = SearchOptionsBar(tag="section")
    search = Button(xpath='//button[text()="Поиск"]')
    cancel = Button(xpath='//button[text()="Отмена"]')
    empty_content = Component(xpath='//div[text()="Добавьте фильтры, которые хотите применить"]')
    context_query_field = Component(xpath='//textarea[@placeholder="Введите слово или фразу для поиска..."]')
    articles = Components(tag='article')
    authors_field = Component(
        xpath='//h1[text()="Авторы"]/parent::div/following::input[contains(@class, "MuiInputBase-input")]'
    )
    field_dropdown = Component(tag='ul')
    filters_fields_labels = Components(css='[class*="MuiChip-label"]')
    sources_field = Component(
        xpath='//h1[text()="Источники"]/parent::div/following::input[contains(@class, "MuiInputBase-input")]'
    )
    objects_field = Component(
        xpath='//h1[text()="Обьекты"]/parent::div/following::input[contains(@class, "MuiInputBase-input")]')
    create_report_error_msg = Component(xpath='//div[text()="Пожалуйста, добавьте название отчета"]')
    newspapers_titles = Components(css='li[class*="MenuItem"]')
    frame = Component(tag='iframe')


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
