# todo list app
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Button, Input, Static, Checkbox
from textual.binding import Binding


class TodoItem(Static):
    
    def __init__(self, text: str, task_id: int, completed: bool = False):
        super().__init__()
        self.text = text
        self.task_id = task_id
        self.completed = completed
    
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Checkbox(
                self.text, 
                value=self.completed, 
                id=f"check_{self.task_id}"
            )
            
            yield Button("🗑️", classes="delete-btn", id=f"del_{self.task_id}")
    
    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        self.completed = event.value


class TodoApp(App):
    
    CSS = """
    /* Main screen background - centered layout */
    Screen {
        background: $surface;
        align: center top;
    }
    
    /* The main todo list container */
    #main-container {
        width: 70;
        height: 100%;
        border: heavy $primary;
        background: $panel;
    }
    
    /* Title area at the top */
    #header-section {
        height: auto;
        padding: 1 2;
        background: $primary;
        color: $text;
    }
    
    #title {
        width: 100%;
        text-align: center;
        text-style: bold;
    }
    
    /* Where you type new tasks */
    #input-section {
        height: auto;
        padding: 1 2;
        border-bottom: solid $accent;
    }
    
    #task-input {
        width: 1fr;
    }
    
    #add-button {
        width: 12;
        background: $success;
        margin-left: 1;
    }
    
    /* The scrolling list of tasks */
    #todo-list {
        height: 1fr;
        overflow-y: auto;
        padding: 1 2;
    }
    
    /* Individual todo items */
    TodoItem {
        height: auto;
        padding: 1;
        margin-bottom: 1;
        background: $surface;
        border: round $accent;
    }
    
    /* Highlight when you hover over a task */
    TodoItem:hover {
        background: $accent 30%;
    }
    
    Checkbox {
        width: 1fr;
    }
    
    .delete-btn {
        width: 5;
        background: $error;
        margin-left: 1;
    }
    
    /* Stats at the bottom */
    #stats {
        height: 3;
        padding: 1 2;
        background: $primary-darken-1;
        color: $text;
        border-top: solid $accent;
    }
    """
    
    # Keyboard shortcuts
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("a", "add", "Add Task"),
        Binding("c", "clear_completed", "Clear Completed"),
    ]
    
    def __init__(self):
        """Set up the app when it starts."""
        super().__init__()
        # This list holds all your tasks
        self.tasks = []
        # Used to give each task a unique ID number
        self.next_id = 1
    
    def compose(self) -> ComposeResult:
        """Build the app's user interface."""
        yield Header()
        
        with Vertical(id="main-container"):
            # Title section
            with Horizontal(id="header-section"):
                yield Static("📝 My Todo List", id="title")
            
            # Where you add new tasks
            with Horizontal(id="input-section"):
                yield Input(
                    placeholder="What do you need to do?", 
                    id="task-input"
                )
                yield Button("➕ Add", id="add-button")
            
            # The list where all your tasks appear
            with Vertical(id="todo-list"):
                pass  # Tasks will be added here as you create them
            
            # Statistics showing your progress
            yield Static("", id="stats")
        
        yield Footer()
    
    def on_mount(self) -> None:
        """Called when the app first opens."""
        # Show initial stats (will be "Total: 0" etc.)
        self.update_stats()
        
        # Put the cursor in the input box so you can start typing
        self.query_one("#task-input", Input).focus()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Someone clicked a button! Figure out which one."""
        
        if event.button.id == "add-button":
            # They clicked the Add button
            self.add_task()
        
        elif event.button.id and event.button.id.startswith("del_"):
            # They clicked a delete button (🗑️)
            # Get the task ID from the button ID
            task_id = int(event.button.id.split("_")[1])
            self.delete_task(task_id)
    
    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Someone pressed Enter in the input box."""
        if event.input.id == "task-input":
            self.add_task()
    
    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        """Someone checked or unchecked a task."""
        # Update our task list to remember this change
        if event.checkbox.id and event.checkbox.id.startswith("check_"):
            task_id = int(event.checkbox.id.split("_")[1])
            
            # Find the task and update its completed status
            for task in self.tasks:
                if task["id"] == task_id:
                    task["completed"] = event.value
                    break
        
        # Update the stats to show new progress
        self.update_stats()
    
    def add_task(self) -> None:
        # Get what they typed
        task_input = self.query_one("#task-input", Input)
        task_text = task_input.value.strip()
        
        # Don't add empty tasks
        if not task_text:
            return
        
        # Create the task
        task = {
            "id": self.next_id,
            "text": task_text,
            "completed": False
        }
        self.tasks.append(task)
        self.next_id += 1
        
        # Add it to the screen
        todo_list = self.query_one("#todo-list")
        todo_list.mount(TodoItem(task_text, task["id"]))
        
        # Clear the input box and get ready for the next task
        task_input.value = ""
        task_input.focus()
        
        # Update the stats
        self.update_stats()
    
    def delete_task(self, task_id: int) -> None:
        # Remove from our list
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        
        # Remove from the screen
        for item in self.query(TodoItem):
            if item.task_id == task_id:
                item.remove()
                break
        
        # Update the stats
        self.update_stats()
    
    def update_stats(self) -> None:
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        remaining = total - completed
        
        stats = self.query_one("#stats", Static)
        stats.update(
            f"Total: {total} | Completed: {completed} | Remaining: {remaining}"
        )
    
    def action_add(self) -> None:
        self.query_one("#task-input", Input).focus()
    
    def action_clear_completed(self) -> None:
        # Remove completed tasks from our list
        self.tasks = [t for t in self.tasks if not t["completed"]]
        
        # Remove completed tasks from the screen
        for item in self.query(TodoItem):
            if item.completed:
                item.remove()
        
        # Update the stats
        self.update_stats()


if __name__ == "__main__":
    print("=" * 60)
    print("📝 Starting Your Todo List App!")
    print("=" * 60)
    print()
    print("✨ Tips:")
    print("  - Type a task and press Enter")
    print("  - Check the box when you're done")
    print("  - Click 🗑️ to delete a task")
    print("  - Press 'a' to quickly add a new task")
    print("  - Press 'c' to clear completed tasks")
    print("  - Press 'q' to quit")
    print()
    print("=" * 60)
    print()
    
    # Create and run the app
    app = TodoApp()
    app.run()
    
    print()
    print("👋 Thanks for using the Todo List app!")
    print()
