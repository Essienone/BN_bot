from function import *

# 格林镇默认位置
def green_default():
    time.sleep(1)
    click_attack_button()
    time.sleep(game_react_period)
    click_attack_confirm_button()
    while True:
        if is_in_battle():
            break
        else:
            time.sleep(1)

# 格林镇攻击目标地点
def green_attack(scroll_flag, target_image):
    while True:
        if is_in_map():
            break
        else:
            time.sleep(1)
    if not scroll_flag:
        scroll_cnt = 0
        while scroll_cnt < 5:
            pg.scroll(-100)
            scroll_cnt += 1
            time.sleep(mouse_action_period)
    click_attack_button()
    time.sleep(game_react_period)
    pg.moveTo(green_start_pos)
    time.sleep(mouse_action_period)
    try:
        location = pg.locateOnScreen(target_image, confidence=0.6)
    except pg.ImageNotFoundException:
        raise Exception("图像识别异常：未能定位目标")
    else:
        time.sleep(mouse_action_period)
        pg.dragTo(location, mouseDownUp=True, duration=1)
        time.sleep(mouse_action_period)
        click_attack_confirm_button()

