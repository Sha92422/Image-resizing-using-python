import cv2
src = "python.jpg"
dest = "Resized photo.jpg"
s = cv2.imread(src,cv2.IMREAD_UNCHANGED)
scale = 50
resized_width = int(s.shape[1]*scale/100)
resized_height = int(s.shape[0]*scale/100)
result = cv2.resize(s,(resized_width,resized_height))
cv2.imwrite(dest,result)
cv2.waitKey(0)