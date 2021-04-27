import os
import logging
import boto3
import json
import os
import subprocess
import requests
from requests.auth import HTTPBasicAuth 
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection
from boto3.dynamodb.conditions import Key, Attr


def getTopItems():
    credentials = boto3.Session().get_credentials()
    region = 'us-east-1'
    service = 'es'
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
    host = 'search-subscription-nhap2ubc42ftj27ho7fpciqtte.us-east-1.es.amazonaws.com'
    es = Elasticsearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=('ses','ANOTHERawsELASTICMESS88!'),
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection)
    
    #pull =es.search(index='subscription', doc_type="_doc", body={"query": {"match": {"Name":item}}})
    
    pull =es.search(index='subscription', doc_type="_doc", size = 348)
    # print('hits: {}'.format(pull['hits']['hits']))
    subscribeCount = {}
    for item in pull['hits']['hits']:
        tempCount = len(list(item['_source']['Subscribers']))
        tempName = item['_source']['Name']
        subscribeCount[tempName] = tempCount
     
    sortedDict = sorted(subscribeCount.items(), key=lambda x: x[1], reverse=True)
   
    return sortedDict


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
        toReturn.append('<td><a href="{}">{}</a></td>'.format(item['URL'],item['ID']))
        toReturn.append('</tr>')

    toReturn.append('</table>')
    return toReturn

# pulls the stock information on a given item based on company or type of item (barbell, rack, etc.)
def pullDynamo(searchIndex, searchKey):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Product')
    response = {}
    if searchIndex == 'COMPANY':
        response = table.scan(
            FilterExpression=Attr('Manufacturer').eq(searchKey) & Attr('InStock').eq('True')
        )
    else:
        response = table.scan(
            FilterExpression=Attr('Type').eq(searchKey) & Attr('InStock').eq('True')
        )
    
    return createStockTable(response)
    # return responses

# if 'searchLabels' in intent_request.keys():

def lambda_handler(event, context):
    print(event)
    searchIndex = event['searchIndex']
    searchKey = event['searchLabels']
    toReturn = pullDynamo(searchIndex, searchKey)

    #toReturn = getTopItems()
    
    return{
        'statusCode': 200,
        #'body': toReturn
        'body': ''.join(toReturn)
    }


# lambda_handler({'searchIndex': 'TYPE','searchLabels': 'BARBELL'}, 3)
