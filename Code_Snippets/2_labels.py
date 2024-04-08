import tkinter as tk

root = tk.Tk()

# Basic Label
label1 = tk.Label(root, text="Basic Label")
label1.pack()

# Label with Font Styling
label2 = tk.Label(root, text="Label with Font Styling", font=("Arial", 20, "bold"))
label2.pack()

# Label with Background and Foreground Colors
label3 = tk.Label(root, text="Label with Colors", bg="yellow", fg="red")
label3.pack()

# Label with Padding
label4 = tk.Label(root, text="Label with Padding", padx=10, pady=10)
label4.pack()

# Label with Border
label5 = tk.Label(root, text="Label with Border", bd=2, relief="solid")
label5.pack()

# Label with Text Alignment
label6 = tk.Label(root, text="Label with Text Alignment", justify="left")
label6.pack()

# Label with Text Wrapping
label7 = tk.Label(root, text="Label with Text Wrapping", wraplength=100)
label7.pack()

label8 = tk.Label(root,
                 text="Hello, Tkinter!",
                 font=("Arial", 20, "bold"),
                 bg="yellow",
                 fg="red",
                 padx=10,
                 pady=10,
                 relief="solid",
                 bd=2,
                 anchor="nw",
                 justify="center",
                 wraplength=100)
label8.pack()

root.mainloop()