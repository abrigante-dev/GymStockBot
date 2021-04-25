import json
import pickle
import boto3
import os
import subprocess
import requests
from requests.auth import HTTPBasicAuth 
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection

def putES():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Product')
    products = table.scan()
    toJsonList = []
    for item in products['Items']:
        if item['ID'] == 'Rogue Olympic Plates':
            toJsonList.append({
                'Name': item['ID'],
                'Subscribers' : ['mm3443']
            })
        else:
            toJsonList.append({
                'Name': item['ID'],
                'Subscribers' : []
            })
    
    print('about to push ES')
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
    
    for product in toJsonList:
        tempJsonObj = json.dumps(product, indent = 4)
        try:
            es.index(index='subscription', doc_type="_doc", id=product['Name'], body=tempJsonObj)
        except:
            continue
