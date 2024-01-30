import boto3
import os

def subcribeToSNS(email):

    sns = boto3.client('sns',
                   aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                   aws_secret_access_key = os.environ.get('AWS_SECRET_KEY'),
                   region_name="us-east-2")
    
    topic_arn = os.environ.get('AWS_TOPIC_ARN')

    response = sns.subscribe(TopicArn=topic_arn,
                            Protocol='email', Endpoint=email)
    print(email)
    print(response)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else: return False

