import tkinter as tk

# 建立主視窗
window = tk.Tk()
window.title("簡單的Tkinter範例")
window.geometry("300x100")  # 設定視窗大小

# 建立一個標籤元件，顯示文字
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=20)  # 放置標籤並加上上下間距

# 啟動事件迴圈
window.mainloop()
