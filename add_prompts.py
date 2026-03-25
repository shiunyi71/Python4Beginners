import json

with open("example/HP12_example.ipynb", "r", encoding="utf-8") as f:
    data = json.load(f)

# 需要插入 prompt 的 code cell IDs 和對應的 prompt
prompts_to_add = [
    ("12fef09a", "prompt: 示範使用 read() 方法一次讀取整個檔案內容，並顯示字元數和行數"),
    ("a96535f0", "prompt: 示範使用 read(size) 方法分次讀取指定字元數的內容"),
    ("82986373", "prompt: 示範使用 readline() 方法逐行讀取，並展示如何去除換行符號"),
    ("a970ca52", "prompt: 示範用 while 迴圈和 for 迴圈兩種方式讀取檔案所有行"),
    ("35f31dcd", "prompt: 示範使用 readlines() 方法將所有行讀取成串列"),
    ("db151e7b", "prompt: 比較 read()、readline()、readlines() 三種方法的回傳類型與內容"),
    ("517c7f2e", "prompt: 說明不同檔案大小和場景下應該選擇哪種讀取方法"),
    ("TV_PxIuz0nrr", "prompt: 建立一個小練習區域，讓學生可以嘗試檔案處理的基本操作"),
    ("1ae3d830", "prompt: 建立學生成績 CSV 檔案並讀取計算各科平均和班級比較"),
    ("93df506b", "prompt: 示範使用 write() 方法以模式 w 寫入多行內容到檔案"),
    ("2a8e49f9", "prompt: 比較模式 w 覆蓋寫入與模式 a 附加寫入的差異"),
    ("74256da4", "prompt: 示範模式 a 附加寫入的用法，展示內容會接在檔案後面"),
    ("e204af14", "prompt: 示範 write() 方法回傳寫入的字元數"),
    ("c353c3c0", "prompt: 示範使用 writelines() 方法一次寫入多行內容到檔案"),
    ("15c650eb", "prompt: 展示 writelines() 沒有換行符號時的錯誤與正確寫法比較"),
    ("f9f1fa9e", "prompt: 示範三種自動加換行符號的方法：串列生成式、join()、迴圈"),
    ("a672dea9", "prompt: 示範使用 f-string 格式化寫入學生資料到檔案"),
    ("f08e020d", "prompt: 建立自動日記系統函式，自動加上時間戳記和表情符號"),
    ("32b4b651", "prompt: 建立學生成績 CSV 檔案並進行班級比較和科目分析"),
    ("bc5f43bf", "prompt: 讀取日記檔案、加上行號和裝飾後寫入新的格式化檔案"),
]

cell_id_to_index = {}
for i, cell in enumerate(data["cells"]):
    cell_id = cell.get("id", "")
    if cell_id:
        cell_id_to_index[cell_id] = i

print(f"總共有 {len(data['cells'])} 個 cells")
inserted_count = 0
for target_id, prompt_text in reversed(prompts_to_add):
    if target_id in cell_id_to_index:
        target_index = cell_id_to_index[target_id]
        new_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [prompt_text],
            "id": f"prompt-{inserted_count}"
        }
        data["cells"].insert(target_index, new_cell)
        inserted_count += 1
        print(f"OK: 在 {target_id} 前插入 prompt")
    else:
        print(f"NOT FOUND: {target_id}")

with open("example/HP12_example.ipynb", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print(f"完成！共插入 {inserted_count} 個 prompt cells")
