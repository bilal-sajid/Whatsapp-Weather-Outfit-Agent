"""
This script sends a WhatsApp message to your registered number using the Twilio API.
Environment variables are loaded from a .env file for authentication and recipient details.
"""

import os
from dotenv import load_dotenv
from twilio.rest import Client
from agent import agent  # Import your agent

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

# Get agent response
user_message = "Karachi weather outfit suggestion today"
result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
agent_reply = result['messages'][-1].content

message = client.messages.create(
    from_ = 'whatsapp:+14155238886',
    body = agent_reply,
    to = os.getenv("TWILIO_WHATSAPP_TO")        # The whatsapp number you have registered
)

print(message.sid)