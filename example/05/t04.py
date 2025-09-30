import tkinter as tk

def show_name():
  # name = entry.get()
  # score = int(input("請輸入分數："))
  score = int(entry.get())
  if score >= 60:
    # print("及格！")
    label.config(text=f"你的分數是：{score}，及格！")
  else:
    label.config(text=f"你的分數是：{score}，不及格！")

window = tk.Tk()
window.title("判斷及格範例")

label_score = tk.Label(window, text="請輸入分數", font=("Arial", 20))
label_score.pack()

entry = tk.Entry(window, font=("Arial", 20))
entry.pack()

button = tk.Button(window, text="送出", command=show_name, font=("Arial", 20))
button.pack()

label = tk.Label(window, text="", font=("Arial", 20))
label.pack()

window.mainloop()
