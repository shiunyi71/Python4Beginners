import time

def loading_animation():
  chars = "|/-\\"
  for i in range(20):
    print(f"\r載入中 {chars[i % len(chars)]}", end="")
    time.sleep(0.2)
  print("\r載入完成！✅")

loading_animation()
