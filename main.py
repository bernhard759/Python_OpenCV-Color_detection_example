import cv2 as cv
import numpy as np
import imutils


# Colors
color = (255,255,255)
colors = {'blue': [np.array([95, 255, 85]), np.array([120, 255, 255])],
          'red': [np.array([161, 165, 127]), np.array([178, 255, 255])],
          'yellow': [np.array([16, 0, 99]), np.array([39, 255, 255])],
          'green': [np.array([33, 19, 105]), np.array([77, 255, 255])]}


def find_color(frame, points):
    """find a colored object."""
    print("find color")
    mask = cv.inRange(frame, points[0], points[1])#create mask with boundaries 
    cnts = cv.findContours(mask, cv.RETR_TREE, 
                           cv.CHAIN_APPROX_SIMPLE) # find contours from mask
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        area = cv.contourArea(c) # find how big countour is
        if area > 5000:       # only if countour is big enough, then
            M = cv.moments(c)
            cx = int(M['m10'] / M['m00']) # calculate X position
            cy = int(M['m01'] / M['m00']) # calculate Y position
            return c, cx, cy

cap = cv.VideoCapture(0)

# Loop
while cap.isOpened():
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # HSV color
    for name, clr in colors.items(): # for each color in colors
        if find_color(hsv, clr):  # call find_color function above
            c, cx, cy = find_color(hsv, clr)
            cv.drawContours(frame, [c], -1, color, 3) # draw contours
            cv.circle(frame, (cx, cy), 7, color, -1)  # draw circle
            cv.putText(frame, name, (cx,cy), 
                        cv.FONT_HERSHEY_SIMPLEX, 1, color, 1) # put text
    cv.imshow("Frame: ", frame) # show image
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows() # close all windows opened by opencv


