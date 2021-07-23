import tkinter as tk

app = tk.Tk()
app.geometry('400x500')
app.title("ArmStrong")     # Add a title


# 这个index是一个Int
game_index = tk.IntVar()

# variable 参数必须要
rdioOne = tk.Radiobutton(app, text='R6S',
                         variable=game_index, value=0)
rdioTwo = tk.Radiobutton(app, text='PUBG',
                         variable=game_index, value=1)
rdioThree = tk.Radiobutton(app, text='COD',
                           variable=game_index, value=2)

rdioOne.grid(column=0, row=0, sticky="W")
rdioTwo.grid(column=0, row=1, sticky="W")
rdioThree.grid(column=0, row=2, sticky="W")

#
labelValue = tk.Label(app, textvariable=game_index)

labelValue.grid(column=2, row=0, sticky="E", padx=40)

app.mainloop()
