from textual.app import App, ComposeResult
from textual import events
from textual.widgets import Static
import time

class GameApp(App):
    """A text-based game with proper game loop"""
    
    BINDINGS = [("q", "quit", "Quit game")]
    
    def __init__(self):
        super().__init__()
        self.player_x = 5
        self.player_y = 5
        self.game_active = True
        self.last_update = time.monotonic()

    def compose(self) -> ComposeResult:
        """Create game layout"""
        yield Static("", id="status")
        
    def on_mount(self) -> None:
        """Set up game loop when app starts"""
        self.set_interval(1/60, self.game_loop)
        
    def game_loop(self) -> None:
        """Main game update cycle"""
        if not self.game_active:
            return
            
        # Calculate delta time
        current_time = time.monotonic()
        dt = current_time - self.last_update
        self.last_update = current_time
        
        # Update game state here
        self.update_display(dt)
        
    def update_display(self, dt: float) -> None:
        """Render game state"""
        display = f"Text Adventure Game | Delta: {dt:.2f}s\n"
        display += f"Position: ({self.player_x}, {self.player_y})\n"
        display += "Use arrow keys to move\nPress Q to quit"
        self.query_one("#status").update(display)

    def on_key(self, event: events.Key) -> None:
        """Handle player input"""
        if event.key == "q":
            self.action_quit()
        elif event.key == "up":
            self.player_y -= 1
        elif event.key == "down":
            self.player_y += 1
        elif event.key == "left":
            self.player_x -= 1
        elif event.key == "right":
            self.player_x += 1
            
    def action_quit(self) -> None:
        """Exit the game"""
        self.game_active = False
        self.exit()

if __name__ == "__main__":
    GameApp().run()
