from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msbox
import random
import time


def paper_icon_clicked():
    paper_icon_button.config(relief=RAISED, bg='black')
    rock_icon_button.config(relief=FLAT, bg='white')
    Scissor_icon_button.config(relief=FLAT, bg='white')

def rock_icon_clicked():
    rock_icon_button.config(relief=RAISED, bg='black')
    paper_icon_button.config(relief=FLAT, bg='white')
    Scissor_icon_button.config(relief=FLAT, bg='white')

def scissor_icon_clicked():
    Scissor_icon_button.config(relief=RAISED, bg='black')
    rock_icon_button.config(relief=FLAT, bg='white')
    paper_icon_button.config(relief=FLAT, bg='white')

def get_user_token():
    l1 = [rock_icon_button, paper_icon_button, Scissor_icon_button]
    for item in l1:
        if item.cget('relief') == RAISED:
            if item._name == '!button':
                return 'rock'
            if item._name == '!button2':
                return 'paper'
            if item._name == '!button3':
                return 'scissor'
            else:
                pass
                # msbox.showerror('error', 'please select one')

def get_random_token():
    tokens = ['rock', 'paper', 'scissor']
    comp_token = random.choice(tokens)
    return comp_token

def show_player_token():
    if get_user_token() == 'rock':
        rock_token = ImageTk.PhotoImage(Image.open('./gallery/rock_token.png'))
        player_label.configure(image=rock_token, width=80, height=80)
        player_label.image = rock_token
        return True

    if get_user_token() == 'paper':
        paper_token = ImageTk.PhotoImage(Image.open('./gallery/paper_token.png'))
        player_label.configure(image=paper_token, width=80, height=80)
        player_label.image = paper_token
        return True

    if get_user_token() == 'scissor':
        scissor_token = ImageTk.PhotoImage(Image.open('./gallery/scissor_token.png'))
        player_label.configure(image=scissor_token, width=80, height=80)
        player_label.image = scissor_token
        return True

    else:
        msbox.showerror('error', 'please select one token')
        return False

def show_comp_token():
    global computer
    computer = get_random_token()
    if computer == 'rock':
        rock_token = ImageTk.PhotoImage(Image.open('./gallery/rock_token.png'))
        comp_label.configure(image=rock_token, width=80, height=80)
        comp_label.image = rock_token

    if computer == 'paper':
        paper_token = ImageTk.PhotoImage(Image.open('./gallery/paper_token.png'))
        comp_label.configure(image=paper_token, width=80, height=80)
        comp_label.image = paper_token

    if computer == 'scissor':
        scissor_token = ImageTk.PhotoImage(Image.open('./gallery/scissor_token.png'))
        comp_label.configure(image=scissor_token, width=80, height=80)
        comp_label.image = scissor_token

computer_score = 0
player_score = 0
def logic():
    global computer_score
    global player_score

    if get_user_token() == 'rock':
        if computer == 'rock':
            wl_label.config(text=f'This Round was a TIE')
        if computer == 'paper':
            computer_score += 1
            wl_label.config(text=f'You LOST This Round')
            computer_score_label.config(text=f'COMPUTER-{computer_score}')
        if computer == 'scissor':
            wl_label.config(text=f'You WON This Round')
            player_score += 1
            player_score_label.config(text=f'PLAYER-{player_score}')

    if get_user_token() == 'paper':
        if computer == 'rock':
            wl_label.config(text=f'You WON This Round')
            player_score += 1
            player_score_label.config(text=f'PLAYER-{player_score}')
        if computer == 'paper':
            wl_label.config(text=f'This Round was a TIE')
        if computer == 'scissor':
            wl_label.config(text=f'You LOST This Round')
            computer_score +=1
            computer_score_label.config(text=f'COMPUTER-{computer_score}')

    if get_user_token() == 'scissor':
        if computer == 'rock':
            wl_label.config(text=f'You LOST This Round')
            computer_score +=1
            computer_score_label.config(text=f'COMPUTER-{computer_score}')
        if computer == 'paper':
            wl_label.config(text=f'You WON This Round')
            player_score += 1
            player_score_label.config(text=f'PLAYER-{player_score}')
        if computer == 'scissor':
            wl_label.config(text=f'This Round was a TIE')


def main_func():
    show_comp_token()
    show_player_token()

    logic()
    if player_score >= 5:
        msbox.showinfo('PLAYER WON', 'YOU WON 5 MATCHES')
        quit()
    if computer_score >= 5:
        msbox.showinfo('PLAYER LOST', 'YOU LOST')
        quit()


if __name__ == '__main__':
    root = Tk()

    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    root.title('Rock Paper Scissor')

    header_frame = Frame(root).pack()
    Label(header_frame, text="ROCK PAPER SCISSOR", font='"Segoe UI" 20 bold italic', fg="#707070").pack()

    icon_frame = Frame(root)
    icon_frame.pack(pady=33)

    rock_icon = ImageTk.PhotoImage(Image.open('./gallery/rock_icon.jpg'))
    rock_icon_button = Button(icon_frame, image=rock_icon, relief=FLAT, command=rock_icon_clicked)
    rock_icon_button.pack(side="left", fill="both", expand="yes", padx=15)

    paper_icon = ImageTk.PhotoImage(Image.open('./gallery/paper_icon.jpg'))
    paper_icon_button = Button(icon_frame, image=paper_icon, relief=FLAT, command=paper_icon_clicked)
    paper_icon_button.pack(side="left", fill="both", expand="yes", padx=15)

    Scissor_icon = ImageTk.PhotoImage(Image.open('./gallery/Scissor_icon.jpg'))
    Scissor_icon_button = Button(icon_frame, image=Scissor_icon, relief=FLAT, command=scissor_icon_clicked)
    Scissor_icon_button.pack(side="right", fill="both", expand="yes", padx=15)

    go_button = Button(root, text='GO', padx=30, pady=5, font='Segeo 15 bold', relief=GROOVE, borderwidth=2,
                       command=main_func)
    go_button.pack()

    vs_frame1 = Frame(root)
    vs_frame1.pack(pady=(30, 0))

    player_score_label = Label(vs_frame1, text=f'PLAYER-0', font='"Segeo UI" 9 bold')
    player_score_label.pack(side=LEFT, padx=60)

    computer_score_label = Label(vs_frame1, text=f'COMPUTER-0', font='"Segeo UI" 9 bold')
    computer_score_label.pack(side=RIGHT, padx=50)

    vs_frame2 = Frame(root)
    vs_frame2.pack()

    player_label = Label(vs_frame2, borderwidth=2, relief=GROOVE, width=10, height=5)
    player_label.pack(side=LEFT)

    vs_img = ImageTk.PhotoImage(Image.open('./gallery/vs.png'))
    vs_label = Label(vs_frame2, image=vs_img)
    vs_label.pack(side=LEFT)

    comp_label = Label(vs_frame2, borderwidth=2, relief=GROOVE, width=10, height=5)
    comp_label.pack(side=LEFT)

    wl_label = Label(root, font='comicsaans 15 bold')
    wl_label.pack(pady=20)

    root.mainloop()