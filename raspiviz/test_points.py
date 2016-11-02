import cv2

def circle(x,y):
    test = cv2.imread('snap.jpg')
    cv2.circle(
        test, (x, y),
        1, (255, 255, 255),
        thickness=1)
    print 'circle made'
    cv2.imwrite('xy.jpg', test)