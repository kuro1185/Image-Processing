import cv2
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

if not cap.isOpened():
    print("Cannot open camara")
    exit()
    
while True:
    ret,frame = cap.read()
    
    if not ret:
        print("Can't receive frame(stream end?).EXiting...")
        break
    cv2.imshow("frame",frame)
    cv2.imwrite("photo.jpg",frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()