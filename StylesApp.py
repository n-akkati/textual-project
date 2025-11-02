"""
Learn how to make your apps beautiful with CSS.
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Button, Label, Static


class StylesApp(App):
    """An app demonstrating CSS styling capabilities."""
    
    CSS = """
    Screen {
        background: $surface;
    }
    
    Header {
        background: $primary;
        color: $text;
    }
    
    #hero {
        width: 100%;
        height: 10;
        background: $accent;
        color: $text;
        content-align: center middle;
        text-style: bold;
        border: heavy $primary;
    }
    
    .card {
        width: 1fr;
        height: 12;
        margin: 1 2;
        padding: 1 2;
        background: $panel;
        border: round $accent;
        content-align: center middle;
    }
    
    .card:hover {
        background: $accent 30%;
        border: heavy $primary;
    }
    
    .card-title {
        text-style: bold;
        color: $primary;
    }
    
    .card-content {
        color: $text-muted;
        margin-top: 1;
    }
    
    #button-container {
        width: 100%;
        height: auto;
        align: center middle;
        margin-top: 2;
    }
    
    Button {
        width: 20;
        margin: 0 1;
    }
    
    Button.primary {
        background: $primary;
        color: $text;
    }
    
    Button.primary:hover {
        background: $primary-darken-1;
    }
    
    Button.success {
        background: $success;
    }
    
    Button.warning {
        background: $warning;
    }
    
    Button.error {
        background: $error;
    }
    
    #output {
        width: 100%;
        height: 5;
        background: $panel;
        color: $success;
        content-align: center middle;
        border: solid $success;
        margin-top: 2;
        text-style: bold;
    }
    """

    def compose(self) -> ComposeResult:
        """Create a beautifully styled interface."""
        yield Header()
        
        # Hero section
        with Container(id="hero"):
            yield Static("🎨 Textual Styling Demo")
        
        # Cards
        with Horizontal():
            with Container(classes="card"):
                yield Label("Feature 1", classes="card-title")
                yield Label("Fast & Responsive", classes="card-content")
            
            with Container(classes="card"):
                yield Label("Feature 2", classes="card-title")
                yield Label("Beautiful Design", classes="card-content")
            
            with Container(classes="card"):
                yield Label("Feature 3", classes="card-title")
                yield Label("Easy to Use", classes="card-content")
        
        # Buttons
        with Horizontal(id="button-container"):
            yield Button("Primary", classes="primary", id="btn1")
            yield Button("Success", classes="success", id="btn2")
            yield Button("Warning", classes="warning", id="btn3")
            yield Button("Error", classes="error", id="btn4")
        
        # Output
        yield Label("", id="output")
        
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        output = self.query_one("#output", Label)
        button_map = {
            "btn1": "Primary action executed! ✓",
            "btn2": "Success! Operation completed. ✓",
            "btn3": "Warning: Are you sure? ⚠️",
            "btn4": "Error: Action cancelled! ✗"
        }
        output.update(button_map.get(event.button.id, "Button clicked!"))


if __name__ == "__main__":
    app = StyledApp()
    app.run()
