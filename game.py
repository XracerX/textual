from textual.app import App, ComposeResult
from textual.widgets import Static

class GameApp(App):
    """A minimal text-based game loop"""
    
    BINDINGS = [("q", "quit", "Quit game")]
    
    def compose(self) -> ComposeResult:
        """Create game layout"""
        yield Static("Welcome to Text Adventure!\nPress Q to quit", id="status")
    
    def on_key(self, event):
        """Handle key presses"""
        self.query_one("#status").update(f"Last key pressed: {event.key}\nPress Q to quit")
    
    def action_quit(self):
        """Quit the game"""
        self.exit()

if __name__ == "__main__":
    GameApp().run()
