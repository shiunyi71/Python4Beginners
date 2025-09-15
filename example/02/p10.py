import time

# 獲取當前時間
current_time = time.time()

print(time.localtime(current_time))
print(time.gmtime(current_time))

# 格式化時間顯示
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
print("現在時間：", formatted_time)
