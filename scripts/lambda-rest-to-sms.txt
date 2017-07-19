import boto3
import os

sns = boto3.client('sns')

def lambda_handler(event, context):
    
    sns.publish(
        TopicArn = os.environ['SNS_TOPIC'],
        Message = event['queryStringParameters']['message']
    )

    return {
            'statusCode': "200",
            'body': "Lambda has just send a SMS: " + event['queryStringParameters']['message'],
            'headers': {
                'Content-Type': 'text/html',
            }
        }