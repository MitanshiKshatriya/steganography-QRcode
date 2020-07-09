import os
import sys
import cv2
import qrcode
import numpy as np
import random
from generateQR import generateQR,readQR

qrfilename = os.path.join(sys.path[0],"QR.png")
inputfilename =  os.path.join(sys.path[0],"input.png")
outputfilename =  os.path.join(sys.path[0],"output.png")
decodedqrfilename = os.path.join(sys.path[0],"decodedQR.png")
expfilename = os.path.join(sys.path[0],"exp.png")

def cropDecodedQR(decodedqrfilename):
    img = cv2.imread(decodedqrfilename)
    

    img1 = np.zeros((600, 600, 3), np.uint8)

    for i in range(600):
        for j in range(600):

            img1[i][j]=img[i][j]

    
    cv2.imwrite(expfilename, img1)
    
cropDecodedQR(decodedqrfilename)
