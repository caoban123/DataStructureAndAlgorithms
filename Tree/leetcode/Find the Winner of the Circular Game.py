# n = 6
# k = 5
# lst = [i for i in range(1,n + 1)]
# i = k - 1
# while len(lst) > 1:
#     lst.pop(i)
#     if len(lst) > 0:
#         i = (i + k - 1) % len(lst)
        
# print(lst)
import cv2 as cv
import numpy as np
def draw_circle(event,x,y,flag,param):
  if event == cv.EVENT_LBUTTONDOWN:
    cv.circle(img, (x,y),10, (0,255,0), -1)
cv.namedWindow("banmatlon")
cv.setMouseCallback("banmatlon",draw_circle)
img = np.zeros((512,512,3),np.uint16)
while True:
  cv.imshow("banmatlon",img)
  if cv.getWindowProperty('banmatlon', cv.WND_PROP_VISIBLE) < 1:
    break
  if cv.waitKey(1) == 27:
    break
  
cv.destroyAllWindows()

    
