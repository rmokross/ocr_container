import pytesseract as tess
import preprocessing as prep



def tessData(img_bytes, lang):
    #tess.pytesseract.tesseract_cmd = "D:\\programme\\Tesseract-OCR\\tesseract.exe"
    

    img = prep.imgBuilder(img_bytes)
    binar_img = prep.binarImage(img)
    
    prep_img = prep.rmvNoise(binar_img) #remove noise

    ocr_data = tess.image_to_boxes(prep_img, lang=lang)
    return(ocr_data)