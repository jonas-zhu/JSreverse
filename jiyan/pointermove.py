# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from trace import generate_mouse_trace_between_two_point
import time
import random

ls = [['move', 37, 160, 1640310350775, 'pointermove'], ['move', 93, 168, 1640310350783, 'pointermove'], ['move', 154, 177, 1640310350790, 'pointermove'], ['move', 215, 189, 1640310350799, 'pointermove'], ['move', 273, 202, 1640310350806, 'pointermove'], ['move', 323, 213, 1640310350815, 'pointermove'], ['move', 367, 229, 1640310350822, 'pointermove'], ['move', 401, 241, 1640310350830, 'pointermove'], ['move', 428, 253, 1640310350839, 'pointermove'], ['move', 443, 261, 1640310350849, 'pointermove'], ['move', 459, 270, 1640310350855, 'pointermove'], ['move', 464, 273, 1640310350863, 'pointermove'], ['move', 469, 277, 1640310350871, 'pointermove'], ['move', 472, 278, 1640310350879, 'pointermove'], ['move', 473, 279, 1640310350886, 'pointermove'], ['move', 474, 280, 1640310350895, 'pointermove'], ['move', 475, 280, 1640310350903, 'pointermove'], ['move', 476, 281, 1640310350910, 'pointermove'], ['move', 477, 281, 1640310350918, 'pointermove'], ['move', 479, 283, 1640310350926, 'pointermove'], ['move', 483, 285, 1640310350935, 'pointermove'], ['move', 486, 286, 1640310350943, 'pointermove'], ['move', 492, 289, 1640310350951, 'pointermove'], ['move', 496, 291, 1640310350958, 'pointermove'], ['move', 503, 295, 1640310350966, 'pointermove'], ['move', 508, 297, 1640310350974, 'pointermove'], ['move', 513, 301, 1640310350983, 'pointermove'], ['move', 520, 304, 1640310350990, 'pointermove'], ['move', 530, 308, 1640310350998, 'pointermove'], ['move', 536, 312, 1640310351006, 'pointermove'], ['move', 545, 315, 1640310351016, 'pointermove'], ['move', 561, 320, 1640310351022, 'pointermove'], ['move', 570, 323, 1640310351030, 'pointermove'], ['move', 575, 325, 1640310351038, 'pointermove'], ['move', 583, 327, 1640310351046, 'pointermove'], ['move', 591, 330, 1640310351054, 'pointermove'], ['move', 598, 332, 1640310351063, 'pointermove'], ['move', 603, 334, 1640310351070, 'pointermove'], ['move', 610, 336, 1640310351079, 'pointermove'], ['move', 618, 337, 1640310351086, 'pointermove'], ['move', 625, 339, 1640310351095, 'pointermove'], ['move', 633, 340, 1640310351103, 'pointermove'], ['move', 638, 341, 1640310351110, 'pointermove'], ['move', 645, 341, 1640310351118, 'pointermove'], ['move', 653, 341, 1640310351126, 'pointermove'], ['move', 666, 341, 1640310351135, 'pointermove'], ['move', 675, 341, 1640310351142, 'pointermove'], ['move', 689, 341, 1640310351151, 'pointermove'], ['move', 704, 341, 1640310351158, 'pointermove'], ['move', 711, 340, 1640310351167, 'pointermove'], ['move', 728, 340, 1640310351174, 'pointermove'], ['move', 736, 340, 1640310351183, 'pointermove'], ['move', 749, 340, 1640310351190, 'pointermove'], ['move', 761, 339, 1640310351198, 'pointermove'], ['move', 773, 339, 1640310351206, 'pointermove'], ['move', 781, 338, 1640310351214, 'pointermove'], ['move', 787, 337, 1640310351222, 'pointermove'], ['move', 791, 337, 1640310351230, 'pointermove'], ['move', 794, 336, 1640310351238, 'pointermove'], ['move', 798, 336, 1640310351246, 'pointermove'], ['move', 799, 335, 1640310351254, 'pointermove'], ['move', 801, 334, 1640310351263, 'pointermove'], ['move', 802, 334, 1640310351271, 'pointermove'], ['move', 802, 333, 1640310351287, 'pointermove'], ['move', 803, 333, 1640310351294, 'pointermove'], ['move', 805, 331, 1640310351302, 'pointermove'], ['move', 807, 330, 1640310351311, 'pointermove'], ['move', 811, 328, 1640310351318, 'pointermove'], ['move', 814, 326, 1640310351327, 'pointermove'], ['move', 817, 324, 1640310351335, 'pointermove'], ['move', 822, 321, 1640310351342, 'pointermove'], ['move', 826, 321, 1640310351351, 'pointermove'], ['move', 829, 319, 1640310351358, 'pointermove'], ['move', 833, 318, 1640310351366, 'pointermove'], ['move', 833, 317, 1640310351447, 'pointermove'], ['move', 834, 316, 1640310351454, 'pointermove'], ['move', 836, 314, 1640310351463, 'pointermove'], ['move', 841, 313, 1640310351471, 'pointermove'], ['move', 846, 311, 1640310351478, 'pointermove'], ['move', 852, 309, 1640310351487, 'pointermove'], ['move', 857, 307, 1640310351495, 'pointermove'], ['move', 863, 306, 1640310351502, 'pointermove'], ['move', 868, 306, 1640310351510, 'pointermove'], ['move', 870, 305, 1640310351519, 'pointermove'], ['move', 871, 305, 1640310351526, 'pointermove'], ['focus', 1640310351794], ['down', 871, 305, 1640310351794, 'pointerdown'], ['up', 871, 305, 1640310351910, 'pointerup']]


