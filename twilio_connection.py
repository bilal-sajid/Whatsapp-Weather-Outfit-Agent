"""
This script sends a WhatsApp message to your registered number using the Twilio API.
Environment variables are loaded from a .env file for authentication and recipient details.
"""

import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_ = 'whatsapp:+14155238886',
    body = 'Agent Message will be here',
    to = os.getenv("TWILIO_WHATSAPP_TO")        # The whatsapp number you have registered
)

print(message.sid)