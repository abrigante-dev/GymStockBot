import json
import boto3
import random

def lambda_handler(event, context):
    items = [
        {
            'Active': 'True',
            'Manufacturer': 'TITAN',
            'URL': './images/titanBanner.jpg',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'Active': 'True',
            'Manufacturer': 'ROGUE',
            'URL': './images/rogueBanner.jpg',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'Active': 'True',
            'Manufacturer': 'REP',
            'URL': './images/repBanner.jpg',
            'LastUpdate': '2021-04-23 5:30:28'
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
