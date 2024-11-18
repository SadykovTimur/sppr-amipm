from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

__all__ = ['MmPublicationPage']


class MmPublicationPage(Page):
    loader = Component(css='[class*="LinearProgress-root"]')
    header = Component(id='ms-header')
    menu = Component(tag='aside')
    publication_content = Component(class_name='document-content')
    publication_metrics = Component(class_name='document-metrics')

    @property
    def is_loader_hidden(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.is_loader_hidden
                assert self.header.visible
                assert self.menu.visible
                assert self.publication_content.visible

                return self.publication_metrics.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Страница формы просмотра публикации не загружена')
        self.app.restore_implicitly_wait()
        self.driver.switch_to.default_content()
