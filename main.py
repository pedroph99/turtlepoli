#Following pep8 instructions
import curses
import math
import time
import curses.textpad as ct
#imports the class snake from the file snake_body, wich is in the same folder
from snake_body import snake

snake_1 = snake()


def run(stdscr):
    stdscr.clear()
    curses.start_color()
    w_values = stdscr.getmaxyx()
    screen = curses.newwin(w_values[0],w_values[1]-2,0,0)
    screen.keypad(True)
    screen.box('|','-')
    pad = curses.newpad(2,2)
    screen.refresh()
    pad.addstr(0,0, "@")
    x = 0
    y = 0
    array_saved = []
    pad.refresh(0,0,math.floor(w_values[0]/2)+x,math.floor(w_values[1]/2)+y,math.floor(w_values[0]/2)+x,math.floor(w_values[1]/2)+y)
    while True:
        key = screen.getkey()
        if key == 'KEY_A2':
            x-=1
        elif key == 'KEY_C2':
            x+=1
        elif key == 'KEY_B3':
            y+=1
        elif key == 'KEY_B1':
            y-=1        
        screen.clear()
        screen.box('|','-')
        screen.refresh()
        for x2 in array_saved:
            screen.addstr(x2[0], x2[1], '-')
        pcx = math.floor(w_values[0]/2)+x
        pcy = math.floor(w_values[1]/2)+y
        array_saved.append([pcx,pcy])
        
        pad.refresh(0,0,math.floor(w_values[0]/2)+x,math.floor(w_values[1]/2)+y,math.floor(w_values[0]/2)+x,math.floor(w_values[1]/2)+y)

        
        

    
    


curses.wrapper(run)
