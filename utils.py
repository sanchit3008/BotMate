from apiai import ApiAI
import json
import requests

CLIENT_ACCESS_TOKEN = "YOUR_TOKEN"

ai = ApiAI(CLIENT_ACCESS_TOKEN)

def response(message_text):
	#api.ai response
	request = ai.text_request()
	request.query = message_text
	response = request.getresponse().read().decode('utf-8')
	obj = json.loads(response)
	return (obj["result"]["fulfillment"]["speech"])


def gif_search(message_text):
	#giphy response
	search_phrase = message_text.replace(" ", "-")
	url = "http://api.giphy.com/v1/gifs/search?q=" + search_phrase + "&api_key=dc6zaTOxFJmzC&limit=1"
	response = requests.get(url)
	obj = response.json()
	return (obj["data"][0]["images"]["original"]["url"])
