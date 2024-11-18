from typing import List

from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper

__all__ = ['Articles']


class ArticlesWrapper(ComponentWrapper):
    title = Component(tag='a')


class Articles(Components):
    def __get__(self, instance, owner) -> List[ArticlesWrapper]:
        ret: List[ArticlesWrapper] = []

        for webelement in self.finds(instance):
            ret.append(ArticlesWrapper(instance.app, webelement, self._locator))

        return ret
