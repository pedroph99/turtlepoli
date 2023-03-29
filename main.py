#Following pep8 instructions
import curses
import math
import time
import curses.textpad as ct





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
    pad_2.refresh(0,0,math.floor((w_values[0]-3)),1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))
    turtle_commands = []
    string_comand = ''
    previous_direction = ''
    current_direction = ''
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
                pad_2.refresh(0,0,math.floor((w_values[0]-3)),1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))
            
            elif ord(key) == 10:
                string_comand = ''
                for x_string in turtle_commands:
                    string_comand+=x_string
                print(string_comand)

                if string_comand.split(' ')[0] == 'E':
                    y+=1
                    current_direction = '-'
                    pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)
                elif string_comand.split(' ')[0] == 'NE':
                    y+=1
                    x-=1
                    current_direction = '/'
                    pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)

                    
                turtle_commands.clear()
                pad_2.clear()
                pad_2.addstr(1,1, "Comando turtle: ")
                for x_turtle in range(len(turtle_commands)):
                    pad_2.addstr(1,18 + x_turtle, turtle_commands[x_turtle])
                pad_2.box('|', '-')
                pad_2.refresh(0,0,math.floor((w_values[0]-3)),1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))

            elif (ord(key)>=65 and ord(key)<=90) or (ord(key)>=48 and ord(key)<=57):
                pad_2.addstr(1, 18 + len(turtle_commands), key)
                turtle_commands.append(key)
                pad_2.refresh(0,0,math.floor((w_values[0]-3)),1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))
            elif ord(key) == 32:
                pad_2.addstr(1, 18 + len(turtle_commands), key)
                turtle_commands.append(' ')
                pad_2.refresh(0,0,math.floor((w_values[0]-3)),1,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))

        except:
            pass

        if key == 'KEY_A2':
            x-=1
            current_direction = '|'
        elif key == 'KEY_C2':
            x+=1
            current_direction = '|'
        elif key == 'KEY_B3':
            y+=1
            current_direction = '-'
        elif key == 'KEY_B1':
            y-=1 
            current_direction = '-'      
        screen.clear()
        screen.box('|','-')
        screen.refresh()
        pcx = math.floor((w_values[0]-3)/2)+x
        pcy = math.floor(w_values[1]/2)+y
        if previous_direction != '':
            array_saved[-1][2] = current_direction
        print(array_saved)
        for x2 in array_saved:
            if x2[0] != pcx or x2[1] != pcy:
                screen.addstr(x2[0], x2[1], x2[2])
            else:
                screen.addstr(x2[0], x2[1], '@')
        
        if previous_direction != '':
            array_saved.append([pcx,pcy, None])
        else:
            print(current_direction)
            array_saved.append([pcx,pcy, current_direction])
        previous_direction = current_direction
        
        pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)
        
        

        
        

curses.wrapper(run)
