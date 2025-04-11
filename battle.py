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
    # deploy_a_unit(tank_killer_bar_image)
    deploy_a_unit(raptor_bar_image)
    time.sleep(game_react_period)
    click_battle_start_button()
    """
    if is_in_battle():
        ini_unit_bar()
        time.sleep(game_react_period)
        deploy_a_unit(tank_killer_bar_image)
        time.sleep(game_react_period)
        click_battle_start_button()
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        raise Exception("脚本执行异常：在非战斗场景中不能部署")
    """


# 格林镇单位单刷小黄，一轮不死就撤退
def battle_tactics_1(unit_battle_image):
    while True:
        if is_my_turn():
            break
        else:
            time.sleep(4)
    try:
        location = pg.locateOnScreen(unit_battle_image, confidence=0.6)
    except pg.ImageNotFoundException:
        """
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        raise Exception("图像识别异常：未能找到tk")
        """
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        # pg.screenshot(f'record/unrecognizedUnit_{current_time}.png')
        retreat()
    else:
        time.sleep(mouse_action_period)
        pg.moveTo(location)
        time.sleep(mouse_action_period)
        pg.mouseDown()
        time.sleep(mouse_action_period)
        pg.mouseUp()
        # print("选中")
    time.sleep(game_react_period)
    try:
        location = pg.locateOnScreen(enemy_shock_troop_yellow_image, confidence=0.4)
    except pg.ImageNotFoundException:
        """
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        raise Exception("图像识别异常：未能找到有效目标")
        """
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        # pg.screenshot(f'record/unrecognizedST_{current_time}.png')
        retreat()
        return
    else:
        # print(f'小黄位置{location}')
        time.sleep(mouse_action_period)
        pg.moveTo(location)
        time.sleep(mouse_action_period)
        pg.mouseDown()
        time.sleep(mouse_action_period)
        pg.mouseUp()
        # print("开火")
    while True:
        if is_my_turn():
            t = time.localtime()
            current_time = time.strftime("%H%M%S", t)
            # pg.screenshot(f'record/TKBadHit_{current_time}.png')
            retreat()
            break
        elif is_victory():
            pg.moveTo(battle_over_msg_btn_pos)
            time.sleep(mouse_action_period)
            pg.click(clicks=2, interval=1)
            break
        else:
            time.sleep(1)