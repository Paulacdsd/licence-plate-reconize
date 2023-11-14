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
    caracs = plate_number[:-1]
    caracs = caracs.replace(' ', '')
    caracs = caracs.replace("-", "")
    letras = caracs[:3]
    num = caracs[3:]
    num = num.replace("-", "")
    letras = letras.replace("-", "")
    num = num.replace('O', "0")
    letras = letras.replace('0', "O")
    num = num.replace('I', "1")
    letras = letras.replace('1', "I")
    num = num.replace('G', "6")
    letras = letras.replace('6', "G")
    num = num.replace('B', "8")
    letras = letras.replace('8', "B")
    num = num.replace('T', "1")
    letras = letras.replace('1', "T")
    num = num.replace('Z', "2")
    letras = letras.replace('2', "Z")
    num = num.replace('H', "11")
    letras = letras.replace('11', "H")
    num = num.replace('S', "3")
    letras = letras.replace('5', "S")
    placa_escrita = letras + '-' + num
    return placa_escrita



_, _, filenames = next(walk('./imagens/'))
for i in range(len(filenames)):
    print(filenames[i])


    crop_path=sg.preprocessing('imagens/'+ filenames[i])

    if crop_path is not None:
        #detect_text(crop_path)
        plate = cv2.imread(crop_path)
        plate_number = scan_plate(plate)
        print(plate_number)

    else:
        print('Tente outra imagem!')
