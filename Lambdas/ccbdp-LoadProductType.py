import json
import boto3
import random

def lambda_handler(event, context):
    items = [
        {
            'Active': 'True',
            'Type': 'RACK',
            'URL': './images/rackbutton.png',
            'LastUpdate': '2021-04-23 06:30:28'
        }, {
            'Active': 'True',
            'Type': 'BARBELL',
            'URL': './images/barbellbutton.png',
            'LastUpdate': '2021-04-23 06:30:28'
        }, {
            'Active': 'True',
            'Type': 'PLATES',
            'URL': './images/platebutton.png',
            'LastUpdate': '2021-04-23 06:30:28'
        }, {
            'Active': 'True',
            'Type': 'DUMBBELL',
            'URL': './images/dumbellbutton.png',
            'LastUpdate': '2021-04-23 06:30:28'
        }, {
            'Active': 'True',
            'Type': 'BENCH',
            'URL': './images/benchbutton.png',
            'LastUpdate': '2021-04-23 06:30:28'
        }, {
            'Active': 'True',
            'Type': 'ROWER',
            'URL': './images/rowerbutton.png',
            'LastUpdate': '2021-04-23 06:30:28'      
        }, {
            'Active': 'True',
            'Type': 'ROPE',
            'URL': './images/ropebutton.png',
            'LastUpdate': '2021-04-23 06:30:28'   
        }, {
            'Active': 'True',
            'Type': 'TRAINER',
            'URL': './images/trainerbutton.png',
            'LastUpdate': '2021-04-23 06:30:28'   
        }, {
            'Active': 'True',
            'Type': 'ACCESSORY',
            'URL': './images/accessoriesbutton.png',
            'LastUpdate': '2021-04-23 06:30:28'   
        }, {
            'Active': 'True',
            'Type': 'KETTLEBELL',
            'URL': './images/kettlebellsbutton.png',
            'LastUpdate': '2021-04-23 06:30:28'   
        }, {
            'Active': 'True',
            'Type': 'BIKE',
            'URL': './images/bikebutton.png',
            'LastUpdate': '2021-04-23 06:30:28'               
        }
    ]

    dynamodbclient=boto3.resource('dynamodb')
    type = dynamodbclient.Table('Type')
    
    #id = str(random.randint(0,10000000))
    for item in items:
        response = type.put_item(Item=item)
        print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
