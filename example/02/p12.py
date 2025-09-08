import time
import os

hearts = ["💜", "💙", "💚", "💛", "❤️"]

for i in range(20):
  os.system('cls')  # Windows用 'cls' 
  heart = hearts[i % len(hearts)]
  print(f"\n\n      {heart} Python {heart}")
  print("    學習程式好有趣！")
  time.sleep(0.5)
