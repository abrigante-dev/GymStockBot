import json
import boto3
import random

def lambda_handler(event, context):
    items = [
        {
            'InStock': 'True',
            'ID': 'TITAN T-2 SERIES POWER RACK',
            'Type': 'RACK',
            'Product': 'T-2 SERIES POWER RACK',
            'URL': 'https://www.titan.fitness/racks/power-racks/t-2-series/t-2-series-power-rack/T2-SERIES-RACK.html',
            'Manufacturer': 'TITAN',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'ID': 'ROGUE Euro 28MM Olympic Weightlifting Bar',
            'Product': 'Rogue Euro 28MM Olympic Weightlifting Bar',
            'Type': 'BARBELL',
            'Manufacturer': 'ROGUE',
            'URL': 'https://www.roguefitness.com/28-mm-rogue-eu-oly-wl-bar-with-center-knurl-rogue-hg-clear-shaft-chrome-sleeve',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'ID': 'REP IRON PLATES',
            'Type': 'PLATES',
            'Product': 'REP IRON PLATES',
            'URL': 'https://www.repfitness.com/bars-plates/olympic-plates/iron-plates/rep-iron-plates',
            'Manufacturer': 'REP',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'ROGUE HG 2.0 Bumper Plates',
            'Type': 'PLATES',
            'Product': 'Rogue HG 2.0 Bumper Plates',
            'URL': 'https://www.roguefitness.com/rogue-hg-2-0-bumper-plates',
            'Manufacturer': 'ROGUE',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'ROGUE The Ohio Bar - Cerakote',
            'Type': 'BARBELL',
            'Product': 'The Ohio Bar - Cerakote',
            'URL': 'https://www.roguefitness.com/the-ohio-bar-cerakote',
            'Manufacturer': 'ROGUE',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'ROGUE SML-2C Squat Stand',
            'Type': 'RACK',
            'Product': 'Rogue SML-2C Squat Stand',
            'URL': 'https://www.roguefitness.com/rogue-sml-2c-squat-stand',
            'Manufacturer': 'ROGUE',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'ROGUE Flat Utility Bench 2.0',
            'Type': 'BENCH',
            'Product': 'Rogue Flat Utility Bench 2.0',
            'URL': 'https://www.roguefitness.com/rogue-flat-utility-bench',
            'Manufacturer': 'ROGUE',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'REP FB-3000 FLAT BENCH',
            'Type': 'BENCH',
            'Product': 'REP FB-3000 FLAT BENCH',
            'URL': 'https://www.repfitness.com/strength-equipment/strength-training/benches/rep-flat-bench-with-storage',
            'Manufacturer': 'REP',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'ID': 'REP BASIC BARBELL',
            'Type': 'BARBELL',
            'Product': 'REP BASIC BARBELL',
            'URL': 'https://www.repfitness.com/bars-plates/olympic-bars/20kg-men-s-bars/rep-basic-barbell',
            'Manufacturer': 'REP',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'ROGUE RML-390C Power Rack 3.0',
            'Type': 'RACK',
            'Product': 'Rogue RML-390C Power Rack 3.0',
            'URL': 'https://www.roguefitness.com/rml-390c-power-rack-3-0',
            'Manufacturer': 'ROGUE',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'ID': 'TITAN KG COLOR URETHANE BUMPER PLATES',
            'Type': 'PLATES',
            'Product': 'KG COLOR URETHANE BUMPER PLATES',
            'URL': 'https://www.titan.fitness/strength/weight-plates/bumper-plates/kg-color-urethane-bumper-plates/KGUBUMP_GROUP.html',
            'Manufacturer': 'TITAN',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'ID': 'TITAN FITNESS FLAT WEIGHT BENCH 1,000 LBS. CAPACITY W/ HANDLE & WHEELS',
            'Type': 'BENCH',
            'Product': 'TITAN FITNESS FLAT WEIGHT BENCH 1,000 LBS. CAPACITY W/ HANDLE & WHEELS',
            'URL': 'https://www.titan.fitness/strength/benches/titan-fitness-flat-weight-bench-1000-lbs.-capacity-w-handle-and-wheels/400201.html',
            'Manufacturer': 'TITAN',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'ROGUE Bolt Together Utility Bench',
            'Type': 'BENCH',
            'Product': 'Rogue Bolt Together Utility Bench',
            'URL': 'https://www.roguefitness.com/rogue-bt-bench',
            'Manufacturer': 'ROGUE',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'ROGUE Adjustable Bench 2.0',
            'Type': 'BENCH',
            'Product': 'Rogue Adjustable Bench 2.0',
            'URL': 'https://www.roguefitness.com/rogue-adjustable-bench-2-0',
            'Manufacturer': 'ROGUE',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'ID': 'ROGUE The Ohio Bar - Black Oxide',
            'Product': 'The Ohio Bar - Black Oxide',
            'Type': 'BARBELL',
            'Manufacturer': 'ROGUE',
            'URL': 'https://www.roguefitness.com/rogue-ohio-bar-black-oxide',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'REP PR-1100 HOME GYM POWER RACK',
            'Type': 'RACK',
            'Product': 'REP PR-1100 HOME GYM POWER RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/power-racks/pr-1000-series/rep-pr-1100',
            'Manufacturer': 'REP',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'ROGUE Olympic Plates',
            'Type': 'PLATES',
            'Product': 'Rogue Olympic Plates',
            'URL': 'https://www.roguefitness.com/rogue-olympic-plates',
            'Manufacturer': 'ROGUE',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'True',
            'ID': 'TITAN ECONOMY OLYMPIC BAR – 84-IN',
            'Type': 'BARBELL',
            'Product': 'ECONOMY OLYMPIC BAR – 84-IN',
            'URL': 'https://www.titan.fitness/strength/barbells/olympic/economy-olympic-bar-–-84-in/430085.html',
            'Manufacturer': 'TITAN',
            'LastUpdate': '2021-04-23 5:30:28'
        }
    ]

    dynamodbclient=boto3.resource('dynamodb')
    product = dynamodbclient.Table('Product')
    
    #id = str(random.randint(0,10000000))
    for item in items:
        response = product.put_item(Item=item)
        print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
