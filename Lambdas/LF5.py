import json
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
    
    
    
    client = boto3.client('sns')
    response = client.publish(
        PhoneNumber = payload["myphone"],
        Message = message,
        #Subject='Dining Concierge Recommendations',
        MessageStructure = 'string',
        MessageDeduplicationId = payload["myphone"],
        MessageGroupId = payload["myphone"],
        MessageAttributes={
            "DefaultSMSType":{
                "StringValue": "Transactional",
                "DataType":"String"
            }
        }
    )    
    
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
