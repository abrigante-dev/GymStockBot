import json
import pickle
import boto3
import os
import subprocess
import requests
from requests.auth import HTTPBasicAuth 
from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection
from random import randrange
from boto3.dynamodb.conditions import Key, Attr
#from datetime import datetime
import datetime


# temp function to load elasticsearch
def putES():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Product')
    products = table.scan()
    toJsonList = []
    for item in products['Items']:
        if item['NAME'] == 'Rogue Olympic Plates':
            toJsonList.append({
                'Name': item['NAME'],
                'Subscribers' : ['mm3443']
            })
        else:
            toJsonList.append({
                'Name': item['NAME'],
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
        es.index(index='products', doc_type="_doc", id=product['Name'], body=tempJsonObj)


def updateLastNotification(userInfo):
    ('setting new LastNotificationTime in dynamoDB')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('User')
    notificationTime = datetime.datetime.now()
    dtString = notificationTime.strftime('%Y-%m-%d %H:%M:%S')
    updateResponse = table.update_item(
            Key={
                'UserName' : userInfo['UserName']
            },
            FilterExpression=Attr('Product').eq(userInfo['Product']),
            UpdateExpression='set LastNotificationSent = :r',
            ExpressionAttributeValues={
                ':r': dtString,
            },
            ReturnValues='UPDATED_NEW'
        )


def sendEmail(userInfo):
    SENDER = "ses@caspercreations.org"
    RECIPIENT = userInfo['Email']
    #RECIPIENT = 'anbrigante@gmail.com'
    AWS_REGION = "us-east-1"
    SUBJECT = "Gym Stock Bot Notice: {}".format(userInfo['Product'])
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('stock-items')
    
    response = table.scan(
        FilterExpression=Attr('NAME').eq(userInfo['Product'])
    )
    
    
    BODY_TEXT = ("{} are now in stock. Follow the URL below.\n".format(userInfo['Product']) +
    "{}".format(response['Items'][0]['URL']))
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h4>{} are now in stock. Follow the URL below.</h4>
    <p>{}</p>
    </body>
    </html>
             """.format(userInfo['Product'], response['Items'][0]['URL']) 
    
    print(BODY_TEXT)
    
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER
        )
        print(response)
        # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        


def sendText(userInfo):
    print('sending text')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('stock-items')
    response = table.scan(
        FilterExpression=Attr('NAME').eq(userInfo['Product'])
    )
    sns = boto3.client('sns', 'us-east-1')
    message = "{} are now in stock. Follow the URL below. Thanks! \n{}".format(userInfo['Product'], response['Items'][0]['URL'])
    print('text message: {}'.format(message))
    phoneNumber = '+1' + userInfo['Phone']
    #phoneNumber = '+16199886253'
    print(sns.publish(Message=message, PhoneNumber = phoneNumber))



def getSubInfo(username):
    print('getting subscriber info')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('User')
    response = table.query(
        KeyConditionExpression=Key('UserName').eq(str(username))
    )
    userInfo = response['Items'][0]
    print('user info: {}'.format(userInfo))
    
    lastSentDT = datetime.datetime.strptime(userInfo['LastNotificationSent'], '%Y-%m-%d %H:%M:%S')
    currentDT = datetime.datetime.now()
    diff = currentDT - lastSentDT
    hours = diff.days * 24
    if hours >= int(userInfo['NotificationFrequency']):
        if len(userInfo['Phone']) > 0:
            sendText(userInfo)
        if len(userInfo['Email']) > 0:
            sendEmail(userInfo)
        #updateLastNotification(userInfo)
            


# gets the subscribers from ES for each of the items in the in stock list and notifies them
def getSubscribers(itemList):
    print('getting list of subscribers for each in stock item')
    credentials = boto3.Session().get_credentials()
    region = 'us-east-1'
    service = 'es'
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
    host = 'search-products-v3vrg5jkpzquexer22cirpf53m.us-east-1.es.amazonaws.com'
    es = Elasticsearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=('ccbdp','MichaelIsTheBest1!'),
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection)
    
    # for each item in item list, check if there is anyone subscribed and notify them
    for item in itemList:
        pull =es.search(index='products', doc_type="_doc", body={"query": {"match": {"Name":item}}})
        #print(pull['hits']['hits'][0]['_source']['Name'])
        subscribers = pull['hits']['hits'][0]['_source']['Subscribers']
        if len(subscribers) > 0:
            print(subscribers)
            for sub in subscribers:
                getSubInfo(sub)
        


# gets the list of in stock items from the s3 bucket
def getStockList(key, fileName):
    s3 = boto3.resource('s3')
    itemList = []
    with open(fileName, 'wb') as data:
        s3.Bucket("ccbdp-gymstockbotbucket").download_fileobj(key, data)
        
    with open(fileName, 'rb') as data:
        itemList = pickle.load(data)
    
    #return itemList
    getSubscribers(itemList)
    
def lambda_handler(event, context):
    #s3 = boto3.client('s3')
    key = str(event['Records'][0]['s3']['object']['key'])
    #key = "20210424-150131"
    fileName = "/tmp/{}.pkl".format(key)
    print("fileName: {}".format(fileName))
    itemList = []
    getStockList(key, fileName)
    #putES()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
