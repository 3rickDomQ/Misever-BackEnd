import boto3
from botocore.exceptions import ClientError
from botocore.retryhandler import HTTPStatusCodeChecker


def test():
    try:
        session = boto3.Session(profile_name='misever')
        ses = session.client('ses')
        test = ses.verify_email_address(
            EmailAddress = 'stxtest2021@gmail.com'
        )
    except ClientError as e:
        print(e.test['Error']['Message'])
    else:
        print(f"Verification email sent!\
            Status Code: {test['ResponseMetadata']['HTTPStatusCode']}")
