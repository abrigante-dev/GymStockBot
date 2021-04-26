import json
import boto3
import os
import subprocess
import requests
from requests.auth import HTTPBasicAuth 
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection
from random import randrange
from boto3.dynamodb.conditions import Key, Attr
import datetime

credentials = boto3.Session().get_credentials()
region = 'us-east-1'
service = 'es'
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
host = 'search-subscription-nhap2ubc42ftj27ho7fpciqtte.us-east-1.es.amazonaws.com'
x = randrange(10000)
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=('ses','ANOTHERawsELASTICMESS88!'),
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection)
    
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('User')


def subscribe(event):
    # add user to DyanamoDB User table
    global table
    table.put_item(
                    Item={
                        'UserName' : event['UserName'],
                        'Product' : event['ProductID'],
                        'Email' : event['Email'],
                        'Phone' : event['Phone'],
                        'NotificationFrequency' : event['Frequency']
                    }
                )
    # add user to subscribers in ES
    # first pull subscriber list and then add new subscriber to it
    global es
    pull=es.search(index='subscription', doc_type="_doc", body={"query": {"match": {"Name":event['ProductID']}}})
    subscribers = pull['hits']['hits'][0]['_source']['Subscribers']
    subscribers.append(event['UserName'])
    #update ES with the new subscriber added
    response = es.update(index='subscription',doc_type='_doc',id=event['ProductID'],
        body={"doc": {'Subscribers' : subscribers}})
    return 'Subscriber added'

def unsubscribe(event):
    global table
    # removes user from User DB table
    table.delete_item(
        Key={
            'UserName' : event['UserName'],
            'Product' : event['ProductID'],    
        }
       )
    global es
    # removes user from the Product subscribers array
    pull=es.search(index='subscription', doc_type="_doc", body={"query": {"match": {"Name":event['ProductID']}}})
    subscribers = pull['hits']['hits'][0]['_source']['Subscribers']
    subscribers.remove(event['UserName'])
    #update ES with the new subscriber added
    response = es.update(index='subscription',doc_type='_doc',id=event['ProductID'],
        body={"doc": {'Subscribers' : subscribers}})
    return "Subscriber removed"


def updateES():
    toJson = {
        'Name': 'ROGUE Olympic Plates',
        'Subscribers' : ['mm3443']
    }
    tempJsonObj = json.dumps(toJson, indent = 4)
    response = es.update(index='subscription',doc_type='_doc',id='ROGUE Olympic Plates',
        body={"doc": {'Subscribers' : ['mm3443']}})
    print(response)

def lambda_handler(event, context):
    try:
        if event['Subscribe'] == 'True':
            subscribe(event)
            return True
        elif event['Subscribe'] == 'False':
            unsubscribe(event)
            return True
        return False
    except:
        return {
            'statusCode': 200,
            'body': json.dumps('improper body request formatting')
        }
