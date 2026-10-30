import sys
from abstract_factory import GUIFactory
from concrete_factories import WinFactory, MacFactory

class Application:
    def __init__(self, factory: GUIFactory) -> None:
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self) -> None:
        self.button.render()
        self.checkbox.render()

def main() -> None:
    os_name = sys.platform
    if os_name == "darwin":
        factory = MacFactory()
    else:
        factory = WinFactory()

    app = Application(factory)
    app.render_ui()

if __name__ == "__main__":
    main()