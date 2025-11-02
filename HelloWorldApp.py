from textual.app import App, ComposeResult
from textual.widgets import Static

class HelloWorldApp(App):

    def compose(self) -> ComposeResult:
        yield Static("Hello, Textual World!")

if __name__ == "__main__":
    app = HelloWorldApp()
    app.run()
