import tkinter as tk
from PIL import Image, ImageTk

# Create a root window
root = tk.Tk()
root.geometry('500x500')  # Set the size of the root window

# Create a main frame
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Create four frames
frame1 = tk.Frame(main_frame, bg='red')
frame1.grid(row=0, column=0, sticky='nsew')

frame2 = tk.Frame(main_frame, bg='green')
frame2.grid(row=0, column=1, sticky='nsew')

frame3 = tk.Frame(main_frame, bg='blue')
frame3.grid(row=1, column=0, sticky='nsew')

frame4 = tk.Frame(main_frame, bg='yellow')
frame4.grid(row=1, column=1, sticky='nsew')

# Create a label in frame2 to display the image
image_label = tk.Label(frame2)
image_label.place(relx=0.5, rely=0.5, anchor='center')

# Create a Listbox widget in frame1
listbox = tk.Listbox(frame1, bg='yellow', fg='red', bd=5, font=("Arial", 10, "bold"),
                     height=10, width=10, relief='solid', selectmode='single')

# Add some items to the Listbox
for i in range(10):
    listbox.insert(tk.END, f"Item {i+1}")

# Place the Listbox into the frame1
listbox.place(relx=0.5, rely=0.5, anchor='center')

# Define a function to update the image
def update_image(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        try:
            if index == 0:  # Item 1 is selected
                image1 = Image.open('pics/pk.jpg')
                image2 = Image.open('pics/025.png')
                resized_image = image1.resize(image2.size) #Resize image 1 to size of image 2
                image_label.image = ImageTk.PhotoImage(resized_image)
                image_label.config(image=image_label.image)
            elif index == 1:  # Item 2 is selected
                image = Image.open('pics/025.png')
                image_label.image = ImageTk.PhotoImage(image)
                image_label.config(image=image_label.image)
            elif index == 2:  # Item 2 is selected
                image = Image.open('pics/250px-Ash_Pikachu.png')
                image_label.image = ImageTk.PhotoImage(image)
                image_label.config(image=image_label.image)
            else:  # Other item is selected
                image_label.config(image='')
        except Exception:
            image_label.config(text='Image not found')

# Bind the function to the Listbox's selection event
listbox.bind('<<ListboxSelect>>', update_image)


"""The code is configuring the grid system for the main_frame widget in Tkinter. 
The grid system is a way to organize widgets in rows and columns, similar to a table.  
The grid_rowconfigure and grid_columnconfigure methods are used to configure the properties of the grid's rows and columns. 
The weight option determines how the extra space is distributed when the window is resized. 
A higher weight means that the row or column will get a larger share of the extra space.  
In your code, all rows and columns are given an equal weight of 1. 
This means that when the window is resized, the extra space will be distributed equally among all rows and columns."""

# Configure the rows and columns of the main frame to have equal weight
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Start the tkinter event loop
root.mainloop()