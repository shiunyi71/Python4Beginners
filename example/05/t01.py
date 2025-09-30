import tkinter as tk

window = tk.Tk()
window.title("Tkinter 基本視窗")
window.geometry("300x200")

label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 20))
label.pack(pady=20)

window.mainloop()