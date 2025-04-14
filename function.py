import cv2
import pyautogui as pg
import time
from config import *

# force use of ImageNotFoundException
pg.useImageNotFoundException()

# 点击地图中的攻击按钮
def click_attack_button():
    time.sleep(mouse_action_period)
    pg.moveTo(map_attack_btn_pos)
    time.sleep(mouse_action_period)
    pg.click(clicks=2, interval=0.1)

# 识别攻击位置并确认
def click_attack_confirm_button():
    try:
        location = pg.locateOnScreen(map_attack_confirm_image, confidence=0.6)
    except pg.ImageNotFoundException:
        raise Exception("图像识别异常：未能识别到攻击位置确认按钮")
    else:
        time.sleep(mouse_action_period)
        pg.moveTo(location)
        time.sleep(mouse_action_period)
        pg.click(clicks=2, interval=0.1)

# 点击开始战斗按钮
def click_battle_start_button():
    time.sleep(mouse_action_period)
    pg.moveTo(battle_fight_btn_pos)
    time.sleep(mouse_action_period)
    pg.click(clicks=2, interval=0.1)

# 单位栏回到最左侧，便于从头遍历
def ini_unit_bar():
    try:
        pg.locateOnScreen(unit_bar_index_image, confidence=0.6)
    except pg.ImageNotFoundException:
        time.sleep(mouse_action_period)
        pg.moveTo(unit_bar_pos)
        time.sleep(mouse_action_period)
        pg.scroll(100)

# 遍历单位栏，根据图像识别并部署该单位
def deploy_a_unit(unit_image):
    while True:
        try:
            location = pg.locateOnScreen(unit_image, confidence=0.6)
        except pg.ImageNotFoundException:
            time.sleep(mouse_action_period)
            pg.moveTo(unit_bar_pos)
            time.sleep(mouse_action_period)
            pg.scroll(-100)
        else:
            time.sleep(mouse_action_period)
            pg.moveTo(location)
            time.sleep(mouse_action_period)
            pg.click()
            break

# 通过pass按钮判断是否进战
def is_in_battle():
    try:
        pg.locateOnScreen(in_battle_pass_image, confidence=0.6)
    except pg.ImageNotFoundException:
        return False
    else:
        return True

# 通过攻击按钮判断是否出图
def is_in_map():
    try:
        pg.locateOnScreen(map_attack_image, confidence=0.6)
    except pg.ImageNotFoundException:
        return False
    else:
        return True

# 在战斗中通过观察键判断战斗中是否为己方回合
def is_my_turn():
    pg.moveTo(battle_observe_btn1_pos)
    time.sleep(mouse_action_period)
    pg.click(clicks=2, interval=0.1)
    try:
        pg.locateOnScreen(in_battle_pass_image, confidence=0.6)
    except pg.ImageNotFoundException:
        time.sleep(1)
        pg.moveTo(battle_observe_btn2_pos)
        pg.click(clicks=2, interval=0.1)
        return True
    else:
        return False

# 判断战斗是否胜利
def is_victory():
    try:
        pg.locateOnScreen(victory_msg_image, confidence=0.6)
    except pg.ImageNotFoundException:
        return False
    else:
        return True

# 撤退返回地图
def retreat():
    if is_in_battle():
        pg.moveTo(battle_retreat_btn_pos)
        time.sleep(mouse_action_period)
        pg.click(clicks=2, interval=1)
        while True:
            try:
                pg.locateOnScreen(defeat_msg_image, confidence=0.6)
            except pg.ImageNotFoundException:
                time.sleep(1)
            else:
                time.sleep(mouse_action_period)
                pg.moveTo(battle_over_msg_btn_pos)
                time.sleep(mouse_action_period)
                pg.click(clicks=2, interval=0.1)
                break
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        raise Exception("脚本执行异常：在非战斗场景不能撤退")
    print("retreat！")
