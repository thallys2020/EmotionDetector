# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:57:35 2021

@author: tales
"""


import cv2
import face_recognition
import math
import csv



def dist(x0, y0, x1, y1):
    a = (x1-x0)**2 + (y1-y0)**2
    b = math.sqrt(a)
    return b

def add(a, lista):
    lista.append(a)
    return print("Sucesso")

def calculoAU (frameNeutro, frameApice):
    #guarda os landmarks em um dicionário
    face_landmarks_list_neutro = face_recognition.face_landmarks(frameNeutro)
    
    face_landmarks_list_apice = face_recognition.face_landmarks(frameApice)
    
    #Inner Brow Raiser
    AU1Variation = dist(face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1],
                        face_landmarks_list_apice[0]['left_eye'][3][0], face_landmarks_list_apice[0]['left_eye'][3][1]) - dist(face_landmarks_list_neutro[0]['left_eyebrow'][4][0], face_landmarks_list_neutro[0]['left_eyebrow'][4][1],
                        face_landmarks_list_neutro[0]['left_eye'][3][0], face_landmarks_list_neutro[0]['left_eye'][3][1]) 
    #Inner Brow Raiser
    AU11Variation = dist(face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1],
                         face_landmarks_list_apice[0]['right_eye'][0][0], face_landmarks_list_apice[0]['right_eye'][0][1]) - dist(face_landmarks_list_neutro[0]['right_eyebrow'][0][0], face_landmarks_list_neutro[0]['right_eyebrow'][0][1],
                         face_landmarks_list_neutro[0]['right_eye'][0][0], face_landmarks_list_neutro[0]['right_eye'][0][1])
    #Outer Brow Raiser
    AU21Variation = dist(face_landmarks_list_apice[0]['left_eyebrow'][1][0], face_landmarks_list_apice[0]['left_eyebrow'][1][1],
                         face_landmarks_list_apice[0]['left_eye'][3][0], face_landmarks_list_apice[0]['left_eye'][3][1]) - dist(face_landmarks_list_neutro[0]['left_eyebrow'][1][0], face_landmarks_list_neutro[0]['left_eyebrow'][1][1],
                         face_landmarks_list_neutro[0]['left_eye'][3][0], face_landmarks_list_neutro[0]['left_eye'][3][1])
    
    #Outer Brow Raiser
    AU22Variation = dist(face_landmarks_list_apice[0]['right_eyebrow'][3][0], face_landmarks_list_apice[0]['right_eyebrow'][3][1],
                         face_landmarks_list_apice[0]['right_eye'][0][0], face_landmarks_list_apice[0]['right_eye'][0][1]) - dist(face_landmarks_list_neutro[0]['right_eyebrow'][3][0], face_landmarks_list_neutro[0]['right_eyebrow'][3][1],
                         face_landmarks_list_neutro[0]['right_eye'][0][0], face_landmarks_list_neutro[0]['right_eye'][0][1])
    
    #Brow Lowerer
    AU4Variation = dist(face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1],
                        face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1]) - dist(face_landmarks_list_neutro[0]['left_eyebrow'][4][0], face_landmarks_list_neutro[0]['left_eyebrow'][4][1],
                        face_landmarks_list_neutro[0]['right_eyebrow'][0][0], face_landmarks_list_neutro[0]['right_eyebrow'][0][1])
    
    #Upper Lid Raiser
    AU51Variation = dist(face_landmarks_list_apice[0]['left_eye'][2][0], face_landmarks_list_apice[0]['left_eye'][2][1],
                         face_landmarks_list_apice[0]['left_eye'][4][0], face_landmarks_list_apice[0]['left_eye'][4][1]) - dist(face_landmarks_list_neutro[0]['left_eye'][2][0], face_landmarks_list_neutro[0]['left_eye'][2][1],
                         face_landmarks_list_neutro[0]['left_eye'][4][0], face_landmarks_list_neutro[0]['left_eye'][4][1])
    
    #Upper Lid Raiser
    AU52Variation = dist(face_landmarks_list_apice[0]['right_eye'][1][0], face_landmarks_list_apice[0]['right_eye'][1][1],
                         face_landmarks_list_apice[0]['right_eye'][5][0], face_landmarks_list_apice[0]['left_eye'][5][1]) - dist(face_landmarks_list_neutro[0]['right_eye'][1][0], face_landmarks_list_neutro[0]['right_eye'][1][1],
                         face_landmarks_list_neutro[0]['right_eye'][5][0], face_landmarks_list_neutro[0]['left_eye'][5][1])
    
    #Cheek Raiser
    AU61Variation = AU51Variation
    
    #Cheek Raiser
    AU62Variation = AU52Variation
    
    #Nose Wrinkler
    AU91Variation = dist(face_landmarks_list_apice[0]['left_eyebrow'][4][0], face_landmarks_list_apice[0]['left_eyebrow'][4][1],
                         face_landmarks_list_apice[0]['nose_tip'][0][0], face_landmarks_list_apice[0]['nose_tip'][0][1]) - dist(face_landmarks_list_neutro[0]['left_eyebrow'][4][0], face_landmarks_list_neutro[0]['left_eyebrow'][4][1],
                         face_landmarks_list_neutro[0]['nose_tip'][0][0], face_landmarks_list_neutro[0]['nose_tip'][0][1])
    
    #Nose Wrinkler
    AU92Variation = dist(face_landmarks_list_apice[0]['right_eyebrow'][0][0], face_landmarks_list_apice[0]['right_eyebrow'][0][1],
                         face_landmarks_list_apice[0]['nose_tip'][4][0], face_landmarks_list_apice[0]['nose_tip'][4][1]) - dist(face_landmarks_list_neutro[0]['right_eyebrow'][0][0], face_landmarks_list_neutro[0]['right_eyebrow'][0][1],
                         face_landmarks_list_neutro[0]['nose_tip'][4][0], face_landmarks_list_neutro[0]['nose_tip'][4][1])
    
    
    #Upper Lip Raiser
    AU10Variation = dist(face_landmarks_list_apice[0]['top_lip'][3][0], face_landmarks_list_apice[0]['top_lip'][3][1],
                         face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]) - dist(face_landmarks_list_neutro[0]['top_lip'][3][0], face_landmarks_list_neutro[0]['top_lip'][3][1],
                         face_landmarks_list_neutro[0]['nose_tip'][2][0], face_landmarks_list_neutro[0]['nose_tip'][2][1])
    
    #Lip Corner Puller
    AU12Variation = dist(face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1],
                         face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]) - dist(face_landmarks_list_neutro[0]['top_lip'][0][0], face_landmarks_list_neutro[0]['top_lip'][0][1],
                         face_landmarks_list_neutro[0]['top_lip'][6][0], face_landmarks_list_neutro[0]['top_lip'][6][1])
    
    #Lip Corner Depressor
    AU151Variation = dist(face_landmarks_list_apice[0]['nose_tip'][0][0], face_landmarks_list_apice[0]['nose_tip'][0][1],
                          face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1]) - dist(face_landmarks_list_neutro[0]['nose_tip'][0][0], face_landmarks_list_neutro[0]['nose_tip'][0][1],
                          face_landmarks_list_neutro[0]['top_lip'][0][0], face_landmarks_list_neutro[0]['top_lip'][0][1])
    
    #Lip Corner Depressor
    AU152Variation = dist(face_landmarks_list_apice[0]['nose_tip'][4][0], face_landmarks_list_apice[0]['nose_tip'][4][1],
                          face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]) - dist(face_landmarks_list_neutro[0]['nose_tip'][4][0], face_landmarks_list_neutro[0]['nose_tip'][4][1],
                          face_landmarks_list_neutro[0]['top_lip'][6][0], face_landmarks_list_neutro[0]['top_lip'][6][1])
    
    #Chin Raiser
    AU17Variation = dist(face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1],
                         face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]) - dist(face_landmarks_list_neutro[0]['bottom_lip'][3][0], face_landmarks_list_neutro[0]['bottom_lip'][3][1],
                         face_landmarks_list_neutro[0]['nose_tip'][2][0], face_landmarks_list_neutro[0]['nose_tip'][2][1])
    
    #Lip stretcher
    AU20Variation = dist(face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1],
                         face_landmarks_list_apice[0]['chin'][8][0], face_landmarks_list_apice[0]['chin'][8][1]) - dist(face_landmarks_list_neutro[0]['bottom_lip'][3][0], face_landmarks_list_neutro[0]['bottom_lip'][3][1],
                         face_landmarks_list_neutro[0]['chin'][8][0], face_landmarks_list_neutro[0]['chin'][8][1])
    
    #Lip Tightener
    AU23Variation = dist(face_landmarks_list_apice[0]['top_lip'][0][0], face_landmarks_list_apice[0]['top_lip'][0][1],
                         face_landmarks_list_apice[0]['top_lip'][6][0], face_landmarks_list_apice[0]['top_lip'][6][1]) - dist(face_landmarks_list_neutro[0]['top_lip'][0][0], face_landmarks_list_neutro[0]['top_lip'][0][1],
                         face_landmarks_list_neutro[0]['top_lip'][6][0], face_landmarks_list_neutro[0]['top_lip'][6][1])
    
    #Lip Pressor
    AU24Variation = dist(face_landmarks_list_apice[0]['top_lip'][3][0], face_landmarks_list_apice[0]['top_lip'][3][1],
                         face_landmarks_list_apice[0]['bottom_lip'][3][0], face_landmarks_list_apice[0]['bottom_lip'][3][1]) - dist(face_landmarks_list_neutro[0]['top_lip'][3][0], face_landmarks_list_neutro[0]['top_lip'][3][1],
                         face_landmarks_list_neutro[0]['bottom_lip'][3][0], face_landmarks_list_neutro[0]['bottom_lip'][3][1])
    
    #Lips Part
    AU25Variation = dist(face_landmarks_list_apice[0]['top_lip'][9][0], face_landmarks_list_apice[0]['top_lip'][9][1],
                         face_landmarks_list_apice[0]['bottom_lip'][9][0], face_landmarks_list_apice[0]['bottom_lip'][9][1]) - dist(face_landmarks_list_neutro[0]['top_lip'][9][0], face_landmarks_list_neutro[0]['top_lip'][9][1],
                         face_landmarks_list_neutro[0]['bottom_lip'][9][0], face_landmarks_list_neutro[0]['bottom_lip'][9][1])
    
    #Jaw Drop
    AU26Variation = dist(face_landmarks_list_apice[0]['chin'][8][0], face_landmarks_list_apice[0]['chin'][8][1],
                         face_landmarks_list_apice[0]['nose_tip'][2][0], face_landmarks_list_apice[0]['nose_tip'][2][1]) - dist(face_landmarks_list_neutro[0]['chin'][8][0], face_landmarks_list_neutro[0]['chin'][8][1],
                         face_landmarks_list_neutro[0]['nose_tip'][2][0], face_landmarks_list_neutro[0]['nose_tip'][2][1])
    
    #Mouth Stretch
    AU27Variation = AU26Variation 
    
    
    return AU1Variation, AU11Variation, AU21Variation, AU22Variation, AU4Variation, AU51Variation, AU52Variation, AU61Variation, AU62Variation, AU91Variation, AU92Variation, AU10Variation, AU12Variation, AU151Variation, AU152Variation, AU17Variation, AU20Variation, AU23Variation, AU24Variation, AU25Variation, AU26Variation, AU27Variation                                 
    



s = 0

while(True):
    
    nome = input(print("Digite o nome do arquivo csv:"))
    
    f = open(nome + '.csv', 'r')
    
    try:
        reader = csv.reader(f, delimiter = ";")
        for line in reader:
            #line[0] -> ID, line[1] -> gender, line[2] -> folderName, line[3] -> emotionNumber
            #line[4l-> emotionName, line[5] -> AUs detectadas de acordo com o banco, 
            #line[6] ->file name neutra, line[7] ->file name ápice, line[8]-> não classificado
            
            print(line)
            
            frameNeutro = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" + str(line[0])+ "/00"+ str(line[2])+ "/"+ str(line[6]) + ".png")
            
            frameApice = cv2.imread("/Users/tales/Desktop/Projeto_PIBIC/extended-cohn-kanade-images/cohn-kanade-images" + "/" + str(line[0])+ "/00"+ str(line[2])+ "/"+ str(line[7]) + ".png")
            
            #emotion number : 1->anger // 2-> contempt // 3-> disgust // 4-> fear // 5-> happiness //
            #6-> sadness // 7-> surprise
            if line[3] == '1' and line[1] == 'M' and s > 1:
                anger = calculoAU(frameNeutro, frameApice)
                
                l = open('angerM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((anger))
                finally:
                   l.close()
                   
            elif line[3] == '1' and line[1] == 'F' and s > 1:
                anger = calculoAU(frameNeutro, frameApice)
                
                l = open('angerF.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((anger))
                finally:
                   l.close()
                   
            elif line[3] == '2' and line[1] == 'M' and s > 1:
                emotion = calculoAU(frameNeutro, frameApice)
                l = open('contemptM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((emotion))
                finally:
                   l.close()
                   
            elif line[3] == '2' and line[1] == 'F' and s > 1:
                emotion = calculoAU(frameNeutro, frameApice)
                l = open('contemptF.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((emotion))
                finally:
                   l.close()
                
            elif line[3] == '3' and line[1] == 'M' and s > 1:
                disgust = calculoAU(frameNeutro, frameApice)
                l = open('disgustM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((disgust))
                finally:
                   l.close()
                   
            elif line[3] == '3' and line[1] == 'F' and s > 1:
                disgust = calculoAU(frameNeutro, frameApice)
                l = open('disgustF.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((disgust))
                finally:
                   l.close()
                
            elif line[3] == '4' and line[1] == 'M' and s > 1:
                fear = calculoAU(frameNeutro, frameApice)
                l = open('fearM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((fear))
                finally:
                   l.close()
            
            elif line[3] == '4' and line[1] == 'F' and s > 1:
                fear = calculoAU(frameNeutro, frameApice)
                l = open('fearF.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((fear))
                finally:
                   l.close()
                
            elif line[3] == '5' and line[1] == 'M' and s > 1:
                happiness = calculoAU(frameNeutro, frameApice)
                l = open('happinessM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((happiness))
                finally:
                   l.close()
                   
            elif line[3] == '5' and line[1] == 'F' and s > 1:
                happiness = calculoAU(frameNeutro, frameApice)
                l = open('happinessF.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((happiness))
                finally:
                   l.close()
                
            elif line[3] == '6' and line[1] == 'M' and s > 1:
                sadness = calculoAU(frameNeutro, frameApice)
                l = open('sadnessM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((sadness))
                finally:
                   l.close()
                   
            elif line[3] == '6' and line[1] == 'F' and s > 1:
                sadness = calculoAU(frameNeutro, frameApice)
                l = open('sadnessF.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((sadness))
                finally:
                   l.close()
                
            elif line[3] == '7' and line[1] == 'M' and s > 1:
                surprise = calculoAU(frameNeutro, frameApice)
                l = open('surpriseM.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((surprise))
                finally:
                   l.close()
                   
            elif line[3] == '7' and line[1] == 'F' and s > 1:
                surprise = calculoAU(frameNeutro, frameApice)
                l = open('surpriseF.csv', 'a', newline = '')
                try:
                    writer = csv.writer(l, delimiter = ";")
                    writer.writerow((surprise))
                finally:
                   l.close()
                   
            s = s + 1
            
            print("Sucesso")
            
    finally:
        f.close()
    
    



    
     

