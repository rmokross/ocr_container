from flask import Flask, jsonify, request
from tesseract_ocr import tessData
import base64

app = Flask(__name__)
app.secret_key = b'\n\xec_5#y2L"F4Q8z'

@app.route('/img_to_boxes', methods=['POST','GET'])
def img_txt():
    img = request.form.get('img')
    img_enc = img.encode('utf-8')
    img_dec_b64 = base64.b64decode(img_enc) #generating bytes from image for preprocessing

    #start ocr engine
    lang = 'deu'
    box_data = tessData(img_dec_b64, lang=lang)    

    return jsonify(f"{box_data}")
    """
    input: POST requerst with 'img' : '**img as utf-8 string**'
    output: response with string
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
