import cv2 as cv 
import mediapipe as mp #to detect the hand 
import pyautogui


hand_detector=mp.solutions.hands.Hands()
cap=cv.VideoCapture(0) 
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height=pyautogui.size()
index_y=0 #declaring here because to use it in thumb operation

while True:
    _,frame=cap.read()  
    frame=cv.flip(frame,1) 
    frame_height,frame_width,_=frame.shape
    rgb_frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)  
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)  
            landmarks=hand.landmark 
            for id,landmark in enumerate(landmarks):
                 
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                print(x,y)#gives the index finger coordinates 
                if id==8:
                    cv.circle(img=frame,center=(x,y),radius=10,color=(0,0,255)) 
                    index_x=(screen_width/frame_width)*x
                    index_y=(screen_height/frame_height)*y
                    
                    pyautogui.moveTo(index_x,index_y)
                if id==4:
                    cv.circle(img=frame,center=(x,y),radius=10,color=(255,255,255)) 
                    thumb_x=(screen_width/frame_width)*x
                    thumb_y=(screen_height/frame_height)*y 
                    if abs(index_y-thumb_y)<30:
                        pyautogui.click()
                        pyautogui.sleep(1)
    


    cv.imshow("virtual mouse",frame) 
    if cv.waitKey(1) & 0XFF == ord('q'):
        break 
    #cv.waitKey(1)