from tkinter import *
from tkinter import ttk
from Grid import Grid
window = Tk()
frm = ttk.Frame(window)
frm.grid()
title = ttk.Label(frm, text = "TIC TAC TOE", style = "secondary.Inverse.TLabel", font = ("Calibri", 40, 'bold'))
title.grid(column = 0, row = 0, columnspan=3)
x = StringVar(frm, "X")
o = StringVar(frm, "O")
ttk.Style().configure("TButton", font=("Calibri", 50, "bold"))
player = {"is_turn": True, "mark": "X"}
game = Grid()

def buttonClick(buttonIndex):
    if player["is_turn"]:
        player["is_turn"] = not player["is_turn"]
        buttons = (button1, button2, button3, button4, button5, button6, button7, button8, button9)
        game.cells[buttonIndex].set_value("X")
        game.play("O")
        for i in range(len(buttons)):
            current_cell = game.cells[i]
            cell_value = current_cell.get_value()
            if cell_value:
                buttons[i].configure(textvariable = x if cell_value == x.get() else o, state = DISABLED)
        player["is_turn"] = not player["is_turn"]
    

button1 = ttk.Button(frm, padding=50, command=lambda: buttonClick(0))
button1.grid(column=0, row=1)
button2 = ttk.Button(frm, padding=50, command=lambda: buttonClick(1))
button2.grid(column=1, row=1)
button3 = ttk.Button(frm, padding=50, command=lambda: buttonClick(2))
button3.grid(column=2, row=1)
button4 = ttk.Button(frm, padding=50, command=lambda: buttonClick(3))
button4.grid(column=0, row=2)
button5 = ttk.Button(frm, padding=50, command=lambda: buttonClick(4))
button5.grid(column=1, row=2)
button6 = ttk.Button(frm, padding=50, command=lambda: buttonClick(5))
button6.grid(column=2, row=2)
button7 = ttk.Button(frm, padding=50, command=lambda: buttonClick(6))
button7.grid(column=0, row=3)
button8 = ttk.Button(frm, padding=50, command=lambda: buttonClick(7))
button8.grid(column=1, row=3)
button9 = ttk.Button(frm, padding=50, command=lambda: buttonClick(8))
button9.grid(column=2, row=3)
window.mainloop()

