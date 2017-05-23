from apiai import ApiAI
import json

CLIENT_ACCESS_TOKEN = "606b6ab2fb7640eb9ef0e29e9d6bd0c8"

ai = ApiAI(CLIENT_ACCESS_TOKEN)

def response(message_text):
	request = ai.text_request()
	request.query = "who are you"
	response = request.getresponse().read().decode('utf-8')
	obj = json.loads(response)
	return (obj["result"]["fulfillment"]["speech"])