import os
import sys
import cv2
import qrcode
from PIL import Image
from generateQR import generateQR,readQR

qrfilename = os.path.join(sys.path[0],"QR.png")
inputfilename =  os.path.join(sys.path[0],"input.png")
outputfilename =  os.path.join(sys.path[0],"output.png")

def encryptImage():
    data = input('Enter data to be encoded: ')
    generateQR(data,qrfilename)

    print("Hiding a QR code within input.png")

    im = Image.open(inputfilename)
    qr = Image.open(qrfilename)
    qr_pixel_map = qr.load()
    im_pixel_map = im.load()

    if qr.size > im.size:
        print("input image smaller than qr code, try with a larger image")
        return

    for x in range(qr.size[0]):
        for y in range(qr.size[1]):
            pixel = im_pixel_map[x,y]
            change = False
            
            if qr_pixel_map[x,y]:
                if sum(pixel)%2:
                    continue
                else:
                    change = True
            else:
                if sum(pixel)%2:
                    change = True
                else:
                    continue

            if change:
                im_pixel_map[x,y] = (pixel[0]-1,pixel[1],pixel[2])

    im.save(outputfilename)

encryptImage()

outputfile = cv2.imread(outputfilename)
cv2.imshow("encrypted-img",outputfile)
cv2.waitKey(0)
cv2.destroyAllWindows()


                    
    
    
    



