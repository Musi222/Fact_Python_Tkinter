from tkinter import *
from tkinter import ttk
import random
import os

#window settings
window =Tk()
window.geometry('700x300')
window.eval('tk::PlaceWindow . center')
window.resizable(False,False)
window.title("Random Fact")

#Text
text_Heading =Label(window, text="Fact of the day" )
text_Heading.pack()

#Random text
def show_random():
    with open('facts.txt','r') as file:
        lines = file.readlines()

    random_line = random.choice(lines)
    result_label.config(text=random_line)

#Select random text
random_button =Button(window, text="Random Fact",command=show_random)
random_button.pack()

#Result Label 
result_label = Label(window,text="")
result_label.pack()

#Exit button
exit_button = Button(window,text="Exit" ,command=window.destroy)
exit_button.pack()



window.mainloop()