import random
import tkinter
from tkinter import font, StringVar, IntVar, scrolledtext, END, messagebox, filedialog
from PIL import ImageTk, Image


#Define root window
root = tkinter.Tk()
root.title('Notepad')
# root.iconbitmap('pad.ico')
root.geometry('600x600')
root.resizable(0,0)

#Define fonts and colors
text_color = '#fffacd'
menu_color = '#dbd9db'
root_color = '#6c809a'
root.config(bg=root_color)

#Define functions
def change_font(event):
    '''Change the given font based off dropbox option'''
    if font_option.get() == 'none':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_option.get())

    #Change font style
    input_text.config(font=my_font)

def new_note():
    '''Create a new note which essentiallly clears the screen'''
    #Use a messagebox to ask for a new note
    question = messagebox.askyesno("New note", "Are you sure you want to start a new note?")
    if question == 1:
    #ScrolledText widget starting index is 1.0 not 0.
        input_text.delete('1.0', END)

def close_note():
    '''closes the note which quots the program'''
    question = messagebox.askyesno("Close Note", "Are you sure you want to close the note?")
    if question == 1:
        root.destroy()

#Define frames
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

def save_note():
    '''Save the given note. First three lines are saved as font family, font size, and font option.'''
    #Use file dialog to get location and name of where/what to save the file as.
    save_name = filedialog.asksaveasfilename(initialdir='./', title='Save note', filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
    with open(save_name, 'w') as f:
        #First three lines of save file are font_family, font_size, and font_option. Font_size must be string not int to write to an int.
        f.write(font_family.get() + '\n')
        f.write(str(font_size.get()) +'\n')
        f.write((font_option.get()) + '\n')

        #Write remaining text in field to the file
        f.write(input_text.get('1.0', END))


def open_note():
    '''Open a previously saved note. First three lines of note are font family, font size, and font options. First set the font, then load the text'''
    #Use filedialog to get location and directory of note file
    open_name = filedialog.askopenfilename(initialdir='./', title="Open Note", filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
    with open(open_name, 'r') as f:
        #Clear the current text
        input_text.delete('1.0', END)

        #First three lines are font family, font size, and font option...You must strip the new line char at the end of each line
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        #Call the change font for these .set() and pass an arbitrary value - '1' in this case
        change_font(1)

        #Read the rest of the file and insert into the text field
        text = f.read()
        input_text.insert('1.0', text)

#Layout for menu frame
#Create the menu: new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame, image = new_image)
new_button.grid(row=0, column=0, padx=5, pady=5)

new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame, image = new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tkinter.Button(menu_frame, image = open_image, command=open_note)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tkinter.Button(menu_frame, image = save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tkinter.Button(menu_frame, image = close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

#create a list of fonts to use
# families =
families = []
my_fonts = []
fonts = font.families()

random_font_index = random.sample(range(0, len(fonts)), 10)
random_font_index = sorted(random_font_index)


for font in fonts:
    families.append(font)

for i in random_font_index:
    my_fonts.append(families[i])
families = my_fonts

font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set("Terminal")
#Set the width so it will fit times new roman and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

sizes = [8,10,12,14,16,18,20,24,32,48,64,72,96]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
font_size.set(12)
#set width to be constant even if its 8
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ['none', 'bold', 'italic']
font_option = StringVar()
font_option_drop = tkinter.OptionMenu(menu_frame, font_option, *options, command=change_font)
font_option.set('none')
#Set the width to be constant
font_option_drop.config(width=5)
font_option_drop.grid(row=0, column=6, padx=5, pady=5)

#Layout for the text frame
my_font = (font_family.get(), font_size.get())
#Create the input_text as a scrolltext widget so you can scroll through th text field
#Set default width and height of the textbox to be more then the window size so that on the smallest text size, the text field is constant
input_text = tkinter.scrolledtext.ScrolledText(text_frame, width=100, height=100, bg=text_color, font=my_font, undo=True)
input_text.pack()


#Run root window main loop
root.mainloop()
