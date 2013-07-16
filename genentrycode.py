# -*- coding:utf-8 -*-
import cv2
import numpy as np
import random

class EntryCodeGenerator:
	def __init__(self):
		self.bg_sz = (150,50)

	def genbgimg(self):
		np.zeros((self.bg_sz[0], self.bg_sz[1],3),np.uint8)

		random.seed(19871001)
		rnd_color_chanel = [0]*6
		for i in range(0,6):
			rnd_color_chanel[i] =  random.randint(0,30)

		bg_c_s = rnd_color_chanel[0:3]
		bg_c_e = rnd_color_chanel[3:6]

		print bg_c_s,bg_c_e


		pass


if __name__ == '__main__':
	g = EntryCodeGenerator()
	g.genbgimg()