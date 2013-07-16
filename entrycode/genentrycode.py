# -*- coding:utf-8 -*-
import numpy as np
import random
import cv2


class EntryCodeGenerator:

    def __init__(self):
        self.bg_sz = (150, 50)
        random.seed()

    def genbgimg(self):
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

    def genrandstring(self, dig_bits=4):
        t = ['a'] * dig_bits
        candi = range(ord('A'), ord('Z')) + range(ord('0'), ord('9'))
        for i in range(0, dig_bits):
            up = len(candi)
            t[i] = chr(candi[random.randint(0, up - 1)])

        return ''.join(t)

    def addtext(self, im, text):
        text_sz = min(self.bg_sz[1] * 0.68, self.bg_sz[0] * 0.25 * 0.9)
        randh_limit = im.shape[0] - text_sz
        randw_limit = im.shape[1] / 4 - text_sz
        randw_limit = randw_limit * 4
        randh_limit = randh_limit * 0.5

        sz = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 4)

        fontScale = text_sz / sz[0][1]

        for i in range(0, 4):
            lorr = random.choice([-1, 1])
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            cv2.putText(
                im, text[i], (
                    max(0, i * im.shape[1] / 4 + lorr * int(
                        random.uniform(randw_limit * 0.5, randw_limit))),
                    im.shape[0] - 5 - int(
                        sz[1] * 0.5) - int(
                            random.uniform(-randh_limit, randh_limit))),
                cv2.FONT_HERSHEY_SIMPLEX, fontScale * random.uniform(0.8, 1), color, 5)

        return im

    def addnoise(self,im):
        # add line
        line_cnt = 50
        color = (8*16,8*16,8*16)
        print im.shape
        while line_cnt > 0:
            line_cnt = line_cnt-1
            x = random.randint(0,im.shape[1])
            y = random.randint(0,im.shape[0])
            x2 = random.randint(0,im.shape[1])
            y2 = random.randint(0,im.shape[0])
            cv2.line(im,(x,y),(x2,y2),color)

        cv2.imwrite('addnoise.bmp',im)
        return im


    def gen(self, cnt=1):
        ims = []
        codes = []

        while cnt > 0:
            cnt = cnt - 1
            bg = self.genbgimg()
            text = self.genrandstring()
            im = self.addtext(bg, text)
            ims.append(im)
            codes.append(text)

        return ims, codes


def test_gen_bg():
    g = EntryCodeGenerator()
    g.genbgimg()


def test_gen_string():
    g = EntryCodeGenerator()
    print g.genrandstring()

if __name__ == '__main__':
    g = EntryCodeGenerator()
    bg = g.genbgimg()
    txt = g.genrandstring()
    im = g.addtext(bg, txt)
    g.addnoise(im)

   # a, b = g.gen()
   # print type(a)
   # print len(a)
   # c, d = g.gen(2)
   # print len(c)
