# filepath: magic_tools.py
"""
魔法工具模組
提供各種實用的魔法函式
"""

def fire_ball(target, power=30):
    """火球術"""
    damage = power * 1.5
    return f"🔥 對{target}造成{damage}點火焰傷害！"

def heal(target, amount=50):
    """治療術"""
    return f"✨ 為{target}恢復{amount}點HP！"

def calculate_damage(base, multiplier=1.0):
    """傷害計算"""
    return int(base * multiplier)

# 模組級別的變數
GAME_VERSION = "1.0.0"
MAX_LEVEL = 99

# 測試程式碼（只有直接執行此檔案才會執行）
if __name__ == "__main__":
    print("測試魔法工具模組...")
    print(fire_ball("哥布林", 50))
    print(heal("勇者", 80))