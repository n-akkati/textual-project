from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Button

class HorizontalLayoutApp(App):
    
    CSS = """
    Horizontal {
        border: solid blue;
        padding: 1;
        margin: 1;
        height: auto;
    }
    
    Vertical {
        border: solid green;
        padding: 1;
        margin: 1;
    }
    
    Static {
        border: solid white;
        padding: 1;
        width: auto;
    }
    """
    
    def compose(self) -> ComposeResult:
        """Create different UI layouts."""
        yield Header()
        
        # Vertical layout (for comparison)
        yield Static("Vertical Layout (top to bottom):")
        with Vertical():
            yield Static(" Item 1")
            yield Static(" Item 2")
            yield Static(" Item 3")
        
        # Horizontal layout (side by side)
        yield Static("Horizontal Layout (left to right):")
        with Horizontal():
            yield Static(" Item A")
            yield Static(" Item B")
            yield Static(" Item C")
        
        # Horizontal with buttons
        yield Static("Horizontal with Buttons:")
        with Horizontal():
            yield Button("Button 1", id="btn1")
            yield Button("Button 2", id="btn2")
            yield Button("Button 3", id="btn3")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        self.notify(f"Clicked: {event.button.id}")


if __name__ == "__main__":
    app = HorizontalLayoutApp()
    app.run()
