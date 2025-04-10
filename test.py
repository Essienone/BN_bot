import keyboard
from battle import *
from map import *


def test():
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
        green_lumber(scroll_flag)
        time.sleep(2)
        deploy_units()
        time.sleep(2)
        battle_tactics_1()




def main():
    # 开始快捷键为alt+c
    print("开始执行脚本...")
    keyboard.add_hotkey("alt+c", test)
    # 结束快捷键为alt+v
    keyboard.wait("alt+v")

if __name__ == '__main__':
    main()