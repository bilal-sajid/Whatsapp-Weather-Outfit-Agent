
# 👕🌤️ WhatsApp Weather Outfit Agent with Flask + Twilio

This project is a `Weather Outfit Suggestion Agent`, accessible via WhatsApp using Flask and Twilio’s WhatsApp API. Users send a city name, and the agent responds with today’s forecast (morning, afternoon, evening, night) along with outfit advice based on temperature, rain, wind, and UV index.

## How it works
1. A user sends a WhatsApp message (e.g., “Paris” or “Outfits Paris").
2. Twilio forwards the message to the Flask webhook (`/reply_whatsapp`).
3. The webhook calls the Weather Outfit Agent, which fetches and summarizes today’s weather and generates outfit recommendations based on the weather.
4. It then delivers the weather summary and outfit recommendations back to the user on WhatsApp.

<div align="center">

![Demo of WhatsApp Weather Outfit Agent](./assets/demo.gif)

</div>

## Requirements
To run this project, you will need:
- A Twilio account with WhatsApp Sandbox enabled
- An OpenWeather API key (version 3.0; free for up to 1000 calls)
- An OpenAI API key

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/bilal-sajid/Whatsapp-Weather-Outfit-Agent.git
cd Whatsapp-Weather-Outfit-Agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Copy `.env.sample` to `.env` and fill in your credentials:
```bash
cp .env.sample .env
```

Edit `.env` and provide your Twilio, OpenAI, and OpenWeather API keys.

### 4. Test WhatsApp connection

Once you have filled in your `.env` credentials, run the following command to check if your WhatsApp connection is successful:

```bash
python twilio_connection.py
```

This will send a WhatsApp message with the body specified in `twilio_connection.py` to your configured WhatsApp number. If you receive the message, your Twilio setup is working correctly.

### 5. Run the application
```bash
python app.py
```

The server will start on `http://0.0.0.0:8080`.

### 6. Expose your local server with Localtunnel

After starting your Flask server, run the following in your terminal:

```bash
npm install -g localtunnel
lt --port 8080
```

Localtunnel will provide a public URL (e.g., `https://your-subdomain.loca.lt`).
Copy this URL.

### 7. Configure Twilio Sandbox

- Go to your Twilio Sandbox configuration page.
- Paste the Localtunnel URL with `/reply_whatsapp` appended (e.g., `https://your-subdomain.loca.lt/reply_whatsapp`) into the **WHEN A MESSAGE COMES IN** webhook field.
- Save the configuration.

Now, when you send a WhatsApp message to your Twilio Sandbox number, your Flask app will automatically reply!


## File Structure
- `app.py`  
  Main Flask application. Handles incoming WhatsApp messages via Twilio webhook and routes them to the agent for responses.

- `agent.py`  
  Defines the weather outfit suggestion agent. Uses tools to fetch weather data and generate outfit advice.

- `helper.py`  
  Contains utility functions used across the project, such as formatting and data processing.

- `tools.py`  
  Implements functions for geolocation and weather retrieval from external APIs.

- `twilio_connection.py`  
  Manages Twilio API setup and connection for sending/receiving WhatsApp messages.

- `.env.sample`  
  Example environment variable file. Copy to `.env` and fill in your API keys and credentials.
