# Example from: https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

import tkinter as tk
from tkinter import ttk

class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SidePage, CompletionScreen, CompletionScreen2):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()
        self.resizable(1,1)


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Adding some layout - my code from four-quadrants.py file
        frame = tk.Frame(self, height='200', width='200', bg='blue')
        frame.pack()

        quad1 = tk.Frame(frame, height='150', width='150')
        quad1.grid(row=0, column=0, padx=5, pady=5)
        quad2 = tk.Frame(frame, height='150', width='150', bg='red')
        quad2.grid(row=0, column=1, padx=5, pady=5)
        quad3 = tk.Frame(frame, height='150', width='150', bg='yellow')
        quad3.grid(row=1, column=0, padx=5, pady=5)
        quad4 = tk.Frame(frame, height='150', width='150', bg='purple')
        quad4.grid(row=1, column=1, padx=5, pady=5)

        quad1.propagate(False)
        quad3.pack_propagate(False)
        quad4.pack_propagate(False)
        # tkinter.Button(quad2, text="Press Me").pack()
        tk.Label(quad1, text="hello").pack(pady=60)
        tk.Label(quad2, text="hello").pack(pady=60)
        tk.Label(quad3, text="hello", bg='yellow').pack(pady=60)
        tk.Label(quad4, text="hello").pack(pady=60)

        # Back to example code
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="top", fill=tk.X)


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Go to the ANOTHER Completion Screen")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(CompletionScreen2)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


# More of my code
class CompletionScreen2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()