import tkinter as tk
import pandas as pd
from random import randint, choice, shuffle
from tkinter import messagebox

PINK = '#fcd1d1'
OFF_WHITE = '#ece2e1'
LIGHT_GREY = '#d3e0dc'
LIGHT_BLUE = '#aee1e1'

german_word = ''
translation = ''
count_down = None
cards_shown = 0
points = 0
list_of_milestones = []


# ----------------- FLASHCARD WORDS SETUP ----------#
try:
    word_data = pd.read_excel('Data/words_to_learn.xlsx')
    print('data was found')
except FileNotFoundError:
    word_data = pd.read_excel('Data/frequent_words_german_with translation.xlsx')
    print('data was not found')

finally:
    to_learn = word_data.to_dict(orient='records')


def reward():
    global points
    # Background image - Blank Card
    # img_dog = tk.PhotoImage(file='images/rewards/dog_3.png')
    img_dog = choice(img_list)
    canvas.itemconfig(card, image=img_dog)
    canvas.itemconfig(card_title, text='')
    canvas.itemconfig(card_word, text='')

    window.after_cancel(count_down)
    canvas.itemconfig(timer_text, text='')
    correct_button.config(command=next_word)
    correct_button.config(state='normal')
    wrong_button.config(state='disabled')
    skip_button.config(state='disabled')


def correct_answer():
    global points
    global german_word
    points += 1
    # to delete dictionary in list
    for i in range(len(to_learn)):
        if to_learn[i]['word'] == german_word:
            del to_learn[i]
            words_to_learn = pd.DataFrame(data=to_learn)
            words_to_learn.to_excel('Data/words_to_learn.xlsx', index=False)
            break

    next_word()


def wrong_answer():
    next_word()


def next_word():
    global points
    global german_word
    global translation
    global cards_shown
    global list_of_milestones

    if (points % 5 == 0) and (points not in list_of_milestones) and points > 0:
        reward()
        list_of_milestones.append(points)
    else:
        timer(5)
        skip_button.config(state='normal')
        canvas.itemconfig(card, image=img_front)
        random_word_dict = choice(to_learn)
        german_word = random_word_dict['word']
        translation = random_word_dict['translation']
        canvas.itemconfig(card_title, text='Deutsch', fill='black')
        canvas.itemconfig(card_word, text=german_word, fill='black')
        cards_shown += 1
        print(f'points: {points}')
        print(f'cards: {cards_shown}')


def show_answer(translation):
    canvas.itemconfig(card, image=img_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=translation, fill='white')
    canvas.itemconfig(timer_text, text='')


def skip():
    correct_button.config(command=correct_answer)
    global count_down
    window.after_cancel(count_down)
    canvas.itemconfig(timer_text, text='')
    correct_button.config(state='normal')
    wrong_button.config(state='normal')
    global translation
    show_answer(translation)


def timer(count):
    global count_down
    correct_button.config(state='disabled')
    wrong_button.config(state='disabled')
    canvas.itemconfig(timer_text, text=f'{count}')

    if count > 0:
        count_down = window.after(1000, timer, count - 1)
    else:
        correct_button.config(state='normal')
        wrong_button.config(state='normal')
        global translation
        show_answer(translation)


# ------------------ UI SETUP -----------------------#
window = tk.Tk()
window.title('Flash Cards')
window.config(pady=50, padx=50, bg=PINK)
window.resizable(False, False)

# Background image - Blank Card
img_front = tk.PhotoImage(file='images/blank_card.png')
img_back = tk.PhotoImage(file='images/back_side_card.png')
img_list = [tk.PhotoImage(file=f'images/rewards/dog_{x}.png') for x in range(1, 12)]
canvas = tk.Canvas(width=810, height=450, bg=PINK, highlightthickness=0)
card = canvas.create_image(400, 220, image=img_front)
canvas.grid(row=1, column=0, columnspan=2)

# title text
card_title = canvas.create_text(400, 73, text='Deutsch', font=('Ariel', 30, 'italic'))
# word text
card_word = canvas.create_text(400, 240, text='German Word', font=('Ariel', 40, 'bold'))
# timer
timer_img = tk.PhotoImage(file="images/stopwatch.png")
timer_icon = canvas.create_image(780, 71, image=timer_img)
timer_text = canvas.create_text(780, 75, text='', font=('Ariel', 35, 'normal'))

# Buttons
correct_image = tk.PhotoImage(file="images/tick.png")
correct_button = tk.Button(image=correct_image, highlightthickness=0, command=correct_answer, bg=PINK)
correct_button["border"] = "0"
correct_button.grid(row=2, column=1, columnspan=1, sticky='E')

wrong_image = tk.PhotoImage(file="images/cross.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_word, bg=PINK)
wrong_button["border"] = "0"
wrong_button.grid(row=2, column=0, columnspan=1, sticky='W')

skip_image = tk.PhotoImage(file="images/magnifying-glass.png")
skip_button = tk.Button(image=skip_image, text='Show Answer', highlightthickness=0, command=skip, bg=PINK)
skip_button["border"] = "0"
skip_button.place(relx=0.5, rely=0.9, anchor='center')

next_word()

window.mainloop()
