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
        battle_tactics_green_1()
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        print(current_time)

def tronk_auto_bot():
    scroll_flag = False
    while True:
        tronk_attack(scroll_flag)
        scroll_flag = True
        time.sleep(2)
        deploy_units_tronk(tank_killer_bar_image)
        time.sleep(2)
        battle_tactics_tronk()
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        print(current_time)

def crazy_blades_auto_bot():
    scroll_flag = False
    while True:
        crazy_blades_attack(scroll_flag)
        scroll_flag = True
        time.sleep(2)
        deploy_units_crazy_blades()
        time.sleep(2)
        battle_tactics_crazy_blades()
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        print(current_time)

def test():
    a = False
    crazy_blades_attack(a)

def main():
    # 开始快捷键为alt+c
    print("开始执行脚本...")
    keyboard.add_hotkey("alt+c", crazy_blades_auto_bot)
    # 结束快捷键为alt+v
    keyboard.wait("alt+v")

if __name__ == '__main__':
    main()