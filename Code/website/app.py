from flask import Flask, render_template, request
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        entry = ""
        entry += request.form['firstName'] + ','
        entry += request.form['lastName'] + ','
        entry += request.form['phoneNumber'] + ','
        qr_code_data = generate_qr_code(entry)  # Generate QR code with the submitted entry
        return render_template('submitted.html', entry=entry, qr_code_data=qr_code_data)

def generate_qr_code(data):
    # Generate QR code (using qrcode library)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    # Create a BytesIO object to hold the QR code image
    qr_img = BytesIO()
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_img, format='PNG')
    # Encode the image as base64 string
    qr_img_base64 = base64.b64encode(qr_img.getvalue()).decode()
    return qr_img_base64

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
