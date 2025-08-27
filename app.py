from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

from agent import agent  # Import your agent

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
    user_message = "Karachi weather outfit suggestion today"
    result = agent.invoke({"messages": [{"role": "user", "content": user_message}]})
    agent_reply = result['messages'][-1].content

    resp.message(agent_reply)
    return Response(str(resp), mimetype='application/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
