from tkinter import *
import random

#next turn

def next_turn(row,col):
    global player
    if game_btns[row][col]['text'] == "" and check_win() == False:
        if player == players[0]:
            game_btns[row][col]['text'] = player
            
            if check_win() == False:
                player = players[1]
                label.config(text=(players[1]+':Turn'))
            elif check_win() == True:
                label.config(text=(players[0]+' :Wins!!'))
            elif check_win() == 'tie':
                label.config(text=('Draw, No winner!'))
        
        elif player == players[1]:
            game_btns[row][col]['text'] = player
            
            if check_win() == False:
                player = players[0]
                label.config(text=(players[0]+':Turn'))
            elif check_win() == True:
                label.config(text=(players[1]+':Wins!!'))
            elif check_win() == 'tie':
                label.config(text=('Draw, No winner!'))
    
    
    
# check_win-------------------------------------------------------------
def check_win() :
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg='green')
            game_btns[row][1].config( bg='green')
            game_btns[row][2].config( bg='green')
            return True
        
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg='green')
            game_btns[1][col].config( bg='green')
            game_btns[2][col].config( bg='green')
            return True
        
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg='green')
        game_btns[1][1].config( bg='green')
        game_btns[2][2].config( bg='green')
        return True
    
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg='green')
        game_btns[1][1].config( bg='green')
        game_btns[2][0].config( bg='green')
        return True
    
    
    if empty_space() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg = 'red')
        
        return 'tie'
    else:
        return False
        
            
# Empty sapces ------------------------
def empty_space():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != '':
                spaces -= 1
    if spaces ==0:
         return False
    else:
        return True


# Restart -------------
def restart():
    global player
    
    player = random.choice(players)
    label.config(text=(player + ":turn"))
    
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text='', bg='#F0F0F0')
    


window = Tk()
window.title('X-O Game !!')

players = ['X','O']
player = random.choice(players)

game_btns = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]
             ]


label  = Label(text=(player + ":turn"), font=('consolas',40))
label.pack(side="top")

restart = Button(text=("Restart"),font=('consolas', 20), command=restart)
restart.pack(side='top')


btn = Frame(window)
btn.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btn, text='', font=('consolas',50), width=4,height=1,
                                 command= lambda row=row, col=col: next_turn(row,col))
        game_btns[row][col].grid(row=row,column=col)
        
        

window.mainloop()