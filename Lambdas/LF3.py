import os
import logging
import boto3
import json

from boto3.dynamodb.conditions import Key, Attr

# creates the HTML table that is returned to the front end
def createStockTable(stockInfo):
    # headers for the product table
    toReturn = [
        '<table style="margin-left:auto;margin-right:auto;">',
        '<tr>',
        '<th style="Color: white">In Stock Products</th>',
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
    print(event)
    searchIndex = event['searchIndex']
    searchKey = event['searchLabels']
    toReturn = pullDynamo(searchIndex, searchKey)

    return{
        'statusCode': 200,
        #'body': toReturn
        'body': ''.join(toReturn)
    }


# lambda_handler({'searchIndex': 'TYPE','searchLabels': 'BARBELL'}, 3)
