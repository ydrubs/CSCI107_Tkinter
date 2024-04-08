import tkinter as tk

root = tk.Tk()
root.geometry('500x500')  # Set the size of the root window

# Sidebar
sidebar = tk.Frame(root, width=80, bg='purple')
sidebar.pack(side='left', fill='y')

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

# Child frames with different background colors
frame1 = tk.Frame(main_frame, bg='red')
frame1.grid(row=0, column=0, sticky='nsew')

frame2 = tk.Frame(main_frame, bg='green')
frame2.grid(row=0, column=1, sticky='nsew')

frame3 = tk.Frame(main_frame, bg='blue')
frame3.grid(row=1, column=0, sticky='nsew')

frame4 = tk.Frame(main_frame, bg='yellow')
frame4.grid(row=1, column=1, sticky='nsew')

# Smaller frames inside each child frame
small_frame1 = tk.Frame(frame1, bg='white', width=50, height=50)
small_frame1.place(relx=0.5, rely=0.5, anchor='center')

small_frame2 = tk.Frame(frame2, bg='white', width=50, height=50)
small_frame2.place(relx=0, rely=0, anchor='nw')

small_frame3 = tk.Frame(frame3, bg='white', width=50, height=50)
small_frame3.place(relx=0.5, rely=0.5, anchor='center')

small_frame4 = tk.Frame(frame4, bg='white', width=50, height=50)
small_frame4.place(relx=0.5, rely=0.5, anchor='center')

# Create a button
button = tk.Button(frame3, text="Button", bg='SpringGreen1')

# Use the place method with all parameters
button.place(x=0, y=0,
             width=50, height=50,
             anchor='center', bordermode='inside',
             relx=0.5, rely=0.5,
             relwidth=0.5, relheight=0.5)

# Configure the rows and columns of the main frame to have equal weight
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

root.mainloop()