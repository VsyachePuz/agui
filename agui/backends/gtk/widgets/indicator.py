from agui.backends.gtk.imports import *
from agui.awidgets import AIndicator
from agui.backends.gtk.widgets import Widget

class Indicator(Widget, AIndicator):
    def __init__(self, window, name, menu, attention_icon, passive_icon):
        AIndicator.__init__(self, window, name, menu, attention_icon, passive_icon)

        self._menu.triggered.connect(self.emit_triggered)

    def _create_item(self):
        self.item = AppIndicator3.Indicator.new(self.name, self._passive_icon.name(), AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.item.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

        self.item.set_icon(self._passive_icon.name())
        self.item.set_attention_icon(self._attention_icon.name())

        self._menu.hide()
        self.item.set_menu(self._menu.item)

    @AIndicator.attention.getter
    def attention(self):
        self._attention = (self.item.get_status() == AppIndicator3.IndicatorStatus.ATTENTION)
        return self._attention

    @attention.setter
    def attention(self, value):
        if value and self.item.get_status() != AppIndicator3.IndicatorStatus.ATTENTION:
            self.item.set_status(AppIndicator3.IndicatorStatus.ATTENTION)
        elif not value and self.item.get_status() != AppIndicator3.IndicatorStatus.ACTIVE:
            self.item.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

        self._attention = value

    @AIndicator.hidden.getter
    def hidden(self):
        self._hidden = (self.item.get_status() == AppIndicator3.IndicatorStatus.PASSIVE)
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        if value:
            if self.item.get_status() != AppIndicator3.IndicatorStatus.PASSIVE:
                self.item.set_status(AppIndicator3.IndicatorStatus.PASSIVE)
        else:
            self.attention(True)
        self._hidden = value

    @AIndicator.attention_icon.setter
    def attention_icon(self, value):
        self.item.set_attention_icon(value.name())
        self._attention_icon = value
