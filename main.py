from tkinter import *
import random
from gtts import gTTS
import pandas as pd
import os
import csv
BACKGROUND_COLOR = "#B1DDC6"

#Functions
try:
    data= pd.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data= pd.read_csv("data/french_words.csv")
    dict1= original_data.to_dict(orient="records")
else:
    dict1 = data.to_dict(orient="records")
random_french = {}
def random_word():
    global random_french, flip_timer,value
    window.after_cancel(flip_timer)
    random_french= random.choice(dict1)
    value= random_french.get("French", "")
    text_to_speech()
    f_words= random_french["French"]
    canvas.itemconfig(word_label, text=f"{f_words}", fill= "black")
    canvas.itemconfig(title_label, text="French", fill="black")
    canvas.itemconfig(background_image, image=my_image)
    flip_timer= window.after(3000, func=front_word)
value= ""
def remove():
    random_word()
    dict1.remove(random_french)
    new_data= pd.DataFrame(dict1)
    new_data.to_csv("data/words_to_learn.csv", index= False)
def front_word():

    canvas.itemconfig(title_label, text="English", fill= "white")
    canvas.itemconfig(word_label, text=random_french["English"], fill="white")
    canvas.itemconfig(background_image, image= back_image)
def text_to_speech():
    text = value
    if text:
        tts= gTTS(text, lang= "fr")
        tts.save("output.mp3")
        os.system("start output.mp3")

window= Tk()
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)
flip_timer= window.after(3000, func=front_word)
my_image = PhotoImage(file="images/card_front.png")
back_image= PhotoImage(file="images/card_back.png")
canvas = Canvas(height=526, width= 800, highlightthickness= 0, bg= BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
background_image= canvas.create_image(410, 280, image=my_image)

#Button image
right_button= PhotoImage(file="images/right.png")
wrong_button= PhotoImage(file= "images/wrong.png")
r_button = Button(image=right_button, highlightthickness=0, bg= BACKGROUND_COLOR, command=remove)
r_button.grid(row=1, column=1, sticky="")
wr_button= Button(image=wrong_button, highlightthickness=0, command= random_word)
wr_button.grid(row=1, column=0, sticky="")

#Labels
title_label = canvas.create_text(390, 150, text="Language", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 300, text="Word", font=("Ariel", 60, "bold"))
























window.mainloop()
