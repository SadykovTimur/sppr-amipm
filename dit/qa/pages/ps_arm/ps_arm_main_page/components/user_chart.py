from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper

__all__ = ['UserChart']


class UserChartWrapper(ComponentWrapper):
    points = Components(class_name='highcharts-point')


class UserChart(Component):
    def __get__(self, instance, owner) -> UserChartWrapper:
        return UserChartWrapper(instance.app, self.find(instance), self._locator)
