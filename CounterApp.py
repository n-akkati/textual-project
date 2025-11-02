from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label


class CounterApp(App):
    
    def __init__(self):

        super().__init__()
        self.counter = 0
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Counter Demo", id="title")
        
        yield Label(f"Count: {self.counter}", id="count_display")
        
        yield Button("➕ Increment", id="btn_inc")
        yield Button("➖ Decrement", id="btn_dec")
        yield Button("Reset", id="btn_reset")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_inc":
            self.counter += 1
        
        elif event.button.id == "btn_dec":
            self.counter -= 1
        
        elif event.button.id == "btn_reset":
            self.counter = 0

        self.update_display()
    
    def update_display(self):

        count_label = self.query_one("#count_display", Label)
        
        count_label.update(f"Count: {self.counter}")


if __name__ == "__main__":
    app = CounterApp()
    app.run()
