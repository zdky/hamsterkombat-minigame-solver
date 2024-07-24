import time
import subprocess
from subprocess import DEVNULL, PIPE
import random

from logger import logger as log
from logger import LANG, get_msg


def get_screenshot():
    screen_cmds = [
        f".\\adb shell screencap -p /sdcard/screen_hm.png",
        f".\\adb pull /sdcard/screen_hm.png",
    ]
    for cmd in screen_cmds:
        subprocess.run(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)


def start_swipes(cmds):
    for cmd in cmds:
        subprocess.run(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)
        log.info(get_msg("sended", LANG).format(cmd[18:]))
        swipe_ms = int(cmd.split()[-1]) / 1000
        time.sleep(swipe_ms + 0.1 + random.uniform(0.0010001, 0.0050001))


def fix_swipes_for_hm(move, x1, y1, x2, y2):
    """Костыль для хомяков, добавляет 50px к точкам свайпа."""
    j1, i1, j2, i2 = move
    c = 50  # Погрешность 50px

    if j1 == j2:  # горизнт.свайп (Y не меняется)
        if i1 > i2:  # Свайп влево по X
            x1 += c
            x2 -= c
        else:  # вправо по X
            x1 -= c
            x2 += c
    elif j1 > j2:  # Свайп вверх по Y
        y1 += c
        y2 -= c
    else:  # Вниз по Y
        y1 -= c
        y2 += c

    return x1, y1, x2, y2


def get_cmd(move, x_cords, y_cords):
    cmd_pattern = ".\\adb shell input swipe {} {} {} {} {}"
    j1, i1, j2, i2 = move
    dist = abs(j1 - j2) + abs(i1 - i2)
    
    x1 = x_cords[i1]
    y1 = y_cords[j1]
    x2 = x_cords[i2]
    y2 = y_cords[j2]
    
    x1, y1, x2, y2 = fix_swipes_for_hm(move, x1, y1, x2, y2)

    swipe_ms = 65*dist + random.randint(1, 20)
    return cmd_pattern.format(x1, y1, x2, y2, swipe_ms)


def get_screen_size():
    """Узнаем через adb разрешение экрана."""
    print(logs)
    log.info(get_msg("screen.size", LANG))
    try:
        res = subprocess.run(
            ["adb", "shell", "wm", "size"],
            stdout=PIPE, stderr=DEVNULL
        )
        output = res.stdout.decode("utf-8")
        if "Physical size:" in output:
            size_str = output.split("Physical size: ")[1].strip()
            width, height = map(int, size_str.split("x"))
            return [width, height]
        else:
            log.error(get_msg("connect.device", LANG))
    except Exception:
        log.error(get_msg("screen.size.err", LANG))
        return False


def adjust_coords(target_size, for_color:bool):
    """Преобразует координаты под разрешение телефона."""
    original_size = [1080, 2246]

    if for_color:
        # коры краев квадрата
        X_vals = [147, 315, 479, 649, 813, 980]
        Y_vals = [836, 1005, 1175, 1336, 1507, 1670]
        cor_type = "цвета" if LANG == "ru" else "colors"
    else:
        # от x0 +82, потом +165 до центра след.квадрата
        X_vals = [82, 247, 412, 577, 742, 907]
        # от y820 +82, далее +165 до центра след.квадрата
        Y_vals = [902, 1067, 1232, 1397, 1562, 1727]
        cor_type = "свайпа" if LANG == "ru" else "swipes"

    log.info(get_msg("coords.adj.do", LANG).format(cor_type))
    # Рассчет соотношений
    width_ratio = target_size[0] / original_size[0]
    height_ratio = target_size[1] / original_size[1]
    # Преобразуем координаты
    adjusted_X_vals = [int(x * width_ratio) for x in X_vals]
    adjusted_Y_vals = [int(y * height_ratio) for y in Y_vals]
    return adjusted_X_vals, adjusted_Y_vals


def print_stats(screen_time, init_time, solve_time, run_time):
    log.info(get_msg("stats", LANG).format(
        screen_time,
        init_time,
        solve_time,
        run_time
    ))

logs='''\033[97m
            made by\u001b[36;1m
 ____ ____ ____ ____ ____ ____ 
||Z |||h |||i |||d |||k |||y ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
\033[97m
          t.me/zhidky
\u001b[0m
'''
