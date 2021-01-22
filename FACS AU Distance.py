# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:57:35 2021

@author: tales
"""

import numpy as np
import cv2
from PIL import Image, ImageDraw
import face_recognition
import math

#declara a lista que armazenara o calculo das distancias entre os pontos
lista1 = []
lista2 = []

#calculo da distância entre dois pontos 
def dist(x0, y0, x1, y1):
    a = (x1-x0)**2 + (y1-y0)**2
    b = math.sqrt(a)
    return b

#função que armazena os resultados na lista
def add(a, lista):
    lista.append(a)
    return print("Sucesso")

def calculoAU (frame, lista):
    #guarda os landmarks em um dicionário
    face_landmarks_list = face_recognition.face_landmarks(frame)
    #Inner Brow Raiser
    AU1 = dist(face_landmarks_list[0]['left_eyebrow'][4][0], face_landmarks_list[0]['left_eyebrow'][4][1],
                face_landmarks_list[0]['left_eye'][3][0], face_landmarks_list[0]['left_eye'][3][1])
    add(AU1, lista)
    #Inner Brow Raiser
    AU11 = dist(face_landmarks_list[0]['right_eyebrow'][0][0], face_landmarks_list[0]['right_eyebrow'][0][1],
                face_landmarks_list[0]['right_eye'][0][0], face_landmarks_list[0]['right_eye'][0][1])
    add(AU11, lista)
    #Outer Brow Raiser
    AU21 = dist(face_landmarks_list[0]['left_eyebrow'][1][0], face_landmarks_list[0]['left_eyebrow'][1][1],
                face_landmarks_list[0]['left_eye'][3][0], face_landmarks_list[0]['left_eye'][3][1])
    add(AU21, lista)
    #Outer Brow Raiser
    AU22 = dist(face_landmarks_list[0]['right_eyebrow'][3][0], face_landmarks_list[0]['right_eyebrow'][3][1],
                face_landmarks_list[0]['right_eye'][0][0], face_landmarks_list[0]['right_eye'][0][1])
    add(AU22, lista)
    #Brow Lowerer
    AU4 = dist(face_landmarks_list[0]['left_eyebrow'][4][0], face_landmarks_list[0]['left_eyebrow'][4][1],
               face_landmarks_list[0]['right_eyebrow'][0][0], face_landmarks_list[0]['right_eyebrow'][0][1])
    add(AU4, lista)
    #Upper Lid Raiser
    AU51 = dist(face_landmarks_list[0]['left_eye'][2][0], face_landmarks_list[0]['left_eye'][2][1],
                face_landmarks_list[0]['left_eye'][4][0], face_landmarks_list[0]['left_eye'][4][1])
    add(AU51, lista)
    #Upper Lid Raiser
    AU52 = dist(face_landmarks_list[0]['right_eye'][1][0], face_landmarks_list[0]['right_eye'][1][1],
                face_landmarks_list[0]['right_eye'][5][0], face_landmarks_list[0]['left_eye'][5][1])
    add(AU52, lista)
    #Cheek Raiser
    AU61 = AU51
    add(AU61, lista)
    #Cheek Raiser
    AU62 = AU52
    add(AU62, lista)
    #Nose Wrinkler
    AU91 = dist(face_landmarks_list[0]['left_eyebrow'][4][0], face_landmarks_list[0]['left_eyebrow'][4][1],
                face_landmarks_list[0]['nose_tip'][0][0], face_landmarks_list[0]['nose_tip'][0][1])
    add(AU91, lista)
    #Nose Wrinkler
    AU92 = dist(face_landmarks_list[0]['right_eyebrow'][0][0], face_landmarks_list[0]['right_eyebrow'][0][1],
                face_landmarks_list[0]['nose_tip'][4][0], face_landmarks_list[0]['nose_tip'][4][1])
    add(AU92, lista)
    #Upper Lip Raiser
    AU10 = dist(face_landmarks_list[0]['top_lip'][3][0], face_landmarks_list[0]['top_lip'][3][1],
                face_landmarks_list[0]['nose_tip'][2][0], face_landmarks_list[0]['nose_tip'][2][1])
    add(AU10, lista)
    #Lip Corner Puller
    AU12 = dist(face_landmarks_list[0]['top_lip'][0][0], face_landmarks_list[0]['top_lip'][0][1],
                face_landmarks_list[0]['top_lip'][6][0], face_landmarks_list[0]['top_lip'][6][1])
    add(AU12, lista)
    #Lip Corner Depressor
    AU151 = dist(face_landmarks_list[0]['nose_tip'][0][0], face_landmarks_list[0]['nose_tip'][0][1],
                 face_landmarks_list[0]['top_lip'][0][0], face_landmarks_list[0]['top_lip'][0][1])
    add(AU151, lista)
    #Lip Corner Depressor
    AU152 = dist(face_landmarks_list[0]['nose_tip'][4][0], face_landmarks_list[0]['nose_tip'][4][1],
                 face_landmarks_list[0]['top_lip'][6][0], face_landmarks_list[0]['top_lip'][6][1])
    add(AU152, lista)
    #Chin Raiser
    AU17 = dist(face_landmarks_list[0]['bottom_lip'][3][0], face_landmarks_list[0]['bottom_lip'][3][1],
                face_landmarks_list[0]['nose_tip'][2][0], face_landmarks_list[0]['nose_tip'][2][1])
    add(AU17, lista)
    #Lip stretcher
    AU20 = dist(face_landmarks_list[0]['bottom_lip'][3][0], face_landmarks_list[0]['bottom_lip'][3][1],
                face_landmarks_list[0]['chin'][8][0], face_landmarks_list[0]['chin'][8][1])
    add(AU20, lista)
    #Lip Tightener
    AU23 = dist(face_landmarks_list[0]['top_lip'][0][0], face_landmarks_list[0]['top_lip'][0][1],
                face_landmarks_list[0]['top_lip'][6][0], face_landmarks_list[0]['top_lip'][6][1])
    add(AU23, lista)
    #Lip Pressor
    AU24 = dist(face_landmarks_list[0]['top_lip'][3][0], face_landmarks_list[0]['top_lip'][3][1],
                face_landmarks_list[0]['bottom_lip'][3][0], face_landmarks_list[0]['bottom_lip'][3][1])
    add(AU24, lista)
    #Lips Part
    AU25 = dist(face_landmarks_list[0]['top_lip'][9][0], face_landmarks_list[0]['top_lip'][9][1],
                face_landmarks_list[0]['bottom_lip'][9][0], face_landmarks_list[0]['bottom_lip'][9][1])
    add(AU25, lista)
    #Jaw Drop
    AU26 = dist(face_landmarks_list[0]['chin'][8][0], face_landmarks_list[0]['chin'][8][1],
                face_landmarks_list[0]['nose_tip'][2][0], face_landmarks_list[0]['nose_tip'][2][1])
    add(AU26, lista)
    #Mouth Stretch
    AU27 = AU26 
    add(AU27, lista)
    

nome1 = input("Nome do arquivo Neutro:")

nome2 = input("Nome do arquivo Ápice:")
#recebe o arquivo da base de dados CK Neutra
frame1 = cv2.imread(nome1+".png")

#recebe o arquivo da base de dados CK Ápice
frame2 = cv2.imread(nome2+".png")

calculoAU(frame1, lista1)

calculoAU(frame2, lista2)

f = open("demofile.txt", "a")

f.write("AUs_Neutra "+"AUs_Ápice "+"Variação"+"\n")

for i in range(0, len(lista1)):
    f.write("%.2f    | %.2f    | %.2f \n" %(lista1[i], lista2[i], lista2[i]-lista1[i]))

f.close()
     
cv2.imshow("frame",frame1)

cv2.imshow("frame2",frame2)


cv2.waitKey(0)    
cv2.destroyAllWindows()