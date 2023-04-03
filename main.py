#Following pep8 instructions
import curses
import math
import time
import curses.textpad as ct
import re


def finish_game(key, curses):
    if key == "q":
        curses.endwin()
        quit()  


def run(stdscr):

    key = ""

    stdscr.clear()
    w_values = stdscr.getmaxyx()
    
    menu = curses.newwin(w_values[0]-3,w_values[1],0,0)
    menu.keypad(True)
    menu.box('|', '-')
    title = "Turtle Game"
    buttonStart = "<S>tart"
    buttonQuit = "<Q>uit"
    menu.addstr(math.floor((w_values[0]-10)/2) , math.floor((w_values[1]-len(title))/2), title)
    menu.addstr(math.floor(((w_values[0]-5)/2)+1) , math.floor((w_values[1]-len(buttonStart))/2), buttonStart)
    menu.addstr(math.floor(((w_values[0])/2)+2) , math.floor((w_values[1]-len(buttonQuit))/2), buttonQuit)
    menu.refresh()
    while key!= "s":
        key = menu.getkey()
        if(key == "q"):
            finish_game(key,curses)


    stdscr.clear()
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
    
    while True:
        key = screen.getkey()
        
        finish_game(key, curses)
        try:

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
                if re.fullmatch((r"(NE|NO|N|SO|SL|S|O|E)\s*[0-9]*"), string_comand):
                    print(string_comand.split(' ')[1])

                    if string_comand.split(' ')[0] == 'E':
                        for x_times in range(string_comand.split[' '][1]):
                            print(x_times)
                            y+=1
                            pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)
                    elif string_comand.split(' ')[0] == 'NE':
                        print('okk')
                        print(string_comand.split(' ')[1])
                        for x_times in range(int(string_comand.split(' ')[1])):

                            y+=1
                            x-=1
                            screen.clear()
                            screen.box('|','-')
                            
                            pcx = math.floor((w_values[0]-3)/2)+x
                            pcy = math.floor(w_values[1]/2)+y
                            print(array_saved)
                            for x2 in array_saved:
                                if x2[0] != pcx or x2[1] != pcy:
                                    screen.addstr(x2[0], x2[1], '*')
                                else:
                                    screen.addstr(x2[0], x2[1], '@')
                            
                            if [pcx, pcy] not in array_saved:
                                array_saved.append([pcx,pcy ])
                            
                            screen.refresh()
                            pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)
                            
                            
                            time.sleep(0.25)
                    
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
        elif key == 'KEY_C2':
            x+=1
        elif key == 'KEY_B3':
            y+=1
        elif key == 'KEY_B1':
            y-=1    
        screen.clear()
        screen.box('|','-')
        screen.refresh()
        pcx = math.floor((w_values[0]-3)/2)+x
        pcy = math.floor(w_values[1]/2)+y
        print(array_saved)
        for x2 in array_saved:
            if x2[0] != pcx or x2[1] != pcy:
                screen.addstr(x2[0], x2[1], '*')
            else:
                screen.addstr(x2[0], x2[1], '@')
        
        if [pcx, pcy] not in array_saved:
            array_saved.append([pcx,pcy ])
        
        
        pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)
        
        

        
        

curses.wrapper(run)  