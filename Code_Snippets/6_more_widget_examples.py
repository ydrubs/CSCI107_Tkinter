import tkinter as tk
from tkinter import ttk


main_window = tk.Tk()
main_window.title("Widgets")
main_window.geometry("400x600")

frame = ttk.Frame(main_window, padding=10)
frame.pack()

text_area = tk.Text(frame, width=40, height=10)
text_area.insert(tk.END, "Hello World!")
text_area.pack()

print(text_area.get("1.0", tk.END))
text_area.delete("1.0", tk.END)
text_area["state"] = tk.NORMAL
text_area["state"] = tk.DISABLED

is_checked = tk.BooleanVar()
checkbox = ttk.Checkbutton(frame, text="Check me!", variable=is_checked, onvalue=True, offvalue=False, command=lambda: print(is_checked.get()))
checkbox.pack()

current_value = tk.IntVar()
slider = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: print(current_value.get()), variable=current_value)
slider.pack()

spinbox_value = tk.IntVar()
spinbox = ttk.Spinbox(frame, from_=0, to=100, command=lambda: print(spinbox_value.get()), textvariable=spinbox_value)
spinbox.pack()

n = tk.StringVar()
monthchoosen = ttk.Combobox(frame, height=200, width=27, textvariable=n)
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.pack(pady=20)
monthchoosen.current()

def temp_var1():
    pass



# https://www.geeksforgeeks.org/binding-function-with-double-click-with-tkinter-listbox/
# https://www.geeksforgeeks.org/python-tkinter-listbox-widget/
def go(event):
    cs = listbox.curselection()
    w.config(text=listbox.get(cs))

listbox = tk.Listbox(frame, height=10,
                  width=15,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="yellow")


def rightClick(event):
    #https://copyprogramming.com/howto/python-remove-selected-item-from-listbox-tkinter
    items = map(int, listbox.curselection())
    for item in items:
        listbox.delete(item)

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

listbox.bind('<Double-1>', go)
listbox.bind("<Button-3>", rightClick)

# pack the widgets
listbox.pack()

w = ttk.Label(frame, text='Default')
w.pack()

#####################################################
##Creating Tables
# Import the required libraries
from tkinter import *
from  tkinter import ttk
ws  = Tk()
ws.title('PythonGuides')
ws.geometry('500x500')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("player_id",anchor=CENTER, width=80)
my_game.column("player_name",anchor=CENTER,width=80)
my_game.column("player_Rank",anchor=CENTER,width=80)
my_game.column("player_states",anchor=CENTER,width=80)
my_game.column("player_city",anchor=CENTER,width=80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("player_id",text="Id",anchor=CENTER)
my_game.heading("player_name",text="Name",anchor=CENTER)
my_game.heading("player_Rank",text="Rank",anchor=CENTER)
my_game.heading("player_states",text="States",anchor=CENTER)
my_game.heading("player_city",text="States",anchor=CENTER)

my_game.insert(parent='',index='end',iid=0,text='',
values=('1','Ninja','101','Oklahoma', 'Moore'))
my_game.insert(parent='',index='end',iid=1,text='',
values=('2','Ranger','102','Wisconsin', 'Green Bay'))
my_game.insert(parent='',index='end',iid=2,text='',
values=('3','Deamon','103', 'California', 'Placentia'))
my_game.insert(parent='',index='end',iid=3,text='',
values=('4','Dragon','104','New York' , 'White Plains'))
my_game.insert(parent='',index='end',iid=4,text='',
values=('5','CrissCross','105','California', 'San Diego'))
my_game.insert(parent='',index='end',iid=5,text='',
values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))

my_game.pack()

ws.mainloop()
#################################################################################

main_window.mainloop()