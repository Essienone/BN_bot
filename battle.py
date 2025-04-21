import time

from function import *

# 部署全部单位开始战斗，自定义阵型（重写函数）
def deploy_units():
    while True:
        if is_in_battle():
            break
        else:
            time.sleep(2)
    ini_unit_bar()
    time.sleep(game_react_period)
    deploy_a_unit(tank_killer_bar_image)
    time.sleep(game_react_period)
    """
    ini_unit_bar()
    deploy_a_unit(wimp_bar_image)
    time.sleep(game_react_period)
    pg.moveTo(allied_row_1_pos[2])
    time.sleep(mouse_action_period)
    pg.dragTo(allied_row_2_pos[2], duration=0.3)
    """
    time.sleep(game_react_period)
    click_battle_start_button()

# 绰克阵型（带刷单位作为参数传入）
def deploy_units_tronk(unit_image):
    while True:
        if is_in_battle():
            break
        else:
            time.sleep(2)
    ini_unit_bar()
    time.sleep(game_react_period)
    for i in range(3):
        deploy_a_unit(light_tank_bar_image)
        time.sleep(game_react_period)
    ini_unit_bar()
    deploy_a_unit(unit_image)
    time.sleep(game_react_period)
    pg.moveTo(allied_row_1_pos[4])
    time.sleep(mouse_action_period)
    pg.dragTo(allied_row_2_pos[2], duration=0.3)
    ini_unit_bar()
    for i in range(3):
        deploy_a_unit(field_agent_bar_image)
        time.sleep(game_react_period)
    time.sleep(game_react_period)
    pg.moveTo(allied_row_2_pos[4])
    time.sleep(mouse_action_period)
    pg.dragTo(allied_row_3_pos[1], duration=0.3)
    time.sleep(game_react_period)
    click_battle_start_button()

# 剑影阵型
def deploy_units_crazy_blades():
    while True:
        if is_in_battle():
            break
        else:
            time.sleep(2)
    ini_unit_bar()
    time.sleep(game_react_period)
    for i in range(3):
        deploy_a_unit(light_tank_bar_image)
        time.sleep(game_react_period)
    ini_unit_bar()
    deploy_a_unit(raptor_bar_image)
    time.sleep(game_react_period)
    pg.moveTo(allied_row_1_pos[4])
    time.sleep(mouse_action_period)
    pg.dragTo(allied_row_2_pos[2], duration=0.3)
    ini_unit_bar()
    for i in range(3):
        deploy_a_unit(field_agent_bar_image)
        time.sleep(game_react_period)
    time.sleep(game_react_period)
    pg.moveTo(allied_row_2_pos[4])
    time.sleep(mouse_action_period)
    pg.dragTo(allied_row_3_pos[1], duration=0.3)
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
def battle_tactics_green_1():
    while True:
        if is_my_turn():
            break
        else:
            time.sleep(3)
    attack_by_pos_1(allied_row_2_pos[2], skill_slot_pos[0])
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
def battle_tactics_green_2():
    # 第一轮
    while True:
        if is_my_turn():
            break
        else:
            time.sleep(3)
    attack_by_pos_1(allied_row_2_pos[2], skill_slot_pos[0])
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

# 绰克阵型公式化打法
def battle_tactics_tronk():
    # 第一轮蹭经验
    while True:
        if is_my_turn():
            break
        else:
            time.sleep(3)
    attack_by_pos_1(allied_row_2_pos[2], skill_slot_pos[0])
    while True:
        # 第k轮(k>=2)
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
        attack_by_pos_1(allied_row_2_pos[1], skill_slot_pos[1])
        # 第k+1轮
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
        attack_by_pos_1(allied_row_2_pos[3], skill_slot_pos[1])
        # 第k+2轮
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
        attack_by_pos_1(allied_row_3_pos[1], skill_slot_pos[1])
        # 第k+3轮
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
        attack_by_pos_1(allied_row_2_pos[1], skill_slot_pos[0])
        # 第k+4轮
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
        attack_by_pos_1(allied_row_2_pos[3], skill_slot_pos[0])

# 剑影阵型公式化打法
def battle_tactics_crazy_blades():
    # 第一轮速龙打刺客
    while True:
        if is_my_turn():
            break
        else:
            time.sleep(3)
    attack_by_pos_1(allied_row_2_pos[2], skill_slot_pos[0])
    while True:
        # 第k轮(k>=2)
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
        attack_by_pos_1(allied_row_2_pos[1], skill_slot_pos[1])
        # 第k+1轮
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
        attack_by_pos_1(allied_row_2_pos[3], skill_slot_pos[1])
        # 第k+2轮
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
        attack_by_pos_1(allied_row_3_pos[1], skill_slot_pos[1])
        # 第k+3~k+5轮
        for i in range(1, 4):
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
            attack_by_pos_1(allied_row_2_pos[i], skill_slot_pos[0])
        # 第k+6~k+8轮
        for i in range(1, 4):
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
            attack_by_pos_1(allied_row_1_pos[i], skill_slot_pos[0])