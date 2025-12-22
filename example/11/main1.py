# filepath: main.py
# 匯入自定義模組
import magic_tools

# 使用模組中的函式
print(magic_tools.fire_ball("哥布林2", 55))
print(magic_tools.heal("勇者2", 85))

# 使用模組中的變數
print(f"遊戲版本：{magic_tools.GAME_VERSION}")
print(f"最高等級：{magic_tools.MAX_LEVEL}")

# 計算傷害
damage = magic_tools.calculate_damage(100, 1.5)
print(f"最終傷害：{damage}")