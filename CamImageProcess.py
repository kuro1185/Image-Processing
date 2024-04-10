import cv2
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

def Process(src):
    src = cv2.imread(src)
    dstx = cv2.Sobel(src,cv2.CV_32F,1,0)
    dsty = cv2.Sobel(src,cv2.CV_32F,0,1)
    dstx = cv2.convertScaleAbs(dstx)
    dsty = cv2.convertScaleAbs(dsty)
    dst = cv2.addWeighted(dstx,0.5,dsty,0.5,0)
    cv2.imshow("Image Processing",dst)
    cv2.imwrite("result.jpg",dst)

if not cap.isOpened():
    print("Cannot open camara")
    exit()
    
while True:
    ret,frame = cap.read()
    
    if not ret:
        print("Can't receive frame(stream end?).EXiting...")
        break
    cv2.imshow("Original Image",frame)
    cv2.imwrite("webcam.jpg",frame)
    Process("webcam.jpg")
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()