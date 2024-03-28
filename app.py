from flask import Flask, render_template, request
import qrcode
import base64
from io import BytesIO
import re

app = Flask(__name__)


def validateFirstName(name):
    if(not bool(name)):
       return 'Please Enter A First Name.'
    if(len(name) >= 64):
        return 'First Name Is Too Long.'
    if(bool(re.match(r'^[a-zA-Z-]+$', name.strip())) is False):
        return 'Invalid First Name.'


def validateLastName(name):
    if(not bool(name)):
       return 'Please Enter A Last Name.'
    if(len(name) >= 64):
        return 'Last Name Is Too Long.'
    if(bool(re.match(r'^[a-zA-Z-]+$', name.strip())) is False):
        return 'Invalid Last Name.'


def validateRank(rank):
    if(not bool(rank)):
        return 'Please Choose A Rank From The Dropdown Menu.'


def validateUnit(unit):
    if(not bool(unit)):
        return 'Please Enter A Unit.'
    if(len(unit) <= 2 or len(unit) >= 5):
        return 'Invalid Unit.'


def validatePhoneNumber(phoneNumber):
    if(not bool(phoneNumber)):
        return 'Please Enter A Phone Number.'
    if(len(phoneNumber) != 10):
        return 'Invalid Length On The Phone Number.'

def validateFitness(fitness):
    if(fitness == 'none'):
        return 'Please Choose An Answer To The Fitness Question.'
    
def validateProfile(profile):
    if(profile == 'none'):
        return 'Please Choose An Answer To The Profile Question.'


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
        errorMessages = []
        errorMessages.append(validateFirstName(firstName))
        errorMessages.append(validateLastName(lastName))
        errorMessages.append(validateRank(rank))
        errorMessages.append(validateUnit(unit))
        errorMessages.append(validatePhoneNumber(phoneNumber))
        errorMessages.append(validateFitness(fitness))
        errorMessages.append(validateProfile(profile))
        for message in errorMessages:
            print(message)
            if(bool(message)):
                return render_template('index.html', error=message)


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
