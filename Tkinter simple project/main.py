from tkinter import *

window = Tk()

window.title('Sqrt/Exp/Mod')

# Canvas 1

canvas1 = Canvas(window, width=400, height=300, bg='#DAF7A6')
canvas1.pack()

# Entries (1, 2, 3)

entry1 = Entry(window)
entry2 = Entry(window)
entry3 = Entry(window)


canvas1.create_window(100, 50, window=entry1)
canvas1.create_window(100, 100, window=entry2)
canvas1.create_window(100, 150, window=entry3)

# Functions
class Delete:
    def deleteEntries():
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)

    def deleteOutputs():
        label1 = Label(window, text="                     ")
        canvas1.create_window(350, 50, window=label1)
        label2 = Label(window, text="                     ")
        canvas1.create_window(350, 100, window=label2)
        label3 = Label(window, text="                     ")
        canvas1.create_window(350, 150, window=label3)

def getSquareRoot():
    x1 = entry1.get()
    label1 = Label(window, text='{:.2f}'.format(float(x1)**0.5))
    canvas1.create_window(350, 50, window=label1)

def getExponential():
    x2 = entry2.get()

    label2 = Label(window, text='{:.2f}'.format(float(x2)*float(x2)))
    canvas1.create_window(350, 100, window=label2)

def getModulo10():
    x3 = entry3.get()
    
    label3 = Label(window, text='{:.2f}'.format(float(x3)%10))
    canvas1.create_window(350, 150, window=label3)


# Buttons

button1 = Button(text=' Get the Square Root ', command=getSquareRoot)
canvas1.create_window(240, 50, window=button1)

button2 = Button(text=' Get the Exponential ', command=getExponential)
canvas1.create_window(240, 100, window=button2)

button3 = Button(text=' Get the Modulo 10  ', command=getModulo10)
canvas1.create_window(240, 150, window=button3)

button4 = Button(text=' Clear Entries ', command=Delete.deleteEntries)
canvas1.create_window(76, 200, window=button4)

button5 = Button(text=' Clear Results ', command=Delete.deleteOutputs)
canvas1.create_window(76, 250, window=button5)

window.mainloop()