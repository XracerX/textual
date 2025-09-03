from textual.app import App, ComposeResult
from textual.widgets import Label
import sys

class GameApp(App):
    """A minimal text-based game with movement mechanics"""
    
    BINDINGS = [("q", "quit", "Quit game")]
    
    def __init__(self):
        super().__init__()
        self.player_x = 5
        self.player_y = 5
        self.running = True
    
    def compose(self) -> ComposeResult:
        yield Label(id="game_display")
    
    def on_mount(self) -> None:
        self.game_loop()
    
    def action_quit(self) -> None:
        self.exit()
    
    def update_display(self) -> None:
        game_display = self.query_one("#game_display")
        game_display.update(f"Position: ({self.player_x}, {self.player_y})\nArrow keys to move, Q to quit")
    
    def game_loop(self) -> None:
        self.update_display()
    
    def on_key(self, event):
        move_speed = 1
        if event.key == "up":
            self.player_y -= move_speed
        elif event.key == "down":
            self.player_y += move_speed
        elif event.key == "left":
            self.player_x -= move_speed
        elif event.key == "right":
            self.player_x += move_speed
        self.game_loop()

if __name__ == "__main__":
    GameApp().run()
