import pygetwindow as gw
import pyautogui

# Replace 'Game Title' with the actual title of your game window
window_title = 'Albion Online Client'

# Find the window with the given title
game_window = None
for window in gw.getAllWindows():
    if window_title in window.title:
        game_window = window
        break

# Activate the game window if found
if game_window:
    game_window.activate()
    # Optional: move the mouse to the center of the game window to ensure focus
    center_x = game_window.left + game_window.width // 2
    center_y = game_window.top + game_window.height // 2
    pyautogui.moveTo(center_x, center_y)
else:
    print(f'Window with title containing "{window_title}" not found.')