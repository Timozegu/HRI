from pyzbar import pyzbar
import cv2

def barcode_detection(image):
    # decodes different types of barcode 
    decoded_barcode = pyzbar.decode(image, symbols=[pyzbar.ZBarSymbol.EAN13])
    print(decoded_barcode)
    if decoded_barcode == []:
        decoded_barcode = pyzbar.decode(image, symbols=[pyzbar.ZBarSymbol.EAN8])
        print(decoded_barcode)
    value = 0
    for barcode in decoded_barcode:
        # print barcode type & data
        print("Type:", barcode.type)
        print("Data:", barcode.data)
        value = barcode.data.decode()
        print(value)
    return value

def read_barcode(path):
    image = cv2.imread(path)
    value = barcode_detection(image)
    # if you want to be sure about the pictures you can display it with :
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)
    return value





