from tkinter import *
import string
import random

grid = []
grid_size = 5
master = Tk()
text = [[None]*grid_size for _ in range(grid_size)]
buttons = [[None]*grid_size]*grid_size

def test():
    print('hi')
    # x = master.btn1.winfo_rootx()
    # Button.config(state=DISABLED)

def action(n, i, letter):
    # text[n][i].set('Clicked')
    print(text[n][i].get())
    # print(text[n][i].se)

for n in range(0,grid_size):
    grid.append([])
    for i in range(0,grid_size):
        letter = random.choice(string.ascii_uppercase)
        text[n][i] = StringVar()
        text[n][i].set(letter)
        grid[n].append(Canvas(master, bg="#1E9522", height="50", width="50"))
        grid[n][i].propagate(False)
        grid[n][i].grid(row=n, column=i)
        buttons[n][i] = Button(grid[n][i],textvariable = text[n][i] , height=1, width=2, bg='#222', fg='white', state=NORMAL, command = lambda n=n, i=i : action(n, i, letter)).pack(pady=15)

mainloop()

