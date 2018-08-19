__author__ = 'z84105425'
# -*- coding:utf-8 -*-

import cv2
import numpy as np

class PerspectiveTransform(object):
    """
    透视变换
    """
    
    pts2 = np.float32([[0, 0], [2048, 0], [2048, 1536], [0, 1536]])
    
    def __init__(self, thresh_area):
        print("初始化...")
        self.thresh_area = thresh_area
        self.size = (2048, 1536)

        
    def preprocess(self, image):
        element = cv2.getStructuringElement(cv2.MORPH_CROSS,(11,11))
        dilation = cv2.dilate(image, element, iterations=3)
        cv2.imwrite('dilation.jpg', dilation)
        return dilation
        
    def get_box_corners(self, binary):
        _, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        for i in range(0,len(contours)):
            cnt = contours[i]
            if cv2.contourArea(cnt) < self.thresh_area:
                continue
            
            # 最小外接矩阵
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
        
        # 更新角点位置
        corners = np.zeros((4, 2), np.float32)
        for b in box:
            if b[1]<1000 and b[0]<1000 :
                corners[0][0] = b[0]
                corners[0][1] = b[1]
            if b[1]<1000 and b[0]>1000:
                corners[1][0] = b[0]
                corners[1][1] = b[1]
            if b[1]>1000 and b[0]>1000:
                corners[2][0] = b[0]
                corners[2][1] = b[1]
            if b[1]>1000 and b[0]<1000:
                corners[3][0] = b[0]
                corners[3][1] = b[1]
        print(corners)
        return corners

    def perspective_transform(self, image, binary):
        # 图像预处理
        temp = self.preprocess(binary)
        # 获得屏幕的四个角点
        pts1 = self.get_box_corners(temp)
        # 生成透视变换矩阵
        M = cv2.getPerspectiveTransform(pts1, self.pts2)
        # 进行透视变换
        dst = cv2.warpPerspective(image, M, self.size)
        cv2.imwrite('dst.jpg', dst)
