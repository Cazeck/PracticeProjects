from tkinter import *   # So we don't need to tkinter.method everything

window = Tk()                   # Creates Empty Window

def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)

# Add widgets between window and mainloop
b1 = Button(window, text="Execute", command=km_to_miles)    # Brackets not needed for commands here
b1.grid(row=0, column=0)        # Needed to put the widget object onto the display. Can use pack or grid. Grid gives more accuracy

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()               # Loops the window and keeps it open

