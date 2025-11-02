from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static


class ButtonClickApp(App):
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Click the button below!")
        yield Button("Click Me!")
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.notify("Button was clicked!")


if __name__ == "__main__":
    app = ButtonClickApp()
    app.run()
