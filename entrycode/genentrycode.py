# -*- coding:utf-8 -*-
import numpy as np
import random


class EntryCodeGenerator:

    def __init__(self):
        self.bg_sz = (150, 50)

    def genbgimg(self):
        random.seed(19871001)
        rnd_color_chanel = [0] * 6
        for i in range(0, 6):
            rnd_color_chanel[i] = random.randint(255 - 30, 255)

        bg_c_s = rnd_color_chanel[0:3]
        bg_c_e = rnd_color_chanel[3:6]

        w, h = self.bg_sz
        line_g = np.array([np.linspace(bg_c_s[0], bg_c_e[0], w), np.linspace(
            bg_c_s[1], bg_c_e[1], w), np.linspace(bg_c_s[2], bg_c_e[2], w).tolist()]).transpose()
        bg = np.zeros((h, w, 3), np.uint8)
        for i in range(0, h):
            bg[i] = line_g

        return bg


if __name__ == '__main__':
    g = EntryCodeGenerator()
    g.genbgimg()
