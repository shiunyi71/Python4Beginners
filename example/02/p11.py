import time

print("開始倒數...")
for i in range(5, 0, -1):
  print(f"{i}...")
  time.sleep(1)  # 暫停1秒
print("時間到！🎉")
