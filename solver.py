"""Core logic of the solver. Given an image, return the swipes to be performed."""
import os
import copy
import collections
import time

import matplotlib.pyplot as plt
import numpy as np

from logger import logger as log
from logger import LANG, get_msg


def read_image(screen_filename):
    image = plt.imread("{}".format(screen_filename))
    image = image[:, :, :3]
    return image


def get_type(color):
    block_red = [0.29411764, 0.15294117, 0.15294117]
    block_green = [0.149019, 0.28627, 0.16078]
    empty = [0.17254902, 0.17254902, 0.17254902]
    yellow = [0.25098039, 0.23921569, 0.16862745]
    color_types = [empty, block_red, block_green, yellow]
    final = np.argmin([np.linalg.norm(color - centre) for centre in color_types])
    # ахуэный костыль, чатжпт идет нахой
    if final in [1, 2]:
        final = 1
    elif final == 3:
        final = 2

    return final


def is_wall(line):
    grad = line[1:] - line[:-1]
    grad_norms = np.sum(grad**2, axis=1)
    return max(grad_norms) > 0.01


def get_string_rep(grid, wall_grid_x, wall_grid_y):
    string = [["" for _ in range(6)] for _ in range(6)]
    vert_counter = 0
    horiz_counter = 0

    for j in range(6):
        for i in range(6):

            if string[j][i]:
                continue

            if grid[j][i] == 0:
                string[j][i] = "e"
            elif grid[j][i] == 2:
                string[j][i] = "r"

            elif wall_grid_x[j][i]:
                string[j][i] = "v{}".format(vert_counter)
                j_temp = j + 1
                while not wall_grid_y[j_temp - 1][i]:
                    string[j_temp][i] = string[j][i]
                    j_temp += 1
                vert_counter += 1
            else:
                string[j][i] = "h{}".format(horiz_counter)
                i_temp = i + 1
                while not wall_grid_x[j][i_temp - 1]:
                    string[j][i_temp] = string[j][i]
                    i_temp += 1
                horiz_counter += 1

    return string


def print_grid(string):
    log.info(get_msg("map", LANG))
    for row in string:
        for elem in row:
            print(f"{elem:4}", end=" ")
        print("")
    print("")


def get_moves(node):
    moves = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dir_map = {
        (0, 1): ["h", "r"],
        (0, -1): ["h", "r"],
        (1, 0): "v",
        (-1, 0): "v",
    }

    empty = []
    for j in range(6):
        for i in range(6):
            if node[j][i] == "e":
                empty.append((j, i))

    for j, i in empty:
        for dy, dx in directions:
            y, x = j + dy, i + dx
            while (0 <= x < 6) and (0 <= y < 6):
                if node[y][x] != "e":
                    if node[y][x][0] in dir_map[(dy, dx)]:
                        move = (j, i, (j - y, i - x))
                        moves.append(move)
                    break
                y, x = y + dy, x + dx

    return moves


def apply_move(old_node, move):
    node = copy.deepcopy(old_node)
    j, i, direc = move
    dy, dx = direc
    label = node[j - dy][i - dx]

    j = int(j - dy)
    i = int(i - dx)
    while (0 <= j < 6) and (0 <= i < 6) and (node[j][i] == label):
        node[j][i] = "e"
        node[j + int(dy)][i + int(dx)] = label
        j = int(j - dy / abs(dy + dx))
        i = int(i - dx / abs(dy + dx))
    return node


def get_neighbors(node):
    moves = get_moves(node)
    neighbors = [apply_move(node, move) for move in moves]
    return neighbors, moves


def check_solved(node):
    solved = (node[2][4] == "r") and (node[2][5] == "r")
    return solved


class HashError(Exception):
    pass


def hashed(node):
    try:
        return "".join([" ".join(row) for row in node])
    except:
        raise HashError


class BFSError(Exception):
    pass

class TimeoutError(Exception):
    pass

class InvalidGrid(Exception):
    pass

class ScreenshotNotFound(Exception):
    pass


def get_start_config(X_vals, Y_vals):
    if not os.path.exists('screen_hm.png'):
        raise ScreenshotNotFound
    
    log.info(get_msg("screen", LANG))
    image = read_image("screen_hm.png")

    grid = get_grid(image, X_vals, Y_vals)
    if not validate_grid(grid):
        return None

    wall_grid_x, wall_grid_y = get_wall_grids(image, X_vals, Y_vals)
    start = get_string_rep(grid, wall_grid_x, wall_grid_y)
    print_grid(start)

    return start


def bfs(start):
    start_time = time.time()
    timeout = 120

    back_pointer = {}
    visited = {}
    queue = collections.deque([start])
    visited[hashed(start)] = True

    while len(queue) > 0:
        if time.time() - start_time > timeout:
            log.error(get_msg("cant.find.path", LANG).format(timeout))
            raise TimeoutError

        node = queue.popleft()
        neighbors, moves = get_neighbors(node)

        # print(f'Processing node: {node}')
        # print(f'Queue length: {len(queue)}')

        for neighbor, move in zip(neighbors, moves):
            if check_solved(neighbor):
                back_pointer[hashed(neighbor)] = node, move
                return back_pointer, neighbor

            if hashed(neighbor) in visited:
                continue
            else:
                queue.append(neighbor)
                visited[hashed(neighbor)] = True
                back_pointer[hashed(neighbor)] = node, move

    log.error(get_msg("bfs.error", LANG))
    raise BFSError


def get_path(back_pointer, start, final):
    path = [(final, None)]
    while path[-1][0] != start:
        prev_node, _ = path[-1]
        node, move = back_pointer[hashed(prev_node)]
        path.append((node, move))
    return list(reversed(path))


def get_swipes(path):
    swipes = []
    for _, move in path:
        x, y, direc = move
        dx, dy = direc
        x1, y1 = x - dx, y - dy
        x2, y2 = x, y
        swipe = (x1, y1, x2, y2)
        swipes.append(swipe)
    return swipes


def get_grid(image, X_vals, Y_vals):
    grid = [[None for _ in range(6)] for _ in range(6)]
    for i, y in enumerate(Y_vals):
        for j, x in enumerate(X_vals):
            color = image[y, x, :]
            grid[i][j] = get_type(color)
    return grid


def get_wall_grids(image, X_vals, Y_vals):
    wall_grid_x = [[True for i in range(6)] for j in range(6)]
    for j in range(6):
        for i in range(5):
            line = image[Y_vals[j], X_vals[i] : X_vals[i + 1], :]
            wall_grid_x[j][i] = is_wall(line)

    wall_grid_y = [[True for i in range(6)] for j in range(6)]
    for j in range(5):
        for i in range(6):
            line = image[Y_vals[j] : Y_vals[j + 1], X_vals[i], :]
            wall_grid_y[j][i] = is_wall(line)

    return wall_grid_x, wall_grid_y


def validate_grid(grid):
    num_red = sum([float(elem == 2) for row in grid for elem in row])
    return num_red == 2


def solve(start):
    back_pointer, final = bfs(start)
    path = get_path(back_pointer, start, final)
    swipes = get_swipes(path[:-1])
    return swipes
