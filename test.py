import time

import keyboard
from battle import *
from map import *

def green_auto_bot():
    scroll_flag = False
    while True:
        green_attack(scroll_flag, map_green_lumber_image)
        scroll_flag = True
        time.sleep(2)
        deploy_units()
        time.sleep(2)
        battle_tactics_green_2()
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        print(current_time)

def tronk_auto_bot():
    scroll_flag = False
    while True:
        tronk_attack(scroll_flag)
        scroll_flag = True
        time.sleep(2)
        deploy_units_tronk(wimp_bar_image)
        time.sleep(2)
        battle_tactics_tronk()
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        print(current_time)

def test():
    deploy_units_tronk(wimp_bar_image)

def main():
    # 开始快捷键为alt+c
    print("开始执行脚本...")
    keyboard.add_hotkey("alt+c", tronk_auto_bot)
    # 结束快捷键为alt+v
    keyboard.wait("alt+v")

if __name__ == '__main__':
    main()