# This file sends a WhatsApp message using Twilio API; useful for testing Twilio setup.
# When run, it sends the content in the 'body' variable to your WhatsApp number.
# Run this file to make sure that you are have connecting to Twilio/Whatsapp successfully

import os
from dotenv import load_dotenv
from twilio.rest import Client
from agent import agent  # Import your agent

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

# Get agent response
# user_message = "NYC Outfit Rec"
# result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
# agent_reply = result['messages'][-1].content

message = "I am recieving this message on whatsapp"

message = client.messages.create(
    from_ = 'whatsapp:+14155238886',            # May require changing based on your Twilio setup
    body = message,
    to = os.getenv("TWILIO_WHATSAPP_TO")        # The whatsapp number you have registered
)

print(message.sid)