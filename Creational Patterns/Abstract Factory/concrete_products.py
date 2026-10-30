from abstract_products import Button, Checkbox

class WinButton(Button):
    def render(self) -> None:
        print("Rendering Windows Button")

class WinCheckbox(Checkbox):
    def render(self) -> None:
        print("Rendering Windows Checkbox")

class MacButton(Button):
    def render(self) -> None:
        print("Rendering macOS Button")

class MacCheckbox(Checkbox):
    def render(self) -> None:
        print("Rendering macOS Checkbox")