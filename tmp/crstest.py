#!/usr/bin/python

# crstest.py
import curses

stdscr = curses.initscr()

# Usually curses applications turn off automatic echoing of keys to the screen, in order to be able to read keys and only display
# them under certain circumstances. This requires calling the noecho() function.
curses.noecho()

# Applications will also commonly need to react to keys instantly, without requiring the Enter key to be pressed; this is called
# cbreak mode, as opposed to the usual buffered input mode.
curses.cbreak()

# Terminals usually return special keys, such as the cursor keys or navigation keys such as Page Up and Home, as a multibyte
# escape sequence. While you could write your application to expect such sequences and process them accordingly, curses can
# do it for you, returning a special value such as curses.KEY_LEFT. To get curses to do the job, you'll have to enable keypad mode.
stdscr.keypad(1)

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

pad = curses.newpad(100, 100)
#  These loops fill the pad with letters; this is
# explained in the next section
for y in range(0, 100):
    for x in range(0, 100):
        try:
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
        except curses.error:
            pass

#  Displays a section of the pad in the middle of the screen
pad.refresh(0,0, 5,5, 20,75)

# Terminating a curses application is much easier than starting one. You'll need to call
curses.nocbreak(); stdscr.keypad(0); curses.echo()

# to reverse the curses-friendly terminal settings. Then call the endwin() function to restore the terminal to its original
# operating mode.
curses.endwin()