from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['SearchOptionsBar']


class SearchOptionsBarWrapper(ComponentWrapper):
    context_query = Button(xpath='//span[text()="Контекстный запрос"]')
    period = Button(xpath='//span[text()="Период"]')
    authors = Button(xpath='//span[text()="Авторы"]')
    sources = Button(xpath='//span[text()="Источники"]/parent::div[contains(@class, "soysii")]')
    objects = Button(xpath='//span[text()="Обьекты"]/parent::div[contains(@class, "soysii")]')


class SearchOptionsBar(Component):
    def __get__(self, instance, owner) -> SearchOptionsBarWrapper:
        return SearchOptionsBarWrapper(instance.app, self.find(instance), self._locator)
