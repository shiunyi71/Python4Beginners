import time

def draw_cat():
  cat = [
    "     /\\_/\\  ",
    "    ( o.o ) ",
    "     > ^ <  ",
  ]
  
  print("繪製小貓中...")
  for line in cat:
    print(line)
    time.sleep(0.5)
  
  print("\n🐱 可愛的ASCII小貓完成了！")

draw_cat()
