from flask import Flask, render_template, request, redirect, url_for, session
from models import get_devices, update_device_price, add_device_submission, create_user, check_user_credentials

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_user_credentials(username, password):
            session['logged_in'] = True
            session['username'] = username  # Store username in session
            return redirect(url_for('manage_devices'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        create_user(username, password)  # Save user to database
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/submit-device', methods=['POST'])
def submit_device():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    brand = request.json.get('brand')
    model = request.json.get('model')
    username = session['username']

    # Save device submission to database
    add_device_submission(username, brand, model)

    return {"message": "Device submitted successfully!"}, 200

@app.route('/manage_devices', methods=['GET'])
def manage_devices():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    devices = get_devices()
    return render_template('manage_devices.html', devices=devices)

if __name__ == '__main__':
    app.run(debug=True)