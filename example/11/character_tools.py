# filepath: character_tools.py
"""角色管理工具"""

def create_character(name, job, level=1):
    """創建角色"""
    return {
        "name": name,
        "job": job,
        "level": level,
        "hp": 100 * level,
        "mp": 50 * level
    }

def level_up(character):
    """角色升級"""
    character["level"] += 1
    character["hp"] = 100 * character["level"]
    character["mp"] = 50 * character["level"]
    print(f"🎉 {character['name']} 升到 Lv.{character['level']}！")
    return character

def show_status(character):
    """顯示角色狀態"""
    print(f"\n{'='*40}")
    print(f"⚔️  角色：{character['name']}")
    print(f"🎭 職業：{character['job']}")
    print(f"⭐ 等級：Lv.{character['level']}")
    print(f"❤️  HP：{character['hp']}")
    print(f"💙 MP：{character['mp']}")
    print(f"{'='*40}\n")