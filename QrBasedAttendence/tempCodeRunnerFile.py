import cv2
import numpy
import pyzbar.pyzbar as pyzbar
import sys
import time
import base64
import generate

#Start webcam

Cap = cv2.VideoCapture(0)

names = []

#function for attendence file

fob=open('encoded.txt','a+')
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z=''.join(str(z))
        fob.write(z+'\n')
        return names

print('Reading code............')

#function data present or not
def checkData(data):
    data =str(data)
    if data in names:
        print('Already Present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'Present done')
        enterData(data)

while True:
    _,frame = Cap.read()
    decodeObject = pyzbar.decode(frame)
    for obj in decodeObject:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow('Frame',frame)

    #Close

    if cv2.waitKey(1)& 0xff==ord('s'):
        cv2.destroyAllWindows()
        break

fob.close()
