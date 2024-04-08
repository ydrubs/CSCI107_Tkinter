import tkinter as tk

# Create a window
root = tk.Tk()

# Set the title of the window
root.title("My Tkinter Window")

# Set the geometry of the window (width x height + x_offset + y_offset)
root.geometry('500x500+100+100')

# Set the window's background color
root.config(bg='lightblue')

# Prevent the window from being resizable
root.resizable(0, 0)

# Set the minimum size of the window
root.minsize(300, 300)

# Set the maximum size of the window
root.maxsize(700, 700)

# Set an icon for the window (replace 'icon.ico' with the path to your icon file)
# root.iconbitmap('icon.ico')

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Run the Tkinter event loop
root.mainloop()