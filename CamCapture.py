# -*- coding: utf-8 -*-
"""
Created on Wed May 15 12:28:39 2019

@author: tales
"""


import cv2

    
cap = cv2.VideoCapture(0)

while(True):
    #lê cada quadro do vídeo e carrega na varíavel frame
    _, frame = cap.read()
    
    
    cv2.imshow("frame",frame)
    
    
    if cv2.waitKey(1)&0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    
        
  
        
        
        