# SMS-bomber-python

OTP Server with Twilio & Flask 📱🔐
A simple and scalable OTP (One Time Password) System using Twilio for sending SMS messages, built with Flask and Python 🐍.
This server supports multiple Twilio phone numbers, sends shuffled messages from a text file, and provides an easy-to-use API to send and verify OTPs. 🚀

Features ✨
OTP Generation: Secure 6-digit OTP generated randomly 🔑.

Multiple Twilio Numbers: Sends OTPs from multiple Twilio numbers, selected randomly 📞.

Shuffled Messages: Messages are loaded from a text file and shuffled to provide variety 📜.

Rate-Limiting: Prevents sending multiple OTPs to the same phone within a short time ⏳.

OTP Expiry: OTPs expire after 5 minutes (configurable) ⏰.

Flask API: Simple REST API for sending and verifying OTPs 📡.


Prerequisites 🛠️
Python 3.x 🐍

Twilio account with an SMS-enabled phone number (or multiple numbers) 📲

Flask and Twilio Python libraries 🛠️


Installation ⚙️
1. Clone the Repository
bash
Copy
Edit
git clone (https://github.com/Kannan-hub-byte/SMS-bomber-python)
cd otp-server
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set up Twilio Account
Create a Twilio account 🌐.

Obtain your Account SID and Auth Token 🔑.

Add your Twilio phone numbers to the TWILIO_PHONE_NUMBERS list in the script 📞.


4. Create messages.txt
Create a file named messages.txt and add your message templates 💬.

Example content of messages.txt:

css
Copy
Edit
Your OTP is: {otp}
Your verification code: {otp}
One-time code for verification: {otp}
Your code: {otp}


Running the Server 🚀
To run the OTP server:

bash
Copy
Edit
python app.py
The server will start on http://127.0.0.1:5000/ 🌍.


API Endpoints 📡
1. Send OTP ✉️
Endpoint:
POST /send-otp

Request:
json
Copy
Edit
{
  "phone": "+12345678901"
}

Response:
json
Copy
Edit
{
  "message": "OTP sent successfully"
}

2. Verify OTP ✅
Endpoint:
POST /verify-otp

Request:
json
Copy
Edit
{
  "phone": "+12345678901",
  "otp": "123456"
}

Response:
json
Copy
Edit
{
  "message": "OTP verified"
}


Logging 📜
All activities are logged to otp_server.log for monitoring and debugging purposes 🔍.

License 📝
This project is licensed under the MIT License 🏷️.


