import tkinter as tk

def say_hello():
  label.config(text="你按下了按鈕！")

window = tk.Tk()
window.title("按鈕範例")
window.geometry("300x200")

label = tk.Label(window, text="請按下按鈕", font=("Arial", 20))
label.pack()

button = tk.Button(window, text="點我", command=say_hello, font=("Arial", 20))
button.pack()

window.mainloop()