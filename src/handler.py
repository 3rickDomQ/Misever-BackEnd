# Python Libraries
import json

# Django / Third-party Libraries

# Stx Libraries
from src.libs.aws_postman import AWSPostman


def lambda_handler(event, context):
	postman = AWSPostman()
	postman.add_Sender('stxtest2021@gmail.com')
	postman.add_Recipient('francisco.germain@gmail.com')
	data = eval(event['body'])
	subject = f"Contacto MISEVER"
	text = f"Se ha recibido la siguiente informacion en tu\
		formulario de contacto:\n\
		Nombre:{data['name']} Correo:{data['correo']}\
		Teléfono:{data['telefono']} mensaje:{data['mensaje']}"
	postman.send_Email(subject, text)
	return {
		"statusCode": 200,
		"headers": {
		"Content-Type": "application/json"
		},
		"body": json.dumps({
		"detail ": "Envío Exitoso!"
		})
	}