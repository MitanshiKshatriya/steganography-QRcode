import os
import sys
import cv2
import qrcode
import numpy as np
import random
from PIL import Image
from generateQR import generateQR,readQR
from cropImage import cropDecodedQR

qrfilename = os.path.join(sys.path[0],"QR.png")
inputfilename =  os.path.join(sys.path[0],"input.png")
outputfilename =  os.path.join(sys.path[0],"output.png")
decodedqrfilename = os.path.join(sys.path[0],"decodedQR.png")
expfilename = os.path.join(sys.path[0],"exp.png")



    
def decryptImage():
    im = Image.open(outputfilename)
    im_pixel_map = im.load()

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if sum(im_pixel_map[x,y])%2:
                im_pixel_map[x,y] = (255,255,255)
            else:
                im_pixel_map[x,y] = (0,0,0)

    im.save(decodedqrfilename)
    #readQR(decodedQRfilename)

decryptImage()

cropDecodedQR(decodedqrfilename)
readQR(expfilename)
decodedqr = cv2.imread(decodedqrfilename)
cv2.imshow('decoded QR',decodedqr)
cv2.waitKey(0)
cv2.destroyAllWindows()
    


    




    
    
    
