import tkinter as tk
from tkinter import ttk

TITLE_FONT = ("Consolas", 22, "bold italic")

class app(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        tk.Tk.wm_title(self, "Avengers Stonehunt")
        tk.Tk.wm_resizable(self, 0, 0)
        tk.Tk.wm_geometry(self, "500x500")
        self.width = 500
        self.height = 500
        BUTTON_FONT = ttk.Style()
        BUTTON_FONT.configure("TButton", font = ("Consolas", 12, "bold"))

        mainframe = tk.Frame(self)
        mainframe.pack(side = "top", fill = "both", expand = True)
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for page in (MainPage, AboutPage):
            frame = page(mainframe, self)
            self.frames[page] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show(MainPage)

    def show(self, frame):
        page = self.frames[frame]
        page.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainlabel = ttk.Label(self, text = "Avengers Stonehunt", font = TITLE_FONT).pack(padx = 30, pady = 15)
        newgamebutton = ttk.Button(self, text = "New Game").pack()
        joingamebutton = ttk.Button(self, text = "Join Game").pack()
        helpbutton = ttk.Button(self, text = "Help").pack()
        aboutbutton = ttk.Button(self, text = "About", command = lambda: controller.show(AboutPage)).pack(pady = (0, 15))

class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        aboutlabel = tk.Label(self, text = "About Avengers Stonehunt", font = TITLE_FONT).pack(padx = 30, pady = 15)

        bodytext = "Stonehunt is an Avengers themed game created with the intention of teaching Cybersecurity principles and processes. "
        bodytext += "It has beed developed by and for CEROC/GenCyber at TTU for use as an educational game. "
        bodytext += "The main technique used in the game is Chaffing and Winnowing. "
        bodytext += "C&W is a cryptographic way of concealing true meaning without the need for encryption. "
        bodytext += "Extra, fake data (chaff) is added to messages sent between authorized entities. The receiver then checks (winnows) for the correct messages. "
        bodytext += "This is a simple way to provide both confidentiality and integrity, both data and origin. "
        bodytext += "\nGood luck and enjoy! - devs"

        body = tk.Label(self, text = bodytext, wraplength = controller.width - 30, justify = "center").pack(padx=20)
        backbutton = ttk.Button(self, text = "Back", command = lambda: controller.show(MainPage)).pack(pady = (30,0))


gui = app()
gui.mainloop()
