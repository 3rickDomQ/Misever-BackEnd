# Python Libraries

# Django / Third-party Libraries

# Stx Libraries
# from src.handler import lambda_handler
# from src.business.event_response import sample as event_test
from src.libs.aws_postman import AWSPostman
# event = event_test
# context = None

# lambda_handler(event, context)
postman = AWSPostman('misever')
postman.send_verification_email('admon@misever.com')
# ses = AWSPostman('misever')
# ses.send_Email(event, context)
