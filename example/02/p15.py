import time
import os

def blinking_cat():
  open_eyes = [
    "     /\\_/\\  ",
    "    ( o.o ) ",
    "     > ^ <  "
  ]
  
  closed_eyes = [
    "     /\\_/\\  ",
    "    ( -.- ) ",
    "     > ^ <  "
  ]
  
  for _ in range(5):
    os.system('cls')  # Windows用 'cls'
    for line in open_eyes:
      print(line)
    time.sleep(1)
    
    os.system('cls')
    for line in closed_eyes:
      print(line)
    time.sleep(0.3)

blinking_cat()
