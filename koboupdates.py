import boto3
import os

def subcribeToSNS(email):

    accesskey = os.getenv('AWS_ACCESS_KEY')
    secretkey = os.getenv('AWS_SECRET_KEY')
    topic_arn = os.getenv('AWS_TOPIC_ARN')

    print(accesskey)
    print(secretkey)
    print(topic_arn)

    sns = boto3.client('sns',
                   aws_access_key_id=accesskey,
                   aws_secret_access_key = secretkey,
                   region_name="us-east-2")
    
    

    response = sns.subscribe(TopicArn=topic_arn,
                            Protocol='email', Endpoint=email)
    print(email)
    print(response)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else: return False

