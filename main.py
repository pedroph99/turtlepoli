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

    w_values = stdscr.getmaxyx()
    screen = curses.newwin(w_values[0]-3,w_values[1],0,0)
    
    screen.keypad(True)
    screen.box('|','-')
    pad = curses.newpad(2,2)
    pad_2 = curses.newpad(w_values[0] -(w_values[0]-3), w_values[1]-1)
    pad_2.box('|', '-')
    screen.refresh()
    pad.addstr(0,0, "@")
    pad_2.addstr(1,1, "Comando turtle: ")
    x = 0
    y = 0
    array_saved = []
    pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor(w_values[1]/2)+y,math.floor((w_values[0]-3)/2)+x,math.floor(w_values[1]/2)+y)
    pad_2.refresh(0,0,11,1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))
    turtle_commands = []
    while True:
        key = screen.getkey()
        try:
            print(key)
            print(ord(key))

            if ord(key) == 8:
                turtle_commands.pop()
                pad_2.clear()
                pad_2.addstr(1,1, "Comando turtle: ")
                for x_turtle in range(len(turtle_commands)):
                    pad_2.addstr(1,18 + x_turtle, turtle_commands[x_turtle])
                pad_2.box('|', '-')
                pad_2.refresh(0,0,11,1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))

            elif (ord(key)>=65 and ord(key)<=90) or (ord(key)>=48 and ord(key)<=57):
                pad_2.addstr(1, 18 + len(turtle_commands), key)
                turtle_commands.append(key)
                pad_2.refresh(0,0,11,1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))
            elif ord(key) == 32:
                pad_2.addstr(1, 18 + len(turtle_commands), key)
                turtle_commands.append(' ')
                pad_2.refresh(0,0,11,1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))

        except:
            pass

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
        pcx = math.floor((w_values[0]-3)/2)+x
        pcy = math.floor(w_values[1]/2)+y
        array_saved.append([pcx,pcy])
        
        pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)
        
        

        
        

    
    


curses.wrapper(run)
