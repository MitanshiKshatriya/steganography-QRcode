import os
import sys
import cv2
import qrcode

#generate a qr code

def generateQR(data,filename):
    img = qrcode.make(data)
    img.save(filename)

def readQR(filename):
    # read the QRCODE image
    img = cv2.imread(filename)

    #initializing cv2 qrcode dectector
    detector = cv2.QRCodeDetector()

    
    data, bbox, straight_qrcode = detector.detectAndDecode(img)

    if bbox is not None:
        print("QRCode data:\n",data)
        # display the image with lines
        # length of bounding box
        n_lines = len(bbox)
        for i in range(n_lines):
            # draw all lines
            point1 = tuple(bbox[i][0])
            point2 = tuple(bbox[(i+1) % n_lines][0])
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

        # display the result
        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("QR code not proper")

filename = os.path.join(sys.path[0], "QR.png")

#generateQR('Back in my body',filename)
#readQR('./exp.png')
