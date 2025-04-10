from pyautogui import scroll

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

# 格林镇木板
def green_lumber():
    time.sleep(1)
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
        location = pg.locateOnScreen(map_green_lumber_image, confidence=0.6)
    except pg.ImageNotFoundException:
        raise Exception("图像识别异常：未能定位木板厂")
    else:
        time.sleep(mouse_action_period)
        pg.dragTo(location, mouseDownUp=True, duration=1)
        time.sleep(mouse_action_period)
        click_attack_confirm_button()
    while True:
        if is_in_battle():
            break
        else:
            time.sleep(1)
