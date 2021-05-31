# Python Libraries
import re

# Django / Third-party Libraries
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

# Stx Libraries


class AWSPostman():

    def __init__(self, _profile=None):
        # Receives an aws profile from your local
        #  aws credentials file, creates a session
        # then initiates email server
        self.sender = None
        self.recipient = []
        self.server = None
        self.charset = 'UTF-8'
        self.regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        self.init_Session(_profile)

    def init_Session(self, _profile):
        if _profile:
            session = boto3.Session(profile_name=_profile)
            self.server = session.client('ses')
        else:
            session = boto3.Session()
            self.server = session.client('ses')

    def send_verification_email(self, _address):
        # Validates email format on _address
        # if true, sends verification email to _address
        if (re.search(self.regex, _address)):
            try:
                verify = self.server.verify_email_address(
                    EmailAddress=_address
                )
            except ClientError as e:
                print(e.verify['Error']['Message'])
            else:
                print(f"Verification email sent to {_address}!\
                    StatusCode:{verify['ResponseMetadata']['HTTPStatusCode']}")
        else:
            raise ValueError("Dirección de correo inválida")

    def add_Sender(self, _address):
        self.sender = _address

    def add_Recipient(self, _address):
        # Validates email format on _address
        # if true, adds _address to recipient list
        if (re.search(self.regex, _address)):
            recipient = self.recipient
            recipient.append(_address)
        else:
            raise ValueError("Dirección de correo inválida")

    def del_Recipient(self, _address):
        # Deletes _address from recipient list
        try:
            recipient = self.recipient
            recipient.remove(_address)
        except ValueError:
            raise ValueError(f"{_address} no se encuentra\
                            entre los destinatarios")

    def validate_Actors(self):
        if not self.sender:
            raise "No se ha agregado ninguna cuenta origen"
        if not self.recipient:
            raise "No se ha agregado ningun destinatario"

    def send_Email(self, _subject, _text):
        self.validate_Actors()
        subject = _subject
        body_text = _text
        body_html = _text
        try:
            response = self.server.send_email(
                Source=self.sender,
                Destination={
                    'ToAddresses': [
                        ", ".join(self.recipient),
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.charset,
                            'Data': body_html,
                        },
                        'Text': {
                            'Charset': self.charset,
                            'Data': body_text,
                        },
                    },
                    'Subject': {
                        'Charset': self.charset,
                        'Data': subject,
                    },
                }
            )

        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

    # def send_Email(self, subject, text):
    #     self.validate_Actors()
    #     subject = subject
    #     body_text = text
    #     body_html = text
    #     try:
    #         response = self.ses.send_email(
    #             Source=self.sender,
    #             Destination={
    #                 'ToAddresses': [
    #                     self.recipient,
    #                 ],
    #             },
    #             Message={
    #                 'Body': {
    #                     'Html': {
    #                         'Charset': self.charset,
    #                         'Data': body_html,
    #                     },
    #                     'Text': {
    #                         'Charset': self.charset,
    #                         'Data': body_text,
    #                     },
    #                 },
    #                 'Subject': {
    #                     'Charset': self.charset,
    #                     'Data': subject,
    #                 },
    #             }
    #         )

    #     except ClientError as e:
    #         print(e.response['Error']['Message'])
    #     else:
    #         print("Email sent! Message ID:"),
    #         print(response['MessageId'])
