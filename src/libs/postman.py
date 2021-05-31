# Python's Libraries
import re
import smtplib

# Django/Third-party Libraries

# Stx Libraries
from .security_type import SecurityType


class Postman():

    def __init__(self, _host, _security: SecurityType, _sender, _password):
        # Receives connection parameters and enables an email server with them
        # _security parameter only takes SecurityType data
        self.host = _host
        self.security = _security       # SecurityType
        self.sender = _sender
        self.password = _password
        self.recipient = []
        self.server = None
        self.init_Server()

    def init_Server(self):
        if type(self.security) != SecurityType:
            raise "SecurityType inválido"
        if self.security.value == SecurityType.SSL.value:
            self.server = smtplib.SMTP_SSL(self.host, self.security.value)
        if self.security.value == SecurityType.TLS.value:
            self.server = smtplib.SMTP(self.host, self.security.value)
            self.server.starttls()
        self.server.login(self.sender, self.password)

    def add_Recipient(self, _recipient):
        # Validates email format on parameter
        # if true, adds paramater to recipient list
        regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        if (re.search(regex, _recipient)):
            recipient = self.recipient
            recipient.append(_recipient)
        else:
            raise ValueError("Dirección de correo inválida")

    def del_Recipient(self, _recipient):
        # Deletes parameter from recipient list
        recipient = self.recipient
        recipient.remove(_recipient)
        self.recipient = recipient

    def send_Email(self, _message):
        # Receives a message object and sends it with
        # previously set parameteres
        if not self.recipient:
            raise "No se ha agregado ningun destinatario"
        try:
            _message['From'] = self.sender
            _message['To'] = ", ".join(self.recipient)
            self.server.sendmail(
                self.sender,
                self.recipient,
                _message.as_string()
            )
            print(f"Correo enviado exitosamente a {self.recipient}")
        except Exception as e:
            print(str(e))
