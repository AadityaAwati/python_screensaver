# Python Screen-Saver

This python program uses tkinter, opencv, and pillow to create a full-screen Screen-Saver(which is a .mp4 video) when in-activity is detected for 10 seconds.
If No Mouse and Keyboard Activity is detected by pynput for 10 seconds continuosly, a full-screen tkinter window is created(which even covers the taskbar!) with a opencv video - screensaver.mp4 as its background. As soon as activity is detected, the window will automatically destroy itself.
The program runs continuosly in a while loop, and in-order to stop the screensaver from appearing, the user must stop the program. Converting main.py to an .exe file using auto-py-to-exe can make it easier to run the screen-saver program. The .exe file can even be set as a Startup Application so that the user will not even have to manually run the program!

### The Screensaver Video Can be Changed by Using a diiferent screensaver.mp4, for now I have used a matrix rain screensaver as an example. The timeout for the ScreenSaver is currently 10 seconds. It can be changed to be higher or lower by changing the timeout variable's value.

### In-order for the Screen-Saver to be full Screen, Python 3.13 and Tk 8.7+ is required!
