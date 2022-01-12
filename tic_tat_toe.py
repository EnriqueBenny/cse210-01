#Erik Benson
#Tic-Tac-Toe Game
import tkinter as tk
from tkinter import *
def main():
    game_board()
def game_board():
    ul = 1
    um = 2
    ur = 3
    ml = 4
    mm = 5
    mr = 6
    ll = 7
    lm = 8
    lr = 9
    win = 0
    tie = False
    print(f"{ul}|{um}|{ur}\n-+-+-\n{ml}|{mm}|{mr}\n-+-+-\n{ll}|{lm}|{lr}\n")
    while win is not True and win is not False and tie is not True:
        x = int(input("x's turn to choose: "))
        if x == 1:
            ul = "x"
        elif x == 2:
            um = "x"
        elif x == 3:
            ur = "x"
        elif x == 4:
            ml = "x"
        elif x == 5:
            mm = "x"
        elif x == 6:
            mr = "x"
        elif x == 7:
            ll = "x"
        elif x == 8:
            lm = "x"
        elif x == 9:
            lr = "x"
        print(f"{ul}|{um}|{ur}\n-+-+-\n{ml}|{mm}|{mr}\n-+-+-\n{ll}|{lm}|{lr}\n")
        win = victory(ul, um, ur, ml, mm , mr, ll, lm, lr)
        tie = detect_draw(ul, um, ur, ml, mm , mr, ll, lm, lr)
        if win is not True and tie is not True:
            o = int(input("o's turn to choose: "))
            if o == 1:
                ul = "o"
            elif o == 2:
                um = "o"
            elif o == 3:
                ur = "o"
            elif o == 4:
                ml = "o"
            elif o == 5:
                mm = "o"
            elif o == 6:
                mr = "o"
            elif o == 7:
                ll = "o"
            elif o == 8:
                lm = "o"
            elif o == 9:
                lr = "o"
            print(f"{ul}|{um}|{ur}\n-+-+-\n{ml}|{mm}|{mr}\n-+-+-\n{ll}|{lm}|{lr}\n")
            win = victory(ul, um, ur, ml, mm , mr, ll, lm, lr)
    if win is True:
        x_win()
    elif win is False:
        o_win()
    elif tie is True:
        draw()
def victory(con0, con1, con2, con3, con4, con5, con6, con7, con8):
    win = "0"
    if con0 == "x" and con1 == "x" and con2 == "x":
        win = True
    elif con3 == "x" and con4 == "x" and con5 == "x":
        win = True
    elif con6 == "x" and con7 == "x" and con8 == "x":
        win = True
    elif con0 == "x" and con3 == "x"and con6 == "x":
        win = True
    elif con1 == "x" and con4 == "x" and con7 == "x":
        win = True 
    elif con2 == "x" and con5 == "x" and con8 == "x":
        win = True
    elif con0 == "x" and con4 == "x" and con8 == "x":
        win = True 
    elif con2 == "x" and con4 == "x" and con6 == "x":
        win = True
    elif con0 == "o" and con1 == "o" and con2 == "o":
        win = False 
    elif con3 == "o" and con4 == "o" and con5 == "o":
        win = False
    elif con6 == "o" and con7 == "o" and con8 == "o":
        win = False
    elif con0 == "o" and con3 == "o" and con6 == "o":
        win = False
    elif con1 == "o" and con4 == "o" and con7 == "o":
        win = False
    elif con2 == "o" and con5 == "o" and con8 == "o":
        win = False
    elif con0 == "o" and con4 == "o" and con8 == "o":
        win = False
    elif con2 == "o" and con4 == "o" and con6 == "o":
        win = False
    else:
        win = 0
    return win
def detect_draw(con0, con1, con2, con3, con4, con5, con6, con7, con8):
    tie = False
    if con0 == "x" or con0 == "o":
        if con1 == "x" or con1 == "o":
            if con2 == "x" or con2 == "o":
                if con3 == "x" or con3 == "o":
                    if con4 == "x" or con4 == "o":
                        if con5 == "x" or con5 == "o":
                            if con6 == "x" or con6 == "o":
                                if con7 == "x" or con7 == "o":
                                    if con8 == "x" or con8 == "o":
                                        tie = True
    return tie
def x_win():
    window = tk.Tk()
    reward = tk.Label(text=f"CONGRADULATIONS X,\nYOU WIN!", fg="red", bg="yellow", height=10, width=45, font=("Arial", 60))
    reward.pack()
    window.after(5000, lambda: window.quit())
    window.mainloop()
def o_win():
    window = tk.Tk()
    reward = tk.Label(text=f"CONGRADULATIONS O,\nYOU WIN!", fg="blue", bg="green", height=10, width=45, font=("Arial", 60))
    reward.pack()
    window.after(5000, lambda:window.quit())
    window.mainloop()
def draw():
    window = tk.Tk()
    reward = tk.Label(text=f"CONGRADULATIONS,\nIT'S A DRAW!", fg="white", bg="black", height=10, width=45, font=("Arial", 60))
    reward.pack()
    window.after(5000, lambda:window.quit())
    window.mainloop()

main()