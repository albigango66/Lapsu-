from flask import Flask, request
import requests
import uuid

app = Flask(__name__)
TOKEN = "7917068350:AAHbQz2VgdKrB4RjT9f43jRorcTcBOy30ZM"  # Replace with your BotFather token
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "Welcome! Use /getlink to generate an access link.")
        elif text == "/getlink":
            unique_id = str(uuid.uuid4())
            link = f"https://your-heroku-app.herokuapp.com/access/{unique_id}"
            send_message(chat_id, f"Share this link: {link}")
    return "OK", 200

def send_message(chat_id, text):
    requests.post(f"{TELEGRAM_API}/sendMessage", json={"chat_id": chat_id, "text": text})

if __name__ == "__main__":
    app.run()
