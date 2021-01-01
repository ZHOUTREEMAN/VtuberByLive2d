# coding=utf-8
import cv2
import dlib
import pyautogui
import time

# landmark  dat
predictor_path = "shape_predictor_68_face_landmarks.dat"

# 初始化landmark
predictor = dlib.shape_predictor(predictor_path)

# 初始化dlib人脸检测器
detector = dlib.get_frontal_face_detector()

# 初始化显示窗口
win = dlib.image_window()

# opencv加载视频文件
#cap = cv2.VideoCapture('/home/ljx/ImageDatabase/WaterBar.mp4')
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print ("Unable to connect to camera !")
while cap.isOpened():

    ret, cv_img = cap.read()
    if cv_img is None:
        break

    # RGB TO BGR
    img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)

    dets = detector(img, 0)
    print("Number of faces detected: {}".format(len(dets)))
    shapes = []
    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, d.left(), d.top(), d.right(), d.bottom()))
        if d.left()>300:
            pyautogui.click(340, 800,button='left')

        if d.left()<200:
            pyautogui.click(1320, 800, button='left')
        shape = predictor(img, d)
        shapes.append(shape)

# Draw the face landmarks on the screen.
    win.clear_overlay()
    win.set_image(img)
    if len(shapes)!= 0 :
        for i in range(len(shapes)):
            win.add_overlay(shapes[i])
    win.add_overlay(dets)
cap.release()
