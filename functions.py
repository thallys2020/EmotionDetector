# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 15:49:30 2021

@author: tales
"""

import math 
import face_recognition


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
    
