#Following pep8 instructions
import curses
import math
import time
import re
from functions import *

def finish_game(key, curses):
    if key == "q":
        curses.endwin()
        quit()  

def run(stdscr):

    key=""
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
    desenha_tela(pad, 0,0, "@")
    desenha_tela(pad_2,1,1,"Comando turtle: ")
    x = 0
    y = 0
    array_saved = []
    refresh_pad(pad, w_values, x, y)
    refresh_pad2(pad_2, w_values)
    turtle_commands = []
    string_comand = ''
    while True:
        key = screen.getkey()
        
        if key == "q":
            finish_game(key, curses)
        
        try:

            if ord(key) == 8:
                turtle_commands.pop()
                pad_2.clear()
                desenha_tela(pad_2, 1,1, 'Comando turtle')
                for x_turtle in range(len(turtle_commands)):
                    desenha_tela(pad_2, 1,18+x_turtle,  turtle_commands[x_turtle])
                pad_2.box('|', '-')
                refresh_pad2(pad_2, w_values)
            
            elif ord(key) == 10:
                string_comand = ''
                for x_string in turtle_commands:
                    string_comand+=x_string
                if re.fullmatch((r"(NE|NO|N|SO|SL|S|O|E|L)\s*[0-9]*"), string_comand):
                    print(string_comand.split(' ')[1])
                    
                    if string_comand.split(' ')[0] == 'NE':
                        print(string_comand.split(' ')[1])
                        for x_times in range(int(string_comand.split(' ')[1])):
                            y+=1
                            x-=1
                            x = verify_x(w_values, x)
                            y = verify_y(w_values, y)
                            draw_directions(screen, w_values, array_saved, pad, x, y)
                    elif string_comand.split(' ')[0] == 'NO':
                        print(string_comand.split(' ')[1])
                        for x_times in range(int(string_comand.split(' ')[1])):
                            y-=1
                            x+=1
                            x = verify_x(w_values, x)
                            y = verify_y(w_values, y)
                            draw_directions(screen, w_values, array_saved, pad, x, y)

                    elif string_comand.split(' ')[0] == 'N':
                        print(string_comand.split(' ')[1])
                        for x_times in range(int(string_comand.split(' ')[1])):
                            x-=1
                            x = verify_x(w_values, x)

                            draw_directions(screen, w_values, array_saved, pad, x, y)
                    elif string_comand.split(' ')[0] == 'S':
                        for x_times in range(int(string_comand.split(' ')[1])):
                            x+=1
                            x = verify_x(w_values, x)
                            draw_directions(screen, w_values, array_saved, pad, x, y)
                    elif string_comand.split(' ')[0] == 'SL':
                        for x_times in range(int(string_comand.split(' ')[1])):
                            x+=1
                            y+=1
                            x = verify_x(w_values, x)
                            y =  verify_y(w_values, y)
                            draw_directions(screen, w_values, array_saved, pad, x, y)
                    elif string_comand.split(' ')[0] == 'SO':
                        print(string_comand.split(' ')[1])
                        for x_times in range(int(string_comand.split(' ')[1])):
                            y-=1
                            x+=1
                            x = verify_x(w_values, x)
                            y = verify_y(w_values, y)
                            draw_directions(screen, w_values, array_saved, pad, x, y)
                    
                    elif string_comand.split(' ')[0] == 'O':
                        print(string_comand.split(' ')[1])
                        for x_times in range(int(string_comand.split(' ')[1])):
                            y-=1
                            y = verify_y(w_values, y)
                            draw_directions(screen, w_values, array_saved, pad, x, y)
                    
                    elif string_comand.split(' ')[0] == 'L':
                        print(string_comand.split(' ')[1])
                        for x_times in range(int(string_comand.split(' ')[1])):
                            y+=1
                            y = verify_y(w_values, y)
                            draw_directions(screen, w_values, array_saved, pad, x, y)
                            
                    
                    
                turtle_commands.clear()
                pad_2.clear()
                desenha_tela(pad_2, 1,1, "Comando turtle: ")
                for x_turtle in range(len(turtle_commands)):
                    pad_2.addstr(1,18 + x_turtle, turtle_commands[x_turtle])
                pad_2.box('|', '-')
                refresh_pad2(pad_2, w_values)

            elif (ord(key)>=65 and ord(key)<=90) or (ord(key)>=48 and ord(key)<=57):
                desenha_tela(pad_2, 1,18+len(turtle_commands), key)
                turtle_commands.append(key)
                refresh_pad2(pad_2, w_values)
            elif ord(key) == 32:
                desenha_tela(pad_2, 1,18+len(turtle_commands), key)
                turtle_commands.append(' ')
                refresh_pad2(pad_2, w_values)

        except:
            pass

        if key == 'KEY_A2' or key == 'KEY_UP':
            x-=1
            x = verify_x(w_values, x)
        elif key == 'KEY_C2' or key == 'KEY_DOWN':
            x+=1
            x = verify_x(w_values, x)
        elif key == 'KEY_B3' or key == 'KEY_LEFT':
            y+=1
            y = verify_y(w_values,y)
        elif key == 'KEY_B1' or key == 'KEY_RIGHT':
            y-=1 
            y = verify_y(w_values,y)
        refresh_main_screen(screen)
        pcx = math.floor((w_values[0]-3)/2)+x
        pcy = math.floor(w_values[1]/2)+y
        print(array_saved)
        for x2 in array_saved:
            if x2[0] != pcx or x2[1] != pcy:
                desenha_tela(screen, x2[0], x2[1], '*')
            else:
                desenha_tela(screen, x2[0], x2[1], '@')
        
        if [math.floor((w_values[0]-3)/2), math.floor(w_values[1]/2)] not in array_saved:
            array_saved.append([math.floor((w_values[0]-3)/2), math.floor(w_values[1]/2)])
        if [pcx, pcy] not in array_saved:
            array_saved.append([pcx,pcy ])
        
        desenha_tela(screen, pcx,pcy, '@')
        refresh_tela(pad, w_values, x, y)

curses.wrapper(run)