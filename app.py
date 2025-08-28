# Flask application for handling WhatsApp messages via Twilio webhook.
# Integrates with a "Weather Outfit Suggestion" agent to provide automated responses
# based on user input received through WhatsApp.

from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

from agent import agent  # Importing the "Weather Outfit Suggestion" Agent

app = Flask(__name__)

# Simple check in browser
@app.get("/")
def home():
    return "Flask is running. POST to /reply_whatsapp for Twilio."

# Twilio webhook
@app.route("/reply_whatsapp", methods=['POST'])
def reply_whatsapp():
    resp = MessagingResponse()

    # Get agent response
    user_message = request.form.get('Body', '')  # Get WhatsApp message body
    result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    agent_reply = result['messages'][-1].content

    resp.message(agent_reply)
    return Response(str(resp), mimetype='application/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
