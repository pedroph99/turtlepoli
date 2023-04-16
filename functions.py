
import math
import time
# Funções auxiliares ao código main.

def refresh_tela(pad,w_values,x,y):
    pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)


def refresh_pad2(pad_2,w_values):
    pad_2.refresh(0,0,math.floor((w_values[0]-3)),0,math.floor((w_values[0]-1)),math.floor(w_values[1]-1))


def desenha_tela(tela, x,y, simbolo):
    tela.addstr(x,y,simbolo)


def refresh_pad(pad, w_values, x,y):
    pad.refresh(0,0,math.floor((w_values[0]-3)/2)+x,math.floor((w_values[1])/2)+y,math.floor((w_values[0] -3)/2)+x,math.floor(w_values[1]/2)+y)


def refresh_main_screen(screen):
    screen.clear()
    screen.box('|','-')
    screen.refresh()

def verify_x(w_values, x):
    if math.floor(w_values[0]/2)+x<=2:
        return math.floor(w_values[0]/2)-3
    elif math.floor(w_values[0]/2)+x == w_values[0]-2:
        return -(math.floor(w_values[0]/2)-3)
    else:
        return x
    
def verify_y(w_values, y):
    print(math.floor(w_values[1]/2)+y)
    if math.floor(w_values[1]/2)+y<=1:
        print('FOI PARA BAIXO DE 0')
        print(w_values[1])
        return math.floor(w_values[1]/2)-2
    elif math.floor(w_values[1]/2)+y == w_values[1]-2:
        print('chegou ao ponto')
        print(-(math.floor(w_values[1]/2)-2))
        return -(math.floor(w_values[1]/2)-2)
    else:
        return y

def draw_directions(screen, w_values, array_saved, pad, x, y):
    screen.clear()
    screen.box('|','-')
                            
    pcx = math.floor((w_values[0]-3)/2)+x
    pcy = math.floor(w_values[1]/2)+y
    print(array_saved)
    for x2 in array_saved:
        if x2[0] != pcx or x2[1] != pcy:
            desenha_tela(screen, x2[0], x2[1], '*')
        else:
            desenha_tela(screen, x2[0], x2[1], '@')
                            
    if [pcx, pcy] not in array_saved:
        array_saved.append([pcx,pcy ])
                            
    screen.refresh()
    refresh_pad(pad, w_values, x,y)
                            
    time.sleep(0.25)
    
def finish_game(key, curses):
    if key == "q":
        curses.endwin()
        quit() 
