from flask import Flask, request, jsonify
import pytesseract
import io
from PIL import Image

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr_service():
    if 'image' not in request.files:
        return jsontify({rerror: "No image uploaded"}), 400)

    file = request.files['image']
    image = Image.open(io.BytesIO(file.read()))
    
    # Perform OCR
    text = pytesseract.image_to_string(file)
    
    return jsontify({text: text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)