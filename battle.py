import time

from function import *

# 部署全部单位开始战斗
def deploy_units():
    while True:
        if is_in_battle():
            break
        else:
            time.sleep(2)
    ini_unit_bar()
    time.sleep(game_react_period)
    deploy_a_unit(raptor_bar_image)
    time.sleep(game_react_period)
    deploy_a_unit(light_tank_bar_image)
    time.sleep(game_react_period)
    click_battle_start_button()

# 从左往右遍历敌方第一排点击
def attack_by_pos_1(unit_pos, skill_pos):
    pg.moveTo(unit_pos)
    time.sleep(mouse_action_period)
    pg.mouseDown()
    time.sleep(mouse_action_period)
    pg.mouseUp()
    time.sleep(mouse_action_period)
    pg.moveTo(skill_pos)
    time.sleep(mouse_action_period)
    pg.mouseDown()
    time.sleep(mouse_action_period)
    pg.mouseUp()
    time.sleep(mouse_action_period)
    for row_pos in enemy_row_1_pos:
        pg.moveTo(row_pos)
        time.sleep(mouse_action_period)
        pg.mouseDown()
        time.sleep(mouse_action_period)
        pg.mouseUp()
        time.sleep(mouse_action_period)

# 格林镇单位单刷小黄，一轮不死就撤退
def battle_tactics_1():
    while True:
        if is_my_turn():
            break
        else:
            time.sleep(4)
    attack_by_pos_1(allied_row_1_pos[2], skill_slot_pos[0])
    while True:
        if is_my_turn():
            t = time.localtime()
            current_time = time.strftime("%H%M%S", t)
            # pg.screenshot(f'record/TKBadHit_{current_time}.png')
            print("unable to eliminate")
            retreat()
            return
        elif is_victory():
            pg.moveTo(battle_over_msg_btn_pos)
            time.sleep(mouse_action_period)
            pg.click(clicks=2, interval=1)
            return
        else:
            time.sleep(1)

# 格林镇单刷小黄，一轮带蹭经验，两轮轮不死就撤退（待优化）
def battle_tactics_2():
    # 第一轮
    while True:
        if is_my_turn():
            break
        else:
            time.sleep(4)
    attack_by_pos_1(allied_row_1_pos[3], skill_slot_pos[0])
    # 第二轮
    while True:
        if is_my_turn():
            break
        elif is_victory():
            pg.moveTo(battle_over_msg_btn_pos)
            time.sleep(mouse_action_period)
            pg.click(clicks=2, interval=1)
            return
        else:
            time.sleep(1)
    attack_by_pos_1(allied_row_1_pos[2], skill_slot_pos[0])
    while True:
        if is_my_turn():
            t = time.localtime()
            current_time = time.strftime("%H%M%S", t)
            # pg.screenshot(f'record/TKBadHit_{current_time}.png')
            print("unable to eliminate")
            retreat()
            return
        elif is_victory():
            pg.moveTo(battle_over_msg_btn_pos)
            time.sleep(mouse_action_period)
            pg.click(clicks=2, interval=1)
            return
        else:
            time.sleep(1)
