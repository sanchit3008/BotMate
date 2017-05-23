from apiai import ApiAI

CLIENT_ACCESS_TOKEN = "da359014f4414053b6bcf2192d05cbfa"

ai = ApiAI(CLIENT_ACCESS_TOKEN)

def response(message_text, sender_id):
	ai = ApiAI(CLIENT_ACCESS_TOKEN)
	request = ai.text_request()
	
	request.query = message_text
	response = request.getresponse()
	return response.read()