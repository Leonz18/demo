__author__ = 'z84105425'
# -*- coding:utf-8 -*-

import cv2
from threshold import Threshold
from perspective_transform import PerspectiveTransform

if __name__ == '__main__':
    image_path = "bios.jpg"
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 获取阈值
    th = Threshold(gray.shape[1], gray.shape[0], 0.83, 0.03)
    thresh_1 = th.get_thresh_1(gray)
    thresh_2 = th.get_thresh_2(gray)

    # 二值化
    ret1, binary1 = cv2.threshold(gray, thresh_1, 255, cv2.THRESH_BINARY)
    ret2, binary2 = cv2.threshold(gray, thresh_2, 255, cv2.THRESH_BINARY)
    cv2.namedWindow("binary1", 0)
    cv2.namedWindow("binary2", 0)
    cv2.imshow("binary1", binary1)
    cv2.imshow("binary2", binary2)
    cv2.imwrite('binary1.jpg', binary1)
    cv2.waitKey(0)

    # 透视变换
    pt = PerspectiveTransform(10000)
    pt.perspective_transform(img, binary1)