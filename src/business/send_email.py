# Python Libraries

# Django / Third-party Libraries
import boto3
from botocore.exceptions import ClientError

# Stx Libraries

def lambda_handler(event, context):
    print(event)
    sender = 'stxtest2021@gmail.com'
    recipient = 'stxtest2021@gmail.com'
    subject = "aws ses test"
    body_text = ("Amazon SES Test (Python)\r\n"
                "This email was sent with Amazon SES using the "
                "AWS SDK for Python (Boto)."
            )
    body_html = """<html>
    <head></head>
    <body>
        <h1>Amazon SES Test (SDK for Python)</h1>
        <p>This email was sent with
            <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
            <a href='https://aws.amazon.com/sdk-for-python/'>
                AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
            """
    try:
        response = ses.send_email(
            Source=sender,
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': charset,
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': charset,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': subject,
                },
            }
        )

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

    # return {
    #     "statusCode": 200,
    #     "headers": {
    #         "Content-Type": "application/json"
    #     },
    #     "body": json.dumps({
    #         "detail ": "Hola mundo!"
    #     })
    # }
