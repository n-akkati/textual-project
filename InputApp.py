from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Button, Label


class InputApp(App):
    
    def compose(self) -> ComposeResult:
        yield Header()

        yield Label("Enter your name:")
        
        yield Input(placeholder="Type your name here...", id="name_input")
        
        yield Button("Submit", id="submit_btn")
        
        yield Label("", id="output")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        input_widget = self.query_one("#name_input", Input)
        
        name = input_widget.value

        output = self.query_one("#output", Label)
        
        if name:
            output.update(f"Hello, {name}! 👋")
        else:
            output.update("Please enter your name first!")


if __name__ == "__main__":
    app = InputApp()
    app.run()
