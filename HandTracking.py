# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:09:35 2021

@author: Vamsi
"""

import cv2
import mediapipe as mp
import time 

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



while True:
    success, img = cap.read()
    cv2.imshow('Frame',img)
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
   
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
             mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)
            
    
    if cv2.waitKey(1)==ord('q'):
        break
    
cv2.destroyAllWindows()