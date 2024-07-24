"""Solver for the Unblock game in HamsterKombat by https://t.me/Zhidky"""
import time
import os

from logger import logger as log
from logger import LANG, get_msg
import utils
import solver


def start_solver(X_vals, Y_vals, x_cords, y_cords):
    t0 = time.time()
    utils.get_screenshot()
    t1 = time.time()
    
    start_config = solver.get_start_config(X_vals, Y_vals)
    t2 = time.time()
    if start_config is None:
        raise solver.InvalidGrid
    log.info(get_msg("game.lvl", LANG))

    swipes = solver.solve(start_config)
    # log.info(f"swipes: {swipes}")
    if swipes is None:
        raise solver.InvalidGrid
    log.info(get_msg("solve.game", LANG))
    t3 = time.time()

    swipes_cmds = [utils.get_cmd(swipe, x_cords, y_cords) for swipe in swipes]
    # log.info(move_cmds)
    # time.sleep(5) # for test
    log.info(get_msg("need.swipes", LANG).format(len(swipes_cmds)))
    utils.start_swipes(swipes_cmds)
    t4 = time.time()

    utils.print_stats(
        screen_time=t1-t0,
        init_time=t2-t1,
        solve_time=t3-t2,
        run_time=t4-t3
    )
    if os.path.exists('screen_hm.png'):
        os.remove("screen_hm.png")


def main(target_size):
    X_vals, Y_vals = utils.adjust_coords(target_size, for_color=True)
    x_cords, y_cords = utils.adjust_coords(target_size, for_color=False)

    while True:
        try:
            start_solver(X_vals, Y_vals, x_cords, y_cords)
        except solver.InvalidGrid:
            log.info(get_msg("grid.error", LANG))
        except solver.ScreenshotNotFound:
            log.info(get_msg("screenshot.error", LANG))
        except Exception as e:
            log.error(e)
        time.sleep(1)


if __name__ == "__main__":
    target_size = utils.get_screen_size()
    if target_size:
        main(target_size)
    else:
        input(get_msg("exit", LANG))
