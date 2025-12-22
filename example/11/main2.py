# filepath: main.py
"""主程式：整合所有模組"""

import magic_tools
import character_tools

# 創建角色
hero = character_tools.create_character("亞瑟", "騎士", 5)
character_tools.show_status(hero)

# 使用魔法
print(magic_tools.fire_ball("暗黑騎士", 60))
print(magic_tools.heal(hero["name"], 150))

# 角色升級
hero = character_tools.level_up(hero)
character_tools.show_status(hero)