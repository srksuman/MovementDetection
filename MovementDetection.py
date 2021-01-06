import cv2
import winsound
import time
camera = cv2.VideoCapture(0)
output = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'MJPG'),20,(500,500))
while camera.isOpened():
    text = time.ctime()
    itr, frame1= camera.read()
    itr, frame2= camera.read()
    cv2.putText(frame1,text, (10,15),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,56))
    difference = cv2.absdiff(frame1,frame2)
    grey = cv2.cvtColor(difference,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(grey,(5,5),0)
    _,thresh = cv2.threshold(blur,30,255,cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh,None,iterations= 4)
    controus, _ = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for n in controus:
        if cv2.contourArea(n)<6000:
            continue
        x,y,w,h = cv2.boundingRect(n)
        winsound.Beep(1000,400)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),1,4) 
    if cv2.waitKey(10)== ord('n'):
        break
    
    cv2.imshow('Detection',frame1)
    output.write(frame1)
camera.release()
output.release()
cv2.destroyAllWindows()