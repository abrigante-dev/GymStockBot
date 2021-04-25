import json
import boto3
import random

def lambda_handler(event, context):
    #id = str(random.randint(0,10000000))
    items = [
        {
            'UserName': 'mm3443', 
            'Email': 'mm3443@columbia.edu',
            'Phone': '9145894194',
            'Product': 'ROGUE Machined Olympic Plates',
            'NotificationFrequency': 24,
            'LastNotificationSent': '2021-04-20 10:00:00'        
        },
        {
            'UserName': 'mm3443', 
            'Email': 'mm3443@columbia.edu',
            'Phone': '9145894194',
            'Product': 'REP Pull-Up Bands',
            'NotificationFrequency': 24,
            'LastNotificationSent': '2021-04-20 10:00:00'        
        }        
    ]
    
    dynamodbclient=boto3.resource('dynamodb')
    users = dynamodbclient.Table('User')
    
    for item in items:
        response = users.put_item(Item=item)
        print(response)


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }