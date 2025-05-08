from flask import Flask, request, jsonify
from twilio.rest import Client
import random
import threading
import time
import logging
import os

app = Flask(__name__)
otp_storage = {}
lock = threading.Lock()

# Twilio config
TWILIO_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBERS = [
    '+12345678901',  # Replace with your Twilio numbers
    '+12345678902',
    '+12345678903',
    '+12345678904',
    '+12345678905'
]

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Load messages from text file and shuffle
with open('messages.txt', 'r') as f:
    messages_list = [line.strip() for line in f if line.strip()]
random.shuffle(messages_list)

# Logging
logging.basicConfig(filename='otp_server.log', level=logging.INFO)

# OTP generator
def generate_otp():
    return str(random.randint(100000, 999999))

# OTP cleanup (optional expiry)
def expire_otp(phone, delay=300):
    time.sleep(delay)
    with lock:
        otp_storage.pop(phone, None)

# Send SMS OTP
def send_otp(phone):
    otp = generate_otp()
    with lock:
        otp_storage[phone] = otp
    
    # Choose random message and insert OTP
    message_template = random.choice(messages_list)
    message = message_template.replace('{otp}', otp)
    
    # Choose random Twilio number
    from_number = random.choice(TWILIO_PHONE_NUMBERS)
    
    client.messages.create(to=phone, from_=from_number, body=message)
    logging.info(f"OTP sent to {phone} from {from_number}")
    threading.Thread(target=expire_otp, args=(phone,)).start()


@app.route('/send-otp', methods=['POST'])
def send_otp_route():
    data = request.json
    phone = data.get('phone')
    if not phone:
        return jsonify({"error": "Phone number is required"}), 400

    # Basic rate-limiting (1 OTP per minute)
    if phone in otp_storage:
        return jsonify({"message": "OTP already sent. Please wait."}), 429

    try:
        send_otp(phone)
        return jsonify({"message": "OTP sent successfully"}), 200
    except Exception as e:
        logging.error(f"Error sending OTP to {phone}: {e}")
        return jsonify({"error": "Failed to send OTP"}), 500


@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json
    phone = data.get('phone')
    otp = data.get('otp')
    if otp_storage.get(phone) == otp:
        with lock:
            otp_storage.pop(phone)
        return jsonify({"message": "OTP verified"}), 200
    return jsonify({"message": "Invalid OTP"}), 400


if __name__ == '__main__':
    app.run(debug=True)
