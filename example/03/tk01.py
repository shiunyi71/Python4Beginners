# Tkinter溫度轉換器完整版
import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("溫度轉換器")
        self.root.geometry("300x200")

        # 輸入框
        ttk.Label(root, text="溫度:").pack(pady=5)
        self.temp_entry = ttk.Entry(root)
        self.temp_entry.pack(pady=5)

        # 按鈕
        ttk.Button(root, text="攝氏→華氏",
                  command=self.c_to_f).pack(pady=5)
        ttk.Button(root, text="華氏→攝氏",
                  command=self.f_to_c).pack(pady=5)

        # 結果顯示
        self.result_label = ttk.Label(root, text="結果將顯示在這裡")
        self.result_label.pack(pady=10)

    def c_to_f(self):
        try:
            celsius = float(self.temp_entry.get())
            fahrenheit = celsius * 9/5 + 32
            self.result_label.config(
                text=f"{celsius}°C = {fahrenheit:.1f}°F"
            )
        except ValueError:
            self.result_label.config(text="請輸入有效數字！")

    def f_to_c(self):
        try:
            fahrenheit = float(self.temp_entry.get())
            celsius = (fahrenheit - 32) * 5/9
            self.result_label.config(
                text=f"{fahrenheit}°F = {celsius:.1f}°C"
            )
        except ValueError:
            self.result_label.config(text="請輸入有效數字！")

# 執行程式
if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()

print("Tkinter 溫度轉換器類別已定義完成")
print("若要執行GUI，請取消註解最後三行程式碼")
