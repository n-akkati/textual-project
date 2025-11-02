from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class WidgetsApp(App):
    
    def compose(self) -> ComposeResult:
        yield Header()

        yield Static("Welcome to Textual!")
        yield Static("This is a multi-widget app")
        yield Static("Each line is a separate widget")
        yield Static("Pretty cool, right?")
        
        yield Footer()


if __name__ == "__main__":
    app = MultiWidgetApp()
    app.run()
