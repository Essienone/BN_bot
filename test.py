import keyboard
from battle import *
from map import *

def auto_bot():
    scroll_flag = False
    while True:
        """
        while True:
            if is_in_map():
                # green_default()
                green_lumber()
                break
            else:
                time.sleep(1)
        """
        green_attack(scroll_flag, map_green_lumber_image)
        time.sleep(2)
        deploy_units()
        time.sleep(2)
        battle_tactics_2()
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        print(current_time)

def test():
    # attack_by_pos_1(allied_row_1_pos[2], skill_slot_pos[0])
    pg.moveTo(allied_row_1_pos[3])
    time.sleep(mouse_action_period)
    pg.dragTo(allied_row_2_pos[2], duration=0.5)

def main():
    # 开始快捷键为alt+c
    print("开始执行脚本...")
    keyboard.add_hotkey("alt+c", auto_bot)
    # 结束快捷键为alt+v
    keyboard.wait("alt+v")

if __name__ == '__main__':
    main()