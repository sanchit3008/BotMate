import os, sys
from flask import Flask, request
from utils import response, gif_search
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "YOUR_TOKEN"

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

				if messaging_event.has_key('postback'):
					postback_event = messaging_event['postback']['payload']
					if postback_event == "help":
						bot.send_text_message(sender_id, 'I can talk to you, and also search for gifs. Try typing "gif cats" ;) ')


				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					if messaging_text[:3].lower() == "gif":
						if(len(messaging_text[4:])<2):
							bot.send_text_message(sender_id, "Enter a longer search phrase :) ")
						else:
							bot.send_image_url(sender_id, gif_search(messaging_text[4:]))
					else:
						if response(messaging_text) == "":
							bot.send_text_message(sender_id, response("responsetogibberish"))
						elif messaging_text.lower() == "help":
							bot.send_text_message(sender_id, 'I can talk to you, and also search for gifs. Try typing "gif cats" ;) ')
						else:
							bot.send_text_message(sender_id, response(messaging_text))

	return "ok", 200

def log(message):
	print(message)
	sys.stdout.flush()

if __name__ == "__main__":
	app.run(debug = True, port = 1200)
