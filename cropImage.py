import os
import sys
import cv2
import qrcode
import numpy as np
import random
from PIL import Image
from generateQR import generateQR,readQR

qrfilename = os.path.join(sys.path[0],"QR.png")
inputfilename =  os.path.join(sys.path[0],"input.png")
outputfilename =  os.path.join(sys.path[0],"output.png")
decodedqrfilename = os.path.join(sys.path[0],"decodedQR.png")
expfilename = os.path.join(sys.path[0],"exp.png")

def cropDecodedQR(decodedqrfilename):
    image = cv2.imread(decodedqrfilename)
    y=0
    x=0
    h=600
    w=600
    crop_image = image[x:w, y:h]
    #cv2.imshow("Cropped", crop_image)
    #cv2.waitKey(0)
    cv2.imwrite(expfilename,crop_image)
    
#cropDecodedQR(decodedqrfilename)
