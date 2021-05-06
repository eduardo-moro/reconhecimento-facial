#!/usr/bin/env python3
import numpy as np
import cv2
import sys
import base64
import face_recognition
import base64

def compareFaces(path1, path2):

    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)

    encodings = face_recognition.face_encodings(img1)

    if len(encodings) <= 0:
        return(-1)

    known_face_encoding = encodings[0]

    unknown_face_encodings = face_recognition.face_encodings(img2)

    face_found = False
    is_equal = False
    score = 0

    if len(unknown_face_encodings) > 0:
        face_found = True
        # Compara as faces detectadas
        match_results = face_recognition.compare_faces([known_face_encoding], unknown_face_encodings[0])
        distance = face_recognition.face_distance([known_face_encoding], unknown_face_encodings[0])

        distance = 1 - distance
        if distance >= 0.9:
            score = distance
        elif distance >= 0.8:
            score = distance + 0.1
        else:
            score = distance + 0.2
    else:
        return(-1)

    return(', '.join('{:0.2f}'.format(i) for i in score))


def saveFile(name, img64):
    img64 = img64[img64.find(',') +1:]
    with open(name, 'wb+') as image:
        converted_string = base64.decodebytes(img64.encode("utf-8"))
        image.write(converted_string)

    return name
