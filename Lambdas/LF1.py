import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from enum import Enum
import boto3
import json


# enum just makes it easy to say which manufactorer in plain english
class Manufacturer(Enum):
    ROGUE = 'ROGUE'
    TITAN = 'TITAN'
    REP = 3
    POWERBLOCK = 4


# ####scrape functions are independent to the manufactorer
# scrapes titan fitness to check if an item is in stock
def scrapeTitan(url):
    print('scraping titan')
    chrome_driver_path = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)
    driver.get(url)
    page = str(driver.page_source).splitlines()
    for line in page:
        tempList = line.split()
        for word in tempList:
            if word == 'class="out-of-stock--notify"':
                print('Titan Out of Stock')
                driver.quit()
                return False
    print('Titan In Stock')
    driver.quit()
    return True


# scrapes titan fitness to check if an item is in stock
def scrapeRep(url):
    # placeholder right now
    print('scraping rep fitness')
    chrome_driver_path = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)
    driver.get(url)
    page = str(driver.page_source).splitlines()
    for line in page:
        tempList = line.split()
        for word in tempList:
            if word == '<span>Out':
                print('Rep Out of Stock')
                driver.quit()
                return False
    print('Rep In Stock')
    driver.quit()
    return True
    return False


# scrapes the rogue site to determine if the item is in stock
def scrapeRogue(url):
    chrome_driver_path = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)
    driver.get(url)
    page = str(driver.page_source).splitlines()
    for line in page:
        tempList = line.split()
        for word in tempList:
            if word == 'title="Add':
                print('In Stock')
                driver.quit()
                return True
    print('Out of stock')
    driver.quit()
    return False


def scrapeSite(Manufacturer, url):
    if Manufacturer is Manufacturer.ROGUE:
        return scrapeRogue(url)
    elif Manufacturer is Manufacturer.TITAN:
        return scrapeTitan(url)
    elif Manufacturer is Manufacturer.REP:
        return scrapeRep(url)


# returns True for in stock, False for out of stock
def checkStock(Company, url):
    return scrapeSite(Manufacturer(Company), url)

#pull all items being tracked in dynamoDB and update their stock status
def updateStock():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('stock-items')
    #response = []
    response = table.scan()
    #print(response)
    for item in response['Items']:
        tempStock = checkStock(item['COMPANY'], item['URL'])
        updateResponse = table.update_item(
            Key={
                'ID' : item['ID']
            },
            UpdateExpression='set STOCK = :r',
            ExpressionAttributeValues={
                ':r': tempStock,
            },
            ReturnValues='UPDATED_NEW'
        )

def downloadStock():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('stock-items')
    # response = []
    response = table.scan()
    print(response['Items'])
    # print(response)
    #for item in response['Items']:
    #with open('data.json', 'w') as outfile:
     #   json.dump(response['Items'], outfile)
    #json_obj = json.dumps(response['Items'], indent = 4)
    #print(json_obj)


#scrapeRep('https://www.repfitness.com/bars-plates/olympic-bars/20kg-men-s-bars/rep-sabre-bar')
updateStock()
#downloadStock()
