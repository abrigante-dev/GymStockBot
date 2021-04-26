import os
import logging
import boto3
import json
import subprocess
import requests
from requests.auth import HTTPBasicAuth 
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection
from boto3.dynamodb.conditions import Key, Attr

username = ''
masterProduct = {}

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


# creates the HTML table that is returned to the front end
def createStockTable(itemTuple):
    global username
    
    userDict = {}
    for item in itemTuple:
        key, value = item[0], item[1]
        userDict[key] = value
        
    print(userDict)
    # headers for the product table
    toReturn = [
        '<table>',
        '<tr>',
        '<th></th>',
        '</tr>'
    ]
    for item in itemTuple:
        tempItem = next(x for x in masterProduct if x["ID"] == item[0])
        toReturn.append('<tr>')
        # name-hyperlink
        toReturn.append('<td><a href="{}" target="_blank">{}</a></td>'.format(tempItem['URL'],tempItem['ID']))
        
        if len(username) == 0:
            if userDict[tempItem['ID']] == 'True':
                toReturn.append('<td class="subscribeTd"><input type="submit" class="productButton" class="productSubscribe" onclick="productSubscribe({})" value="Subscribe"></td>'.format(tempItem['ID']))
            else:
                toReturn.append('<td class="subscribeTd"><input type="submit" class="productButton" class="productUnsubscribe" onclick="productUnsubscribe({})" value="Unsubscribe"></td>'.format(tempItem['ID']))
        
        toReturn.append('</tr>')

    toReturn.append('</table>')
    #print(toReturn)
    return toReturn
   

def checkSubscription(sortedDict):
    toReturn = []
    for item in sortedDict:
        pull=es.search(index='subscription', doc_type="_doc", body={"query": {"match": {"Name":item[0]}}})
        subscribers= list(pull['hits']['hits'][0]['_source']['Subscribers'])
        if username in subscribers:
            toReturn.append([item[0],'True'])
        else:
            toReturn.append([item[0],'False'])
            
    print(toReturn)
    #return toReturn
    return createStockTable(toReturn)

def sortItems(items):
    #pull =es.search(index='subscription', doc_type="_doc", body={"query": {"match": {"Name":item}}})
    subscribeCount = {}
    for item in items:
        pull=es.search(index='subscription', doc_type="_doc", body={"query": {"match": {"Name":item}}})
        subscribeCount[item] = len(list(pull['hits']['hits'][0]['_source']['Subscribers']))
        
    sortedDict = sorted(subscribeCount.items(), key=lambda x: x[1], reverse=True)
    return checkSubscription(sortedDict)


# pulls the stock information on a given item based on company or type of item (barbell, rack, etc.)
def pullDynamo(searchType, searchKey, searchScope, username):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Product')
    response = {}
    if searchScope == 'InStock':
        response = table.scan(
                FilterExpression=Attr(searchType).eq(searchKey) & Attr('InStock').eq('True')
            )
    else:
        response = table.scan(
                FilterExpression=Attr(searchType).eq(searchKey)
            )
    global masterProduct
    masterProduct = response['Items']
    print(response['Items'])
    items = []
    for item in response['Items']:
        items.append(item['ID'])
        
        
    return sortItems(items)
    # return responses

# if 'searchLabels' in intent_request.keys():

def lambda_handler(event, context):
    print(event)
    
    searchType = event['SearchType']
    searchKey = event['SearchKey']
    searchScope = event['SearchScope']
    global username
    username = event['UserName']
    toReturn = pullDynamo(searchType, searchKey, searchScope, username)
    return toReturn

    return{
        'statusCode': 200,
        #'body': toReturn
        'body': 'Error is post body request format'
    }



