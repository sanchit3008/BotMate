from apiai import ApiAI
import json

CLIENT_ACCESS_TOKEN = "727479e377c14bc293f88801c713a07f"

ai = ApiAI(CLIENT_ACCESS_TOKEN)

def response(message_text):
	request = ai.text_request()
	request.query = "who are you"
	response = request.getresponse().read().decode('utf-8')
	obj = json.loads(response)
	return (obj["result"]["fulfillment"]["speech"])