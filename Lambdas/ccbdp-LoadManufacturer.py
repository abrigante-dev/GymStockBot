import json
import boto3
import random

def lambda_handler(event, context):
    items = [
        {
            'Active': 'True',
            'Manufacturer': 'TITAN',
            'URL': './images/titanbutton.png',
            'LastUpdate': '2021-04-23 05:30:28'
        }, {
            'Active': 'True',
            'Manufacturer': 'ROGUE',
            'URL': './images/roguebutton.png',
            'LastUpdate': '2021-04-23 05:30:28'
        }, {
            'Active': 'True',
            'Manufacturer': 'REP',
            'URL': './images/repbutton.png',
            'LastUpdate': '2021-04-23 05:30:28'
        }
    ]

    dynamodbclient=boto3.resource('dynamodb')
    manufacturer = dynamodbclient.Table('Manufacturer')

    for item in items:
        response = manufacturer.put_item(Item=item)
        print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
