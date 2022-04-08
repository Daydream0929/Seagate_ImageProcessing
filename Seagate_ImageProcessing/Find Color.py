# 点击图片即可获得其像素点的 BGR GRAY HSV 的值

import cv2 as cv

img = cv.imread('original.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

def mouse_click(event, x, y, flags, para):
    if event == cv.EVENT_LBUTTONDOWN:  # 左边鼠标点击
        print('PIX:', x, y)
        print("BGR:", img[y, x])
        print("GRAY:", gray[y, x])
        print("HSV:", hsv[y, x])

if __name__ == '__main__':
    cv.namedWindow("img")
    cv.setMouseCallback("img", mouse_click)
    while True:
        cv.imshow('img', img)
        if cv.waitKey() == ord('q'): #键入q退出
            break
    cv.destroyAllWindows()