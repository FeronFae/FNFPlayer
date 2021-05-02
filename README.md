# FNFPlayer
An automatic ninjamuffin99's Friay Night Funkin' player by FeronFae.

_*Dependencies:*_ 
- Keyboard
- Pyautogui

_*Requierments:*_
- Game must be in fullscreen windowed mode (on a 1080p display)
- Game must be completely centered
- Due to some issues with the win32DC Release function of pyscreeze (used by the pyautogui module for pixel scanning) in Python 3.8+, you must run this script with any version of [Python _3.7]_ (I will update this segment whenever the pyautogui issue is resolved. You can follow any updates [here](https://github.com/asweigart/pyscreeze/issues/72).

_*Known Issues and more information:*_
- The script is not perfect, sometimes it will not achieve a perfect score due to computational limitations (I am doing my best to spread the workload and make this script as efficient as possible).
- The script bases off of the arrow colors and the corresponding pixels on screen that display these colors when the arrow is inside of the hitbox; seen as the colors are different in week 6, I must make a separated file for the pixel weeks.
- Mods are fully supported, as long as the arrows withhold their original colors.
- Any recommendations for bettering performance are welcome!
