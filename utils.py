from apiai import ApiAI

CLIENT_ACCESS_TOKEN = "da359014f4414053b6bcf2192d05cbfa"

ai = ApiAI(CLIENT_ACCESS_TOKEN)

def response(message_text):
	request = ai.text_request()
	request.query = "who are you"
	response = request.getresponse().read().decode('utf-8')
	obj = json.loads(response)
	return (obj["result"]["fulfillment"]["speech"])