import tkinter as tk
from tkinter import ttk

TITLE_FONT = ("Consolas", 22, "bold italic")
ENTRY_FONT = ("Consolas", 12)
LABEL_FONT = ("Consolas", 10)

class app(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        tk.Tk.wm_title(self, "Avengers Stonehunt")
        tk.Tk.wm_resizable(self, 0, 0)
        tk.Tk.wm_geometry(self, "500x500")
        #self.width = 500
        #self.height = 500
        BUTTON_FONT = ttk.Style()
        BUTTON_FONT.configure("TButton", font = ("Consolas", 14, "bold"))

        mainframe = tk.Frame(self)
        mainframe.pack(side = "top", fill = "both", expand = True)
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for page in (MainPage, NewGamePage, JoinGamePage, HelpPage, AboutPage):
            frame = page(mainframe, self)
            self.frames[page] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show(MainPage)

    def show(self, frame):
        page = self.frames[frame]
        page.tkraise()

    def back(self, entries):
        for entry in entries:
            entry.delete(0, "end")
        self.show(MainPage)


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainlabel = ttk.Label(self, text = "Avengers Stonehunt", font = TITLE_FONT).pack(pady = 30)
        newgamebutton = ttk.Button(self, text = "New Game", command = lambda: controller.show(NewGamePage)).pack()
        joingamebutton = ttk.Button(self, text = "Join Game", command = lambda: controller.show(JoinGamePage)).pack()
        helpbutton = ttk.Button(self, text = "Help", command = lambda: controller.show(HelpPage)).pack()
        aboutbutton = ttk.Button(self, text = "About", command = lambda: controller.show(AboutPage)).pack(pady = (0, 15))

class NewGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        newgamelabel = tk.Label(self, text = "New Game", font = TITLE_FONT)
        newgamelabel.grid(
                        row = 0,
                        column = 2,
                        columnspan = 5,
                        pady = 30)
        iplabel = tk.Label(self, text = "Enter your IP address:", font = LABEL_FONT)
        iplabel.grid(
                    row = 1,
                    columnspan = 2,
                    padx = (5, 0),
                    pady = (0, 5),
                    sticky = "e")
        ipentry = ttk.Entry(self, width = 25, font = ENTRY_FONT)
        ipentry.grid(
                    row = 1,
                    column = 2,
                    columnspan = 6)
        portlabel = tk.Label(self, text = "Enter your port number:", font = LABEL_FONT)
        portlabel.grid(
                        row = 2,
                        columnspan = 2,
                        padx = (5, 0),
                        pady = (0, 5),
                        sticky = "e")
        portentry = ttk.Entry(self, width = 25, font = ENTRY_FONT)
        portentry.grid(
                        row = 2,
                        column = 2,
                        columnspan = 6)
        numplayerslabel = tk.Label(self, text = "Enter the number of players:", font = LABEL_FONT)
        numplayerslabel.grid(
                        row = 3,
                        columnspan = 2,
                        padx = (5, 0),
                        pady = (0, 5),
                        sticky = "e")
        numplayersentry = ttk.Entry(self, width = 25, font = ENTRY_FONT)
        numplayersentry.grid(row = 3,
                        column = 2,
                        columnspan = 6)
        backbutton = ttk.Button(self, text = "Back", command = lambda: controller.back({ipentry, portentry, numplayersentry}))
        backbutton.grid(
                        row = 5,
                        column = 0,
                        pady = 30)
        startbutton = ttk.Button(self, text = "Start")
        startbutton.grid(
                        row = 5,
                        column = 7,
                        padx = (20, 0),
                        pady = 30)

class JoinGamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        joingamelabel = tk.Label(self, text = "Join Game", font = TITLE_FONT)
        joingamelabel.grid(
                        row = 0,
                        column = 2,
                        columnspan = 5,
                        pady = 30)
        iplabel = tk.Label(self, text = "Enter your IP address:", font = LABEL_FONT)
        iplabel.grid(
                    row = 1,
                    columnspan = 2,
                    padx = (5, 0),
                    pady = (0, 5),
                    sticky = "e")
        ipentry = ttk.Entry(self, width = 25, font = ENTRY_FONT)
        ipentry.grid(
                    row = 1,
                    column = 2,
                    columnspan = 6)
        portlabel = tk.Label(self, text = "Enter your port number:", font = LABEL_FONT)
        portlabel.grid(
                        row = 2,
                        columnspan = 2,
                        padx = (5, 0),
                        pady = (0, 5),
                        sticky = "e")
        portentry = ttk.Entry(self, width = 25, font = ENTRY_FONT)
        portentry.grid(
                        row = 2,
                        column = 2,
                        columnspan = 6)
        backbutton = ttk.Button(self, text = "Back", command = lambda: controller.back({ipentry, portentry}))
        backbutton.grid(
                        row = 5,
                        column = 0,
                        pady = 30)
        startbutton = ttk.Button(self, text = "Start")
        startbutton.grid(
                        row = 5,
                        column = 7,
                        padx = (20, 0),
                        pady = 30)

class HelpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        helplabel = tk.Label(self, text = "Help Page", font = TITLE_FONT).pack(pady = 30)
        backbutton = ttk.Button(self, text = "Back", command = lambda: controller.show(MainPage)).pack()

class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        aboutlabel = tk.Label(self, text = "About Avengers Stonehunt", font = TITLE_FONT).pack(padx = 30, pady = 30)

        bodytext = "Stonehunt is an Avengers themed game created with the intention of teaching Cybersecurity principles and processes. "
        bodytext += "It has beed developed by and for CEROC/GenCyber at TTU for use as an educational game. "
        bodytext += "The main technique used in the game is Chaffing and Winnowing. "
        bodytext += "C&W is a cryptographic way of concealing true meaning without the need for encryption. "
        bodytext += "Extra, fake data (chaff) is added to messages sent between authorized entities. The receiver then checks (winnows) for the correct messages. "
        bodytext += "This is a simple way to provide both confidentiality and integrity, both data and origin. "
        bodytext += "\nGood luck and enjoy! - devs"

        body = tk.Label(self, text = bodytext, wraplength = controller.winfo_reqwidth() + 100, justify = "center").pack(padx=20)
        backbutton = ttk.Button(self, text = "Back", command = lambda: controller.show(MainPage)).pack(pady = (30,0))

gui = app()
gui.mainloop()
