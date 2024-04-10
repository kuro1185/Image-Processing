import cv2

src = cv2.imread("photo.jpg")
dstx = cv2.Sobel(src,cv2.CV_32F,1,0)
dsty = cv2.Sobel(src,cv2.CV_32F,0,1)
dstx = cv2.convertScaleAbs(dstx)
dsty = cv2.convertScaleAbs(dsty)
dst = cv2.addWeighted(dstx,0.5,dsty,0.5,0)
cv2.imshow("Src",src)
cv2.imshow("Dstx",dstx)
cv2.imshow("Dsty",dsty)
cv2.imshow("Dst",dst)

cv2.imwrite("result.jpg",dst)
    
cv2.waitKey(0)
cv2.destroyAllWindows()