from flask import Flask, render_template, request
import qrcode
import base64
from io import BytesIO
import re

app = Flask(__name__)


def validateName(name):
    if(len(name) >= 64):
        return False
    return bool(re.match(r'^[a-zA-Z-]+$', name.strip()))

def validateRank(rank):
    if (rank != ''):
        return True
    return False

def validateUnit(unit):
    if(len(unit) >= 2 and len(unit) <= 5):
        return True
    return False

def validatePhoneNumber(phoneNumber):
    if(len(phoneNumber) != 10):
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':


        firstName = request.form['firstName'].strip().lower()
        lastName = request.form['lastName'].strip().lower()
        rank = request.form['rank'].strip().lower()
        unit = re.sub('[^0-9]', '', request.form['unit']).strip()
        phoneNumber = re.sub('[^0-9]', '', request.form['phoneNumber']).strip()
        fitness = request.form['fitness']
        profile = request.form['profile']


        #following if statements check to see if the user submitted valid inputs
        #If one of them is wrong, update the index.html page with appropriate error message

        if(validateName(firstName) is False):
            if(len(firstName) == 0):
                return render_template('index.html', error='Please Enter A First Name.')
            return render_template('index.html', error='Invalid First Name.')
        
        if(validateName(lastName) is False):
            if(len(lastName) == 0):
                return render_template('index.html', error='Please Enter A Last Name.')
            return render_template('index.html', error='Invalid Last Name.')
        
        if(validateRank(rank) is False):
            return render_template('index.html', error='Please Choose A Rank From The Dropdown Menu.')
        
        if(validateUnit(unit) is False):
            if(unit == ''):
                return render_template('index.html', error='Please Enter A Unit.')    
            return render_template('index.html', error='Invalid Unit.')
        
        if(validatePhoneNumber(phoneNumber) is False):
            if(phoneNumber == ''):
                return render_template('index.html', error='Please Enter A Phone Number.')
            return render_template('index.html', error='Invalid Length On The Phone Number.')

        if(fitness == 'none'):
            return render_template('index.html', error='Please Select Fitness Status.')

        if(profile == 'none'):
            return render_template('index.html', error='Please Select Profile Status.')

        #stores value of all entries in a single variable
        entry = f"{firstName},{lastName},{rank},{unit},{phoneNumber},{fitness},{profile}"

        qr_code_data = generate_qr_code(entry)  # Generate QR code with values user enters
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
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(qr_img)
    # Encode the image as base64 string
    qr_img_base64 = base64.b64encode(qr_img.getvalue()).decode()
    return qr_img_base64

if __name__ == '__main__':
    app.run()
