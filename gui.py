import math
import os
import sys
import tkinter as tk
from tkinter import filedialog as fd


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_file() -> str:
    filetypes = (('Excel files', '*.xls'), ('HTML files', '*.html'), ('All files', '*.*'))
    file = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
    return file


def show_message(title: str = "", message: str = "", button_text: str = "Continuar") -> None:
    # Create the root window
    root = tk.Tk()
    root.title(title)
    root.configure(bg="white")
    root.resizable(False, False)

    logo = tk.PhotoImage(file=resource_path("logo.png"))
    image = tk.Label(root, bg="white", image=logo)
    text = tk.Message(root, bg="white", text=f"{message}", justify="left", font=("Vollkorn", 12),
                      fg="#004000", width=500)
    title = tk.Label(root, bg="white", text=f"Quinta Compañía «Bomba Arturo Prat»", justify="left",
                     font=("Vollkorn SC", 12, "bold"), fg="#004000")
    button = tk.Button(root, text=button_text, command=root.destroy, font=("Vollkorn", 10))

    image.grid(row=0, column=0, rowspan=4, ipadx=10, sticky="N")
    title.grid(row=1, column=1, ipady=10, sticky="S")
    text.grid(row=2, column=1, ipadx=10, sticky="NW")
    button.grid(row=3, column=1, padx=10, pady=10)
    blank = tk.Message(root, bg="white")
    blank.grid(row=0, column=1)

    root.attributes("-topmost", True)
    root.update()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = root.winfo_width()
    h = root.winfo_height()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2) - 100
    root.geometry("+%d+%d" % (x, y))

    root.mainloop()


def show_options(options: list, title: str = "", message: str = "") -> str:
    # Create the root window
    root = tk.Tk()
    root.title(title)
    root.configure(bg="white")
    root.resizable(False, False)

    logo = tk.PhotoImage(file=resource_path("logo.png"))
    image = tk.Label(root, bg="white", image=logo)
    text = tk.Message(root, bg="white", text=f"{message}", justify="left", font=("Vollkorn", 12),
                      fg="#004000", width=500)
    title = tk.Label(root, bg="white", text=f"Quinta Compañía «Bomba Arturo Prat»", justify="left",
                     font=("Vollkorn SC", 12, "bold"), fg="#004000")

    image.grid(row=0, column=0, rowspan=4, ipadx=10, sticky="N")
    title.grid(row=1, column=1, ipady=10, sticky="S")
    text.grid(row=2, column=1, ipadx=10, sticky="NW")

    buttons = []
    frame = tk.Frame(root)
    frame.configure(bg="white")
    frame.grid(row=3, column=1, padx=10, pady=10)

    blank = tk.Message(root, bg="white")
    blank.grid(row=0, column=1)

    def button_click(txt: str):
        global to_return
        to_return = txt
        root.destroy()

    for i in range(len(options)):
        buttons.append(tk.Button(frame, text=options[i], width=8, font=("Vollkorn", 10)))
    for n, button in enumerate(buttons):
        pack_to = n // 5
        button.configure(command=lambda txt=button.cget("text"): button_click(txt))
        button.grid(row=pack_to, column=n % 5, padx=5, pady=5, sticky="N")

    root.attributes("-topmost", True)
    root.update()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = root.winfo_width()
    h = root.winfo_height()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2) - 100
    root.geometry("+%d+%d" % (x, y))

    root.mainloop()
    return to_return


def show_menu(options: list, title: str = "", message: str = "") -> str:
    # Create the root window
    root = tk.Tk()
    root.title(title)
    root.configure(bg="white")
    root.resizable(False, False)

    logo = tk.PhotoImage(file=resource_path("logo.png"))
    image = tk.Label(root, bg="white", image=logo)
    text = tk.Message(root, bg="white", text=f"{message}", justify="left", font=("Vollkorn", 12),
                      fg="#004000", width=500)
    title = tk.Label(root, bg="white", text=f"Quinta Compañía «Bomba Arturo Prat»", justify="left",
                     font=("Vollkorn SC", 12, "bold"), fg="#004000")

    image.grid(row=0, column=0, rowspan=4, ipadx=10, sticky="N")
    title.grid(row=1, column=1, ipady=10, sticky="S")
    text.grid(row=2, column=1, ipadx=10, sticky="NW")

    buttons = []
    frame = tk.Frame(root)
    frame.configure(bg="white")
    frame.grid(row=3, column=1, padx=10, pady=10)

    blank = tk.Message(root, bg="white")
    blank.grid(row=0, column=1)

    def button_click(opt: int):
        global to_return
        to_return = opt
        root.destroy()

    for i in range(len(options)):
        buttons.append(tk.Button(frame, text=options[i], width=50, font=("Vollkorn", 10)))
    for n, button in enumerate(buttons):
        button.configure(command=lambda opt=n: button_click(opt))
        button.grid(row=n, column=0, padx=5, pady=5, sticky="N")

    root.attributes("-topmost", True)
    root.update()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = root.winfo_width()
    h = root.winfo_height()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2) - 100
    root.geometry("+%d+%d" % (x, y))

    root.mainloop()
    return to_return


if __name__ == "__main__":
    print("Only for use as a module")
