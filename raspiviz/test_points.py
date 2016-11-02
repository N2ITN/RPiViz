import cv2

def circle(x,y):
    test = cv2.imread('snapcrop.jpg')
    cv2.circle(
        test, (0, 0),
        1, (0, 255, 255),
        thickness=3)
    
    cv2.circle(
        test, (y, x),
        1, (255, 255, 0),
        thickness=3)
    print 'circle made'
    cv2.imwrite('xy.jpg', test)