def get_pointermove(button_coordinate):
    # 点击出现验证码按钮的坐标
    start_coordinate = (random.randint(30, 1250), random.randint(145, 1075))
    # start_coordinate = (random.randint(0, 1), random.randint(0, 1))
    print(start_coordinate, button_coordinate)
    # 871, 305    点击出现验证码按钮的坐标
    '''
    pointermove_end = [["move", 871, 305, 1640310351526, "pointermove"],
                       ["focus", 1640310351794],
                       ["down", 871, 305, 1640310351794, "pointerdown"],
                       ["up", 871, 305, 1640310351910, "pointerup"]]
    '''
    # 生成鼠标移动轨迹
    traces = generate_mouse_trace_between_two_point(start_coordinate, button_coordinate, show=False, dense_radio=0.1)
    pointermove_traces = [['move', trace[0], trace[1], trace[2], 'pointermove'] for trace in traces[:-1]]

    now_time = int(time.time() * 1000)
    pointermove_end = [['move', button_coordinate[0], button_coordinate[1], traces[-1][2], 'pointermove'],
                       ["focus", now_time],
                       ["down", button_coordinate[0], button_coordinate[1], now_time, "pointerdown"],
                       ["up", button_coordinate[0], button_coordinate[1], now_time+random.randint(100, 200), "pointerup"]]
    pointermove_traces.extend(pointermove_end)
    return pointermove_traces


# 滑块轨迹      // 有问题，这个方法生成的轨迹过不了
def get_slide_trajectory(end_coordinate):
    start_coordinate = (0, 0)
    print(end_coordinate)
    # 生成滑块移动轨迹
    traces = generate_mouse_trace_between_two_point(start_coordinate, end_coordinate, show=False, dense_radio=1)
    print(traces)
    start_click_time = traces[0][2]
    slide_trajectory = [[trace[0], trace[1], trace[2]-start_click_time] for trace in traces]
    print(start_click_time, slide_trajectory)
    return slide_trajectory, start_click_time


if __name__ == '__main__':
    # button_coordinate = (random.randint(864, 878), random.randint(301, 313))
    # result = get_pointermove(button_coordinate)
    # print(result)
    get_slide_trajectory((87, random.randint(1, 10)))
