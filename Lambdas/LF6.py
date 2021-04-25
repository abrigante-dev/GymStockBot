import logging
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

# uses the event['list'] as the table name
def pullDynamo(tableName):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    
    pull = table.scan(
            FilterExpression=Attr('Active').eq('True')
        )
    # alphabetical based on list 
    sortedList = sorted(pull['Items'], key=lambda k: k[tableName])
        
    jsonObj = json.dumps(sortedList, indent = 4)
    print(jsonObj)
    return jsonObj
    
    
def lambda_handler(event, context):
    
    try:
        return pullDynamo(event['list'])
    except:
        return {
            'statusCode': 200,
            'body': json.dumps('list type required')
        }
        
    
