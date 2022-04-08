# 主函数
import cv2 as cv
import numpy as np
import sys

def read_picture(img): # 读入图片img
    img = cv.imread('C:\\Users\\941917\\Desktop\\Mycode\\' + img + '.png')
    if img is None:
        sys.exit("Could not read the image!")
    return img

def show_picture(img): # 显示图片img (按任意键退出)
    cv.imshow("Display Window (Press any key to exit!)", img)
    k = cv.waitKey(0)
    if k == ord("s"):
        return

def get_ROI(img):  # 获取图片中感兴趣的区域
    ROI = img[200:300, 300:400]  #########################重点对象
    if img is None:
        sys.exit("Could not find the ROI!")
    return ROI

def BGR_to_HSV(img):  # 讲BGR转化为HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    return hsv

# def Find_Color_Range():



p1 = read_picture("original")
hsv = BGR_to_HSV(p1)
show_picture(hsv)

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )







