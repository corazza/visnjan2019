import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

def onChange(x):
    print(x)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, onChange)
cv2.createTrackbar("LS", "Tracking", 0, 255, onChange)
cv2.createTrackbar("LV", "Tracking", 0, 255, onChange)
cv2.createTrackbar("UH", "Tracking", 255, 255, onChange)
cv2.createTrackbar("US", "Tracking", 255, 255, onChange)
cv2.createTrackbar("UV", "Tracking", 255, 255, onChange)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h  = cv2.getTrackbarPos("LH", "Tracking")
    l_s  = cv2.getTrackbarPos("LS", "Tracking")
    l_v  = cv2.getTrackbarPos("LV", "Tracking")
    u_h  = cv2.getTrackbarPos("UH", "Tracking")
    u_s  = cv2.getTrackbarPos("US", "Tracking")
    u_v  = cv2.getTrackbarPos("UV", "Tracking")

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Input', res)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
