import cv2
import numpy as np

if __name__ == '__main__':
    cv2.namedWindow( "result" )
#цвет
color= (0,255,255)
#просто фон 3-ёх канальный 128 на 128
img = np.zeros((128,128,3), np.uint8)
#ускорение
a=0
while True:
        #фон красит в голубой
        img[:, 0:1 * 128] = (255, 140, 0)
        #рисует круг с перемещением по х на а ,по у постоянно . Радиус =20
        cv2.circle(img, (a, 64), 20, color, -1)
        a=a+1
        #если кружочек дошел до края, счетчик обнуляется
        if a>108:
            a=0
        #отображение
        cv2.imshow('result', img)
        #Ждет esc
        ch = cv2.waitKey(5)
        if ch == 27:
            break
#удаляет окно
cv2.destroyAllWindows()

