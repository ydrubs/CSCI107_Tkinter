import tkinter as tk

def button_command():
    print("Button clicked!")

root = tk.Tk()

# Basic Button
button1 = tk.Button(root, text="Basic Button")
button1.pack()

# Button with Command
button2 = tk.Button(root, text="Button with Command", command=button_command)
button2.pack()

# Button with Font Styling
button3 = tk.Button(root, text="Button with Font Styling", font=("Arial", 20, "bold"))
button3.pack()

# Button with Background and Foreground Colors
button4 = tk.Button(root, text="Button with Colors", bg="yellow", fg="red")
button4.pack()

# Button with Padding
button5 = tk.Button(root, text="Button with Padding", padx=10, pady=10)
button5.pack()

# Basic Entry
entry1 = tk.Entry(root)
entry1.pack()

# Entry with Default Text
entry2 = tk.Entry(root)
entry2.insert(0, "Default Text")
entry2.pack()

# Entry with Font Styling
entry3 = tk.Entry(root, font=("Arial", 20, "bold"))
entry3.pack()

# Entry with Background and Foreground Colors
entry4 = tk.Entry(root, bg="yellow", fg="red")
entry4.pack()

# Entry with Width
entry5 = tk.Entry(root, width=50)
entry5.pack()

def submit_password():
    print("Password submitted!")

# Password prompt frame
password_frame = tk.Frame(root, pady=10)
password_frame.pack()

# Password label
password_label = tk.Label(password_frame, text="Password")
password_label.grid(row=0, column=0)

# Password entry box
password_entry = tk.Entry(password_frame, show="*")
password_entry.grid(row=0, column=1)

# Submit button
submit_button = tk.Button(password_frame, text="Submit", command=submit_password)
submit_button.grid(row=1, column=0, columnspan=2, sticky='ew')


#Radio Buttons
# Define a tkinter variable
selected_value = tk.IntVar()

# Create radio buttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=selected_value, value=1,
                        padx=10, pady=10, font=("Arial", 20, "bold"),
                        bg="yellow", fg="red", command=lambda: print("Option 1 selected"),
                        relief="solid", bd=2, width=20, height=2,
                        anchor="w", justify="left", wraplength=100)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Option 2", variable=selected_value, value=2,
                        padx=10, pady=10, font=("Arial", 20, "bold"),
                        bg="green", fg="black", command=lambda: print("Option 2 selected"),
                        relief="solid", bd=2, width=20, height=2,
                        anchor="w", justify="left", wraplength=100)
radio2.pack()

root.mainloop()