import tkinter as tk
import random 
window=tk.Tk()
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)
colors=["red", "orange", "yellow", "blue", "green", "indigo", "violet"]

def ColorChange():
    button['bg']=random.choice(colors)
    pass

button=tk.Button(
    text="The color is changing",
    width=25,
    height=25,
    bg="blue",
    fg="yellow",
    command=ColorChange
)
button.pack(fill=tk.BOTH)

window=tk.Tk()
window.rowconfigure(0, minsize=150, weight=1)
window.columnconfigure([0,1], minsize=50, weight=1)

dice_nums=["1","2","3","4","5","6"]

def RollDice():
    number['text']=random.choice(dice_nums)

top_frame=tk.Frame(master=window, width=25, relief=tk.RAISED)
roll=tk.Button(master=top_frame, text="Roll",command=RollDice)
top_frame.pack(fill=tk.BOTH)
roll.pack(fill=tk.BOTH)

bottom_frame=tk.Frame(master=window,width=25)
number=tk.Label(master=bottom_frame,text="1")
bottom_frame.pack()
number.pack()
window.mainloop()