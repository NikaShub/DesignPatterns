from abstract_factory import GUIFactory
from abstract_products import Button, Checkbox
from concrete_products import WinButton, WinCheckbox, MacButton, MacCheckbox

class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()