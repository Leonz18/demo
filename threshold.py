__author__ = 'z84105425'
# -*- coding:utf-8 -*-

import cv2

class Threshold(object):
    """
    用于自动计算阈值
    """
    
    def __init__(self, width, height, threshold_1, threshold_2):
        print("初始化...")
        self.width = width
        self.height = height
        self.threshold_1 = threshold_1
        self.threshold_2 = threshold_2

    def get_thresh_1(self, img):
        hist0 = cv2.calcHist([img],[0],None,[256],[0,256])
        sum = 0.0
        for i in range(255, 0, -1):
            sum += hist0[i]
            if sum / self.width/self.height >= self.threshold_1:
                break
        return i

    def get_thresh_2(self, img):
        hist0 = cv2.calcHist([img],[0],None,[256],[0,256])
        sum = 0.0
        for i in range(255, 0, -1):
            sum += hist0[i]
            if sum / self.width/self.height >= self.threshold_2:
                break
        return i