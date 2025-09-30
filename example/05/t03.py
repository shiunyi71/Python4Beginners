import tkinter as tk

def show_name():
  name = entry.get()
  label.config(text=f"你好，{name}！")

window = tk.Tk()
window.title("輸入框範例")

entry = tk.Entry(window, font=("Arial", 20))
entry.pack()

button = tk.Button(window, text="送出", command=show_name, font=("Arial", 20))
button.pack()

label = tk.Label(window, text="", font=("Arial", 20))
label.pack()

window.mainloop()
