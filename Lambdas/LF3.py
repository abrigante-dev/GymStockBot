import math
import dateutil.parser
import datetime
import time
import os
import logging
import boto3
import json
from datetime import datetime
import http.client
import requests
import time
import random
from boto3.dynamodb.conditions import Key, Attr

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# creates the HTML table that is returned to the front end
def createStockTable(stockInfo):
    # headers for the product table
    toReturn = [
        '<table>',
        '<tr>',
        '<th>Product</th>',
        '</tr>'
    ]
    for item in stockInfo['Items']:
        toReturn.append('<tr>')
        toReturn.append('<td><a href="{}">{}</a></td>'.format(item['URL'],item['NAME']))
        toReturn.append('</tr>')

    toReturn.append('</table>')
    return toReturn

# pulls the stock information on a given item based on company or type of item (barbell, rack, etc.)
def pullDynamo(searchIndex, searchKey):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('stock-items')
    response = {}
    if searchIndex == 'COMPANY':
        response = table.scan(
            FilterExpression=Attr('COMPANY').eq(searchKey) & Attr('STOCK').eq(True)
        )
    else:
        response = table.scan(
            FilterExpression=Attr('TYPE').eq(searchKey) & Attr('STOCK').eq(True)
        )

    return createStockTable(response)
    # return responses

# if 'searchLabels' in intent_request.keys():

def lambda_handler(event, context):

    searchIndex = event['searchIndex']
    searchKey = event['searchLabels']
    print(pullDynamo(searchIndex, searchKey))

    return{
        'statusCode': 200,
        'body': 'Successfully returned stock status to front panel'
    }


lambda_handler({'searchIndex': 'TYPE','searchLabels': 'BARBELL'}, 3)