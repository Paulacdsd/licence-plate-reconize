#from google.cloud import vision
import io
from os import walk
import segmentation as sg
import pytesseract
import cv2

try:
    from PIL import Image
except ImportError:
    import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'



def scan_plate(image):
    custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
    plate_number = (pytesseract.image_to_string(image, config=custom_config))
    return plate_number[:-1]



_, _, filenames = next(walk('./imagens2/'))
for i in range(len(filenames)):
    print(filenames[i])


    crop_path=sg.preprocessing('imagens2/'+ filenames[i])

    if crop_path is not None:
        #detect_text(crop_path)
        plate = cv2.imread(crop_path)
        plate_number = scan_plate(plate)
        print(plate_number)

    else:
        print('Tente outra imagem!')
