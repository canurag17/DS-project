# 1 call host
# 2 call join
# 3 exit
from tkinter import *
import server as Ser
import client as Cli

button = Tk()
button.title("Battleship option")
button.resizable(width=False, height=False)
button.geometry()

bt_host = Button(button, text="Host", font=('Arial', 12), width=30, height=2, command=Ser.click_host)
bt_host.pack()
bt_join = Button(button, text="Join", font=('Arial', 12), width=30, height=2, command=Cli.click_join)
bt_join.pack()

button.mainloop()
