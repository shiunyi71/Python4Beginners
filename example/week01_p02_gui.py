import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("範例程式")
        self.root.geometry("400x300")
        
        # 建立標籤
        self.label1 = tk.Label(root, text="歡迎使用Tkinter範例程式", font=("Arial", 14))
        self.label1.pack(pady=10)
        
        # 建立輸入框
        self.label2 = tk.Label(root, text="請輸入您的名字:")
        self.label2.pack(pady=5)
        
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)
        
        # 建立按鈕
        self.button1 = tk.Button(root, text="問候", command=self.greet_user)
        self.button1.pack(pady=10)
        
        self.button2 = tk.Button(root, text="清除", command=self.clear_entry)
        self.button2.pack(pady=5)
        
        self.button3 = tk.Button(root, text="結束", command=self.quit_app)
        self.button3.pack(pady=5)
        
        # 顯示結果的標籤
        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)
    
    def greet_user(self):
        name = self.entry.get()
        if name:
            greeting = f"您好, {name}!"
            self.result_label.config(text=greeting)
        else:
            messagebox.showwarning("警告", "請先輸入您的名字!")
    
    def clear_entry(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
    
    def quit_app(self):
        if messagebox.askokcancel("確認", "您確定要結束程式嗎?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
