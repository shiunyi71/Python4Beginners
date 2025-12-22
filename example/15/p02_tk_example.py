
import tkinter as tk

def say_hello():
    label.config(text="Hello, Python!")

window = tk.Tk()
window.title("我的第一個GUI")

button = tk.Button(window, text="點我", command=say_hello)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()