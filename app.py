import os, sys
from flask import Flask, request
from utils import response, gif_search
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAYf2X7qS5kBAArGwzRJqJ2JlI1A7CorSl31dHxEMqDNz3W8kUqY28JqT4X9Y84vnqnE7MJOuZBlZBxYyxiXg5AWEaeyLQY27x7cnfZAXFgAtWKH7UFmKPCivnQxzo4sDpSUuvuw0jwMixfmESigL5RZBKvbRyiQ9cFsftI5FwZDZD"

bot = Bot(PAGE_ACCESS_TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:
				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					if messaging_text[:3].lower() == "gif":
						bot.send_image_url(sender_id, gif_search(messaging_text[4:]))
					elif messaging_text.lower() == "get started":
						bot.send_text_message(sender_id, 'You can chat with me, and also search for gifs. For eg -"gif cats"')
					else:
						bot.send_text_message(sender_id, response(messaging_text))

	return "ok", 200

def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
	app.run(debug = True, port = 1200)