import json
import boto3
import random

def lambda_handler(event, context):
    # TODO implement
    items = [{'STOCK': True, 'ID': '8552214', 'TYPE': 'RACK', 'NAME': 'T-2 SERIES POWER RACK', 'URL': 'https://www.titan.fitness/racks/power-racks/t-2-series/t-2-series-power-rack/T2-SERIES-RACK.html', 'COMPANY': 'TITAN'}, {'STOCK': False, 'ID': '1691831', 'NAME': 'Rogue Euro 28MM Olympic Weightlifting Bar', 'TYPE': 'BARBELL', 'COMPANY': 'ROGUE', 'URL': 'https://www.roguefitness.com/28-mm-rogue-eu-oly-wl-bar-with-center-knurl-rogue-hg-clear-shaft-chrome-sleeve'}, {'STOCK': False, 'ID': '5750784', 'TYPE': 'PLATES', 'NAME': 'REP IRON PLATES', 'URL': 'https://www.repfitness.com/bars-plates/olympic-plates/iron-plates/rep-iron-plates', 'COMPANY': 'REP'}, {'STOCK': True, 'ID': '3118473', 'TYPE': 'PLATES', 'NAME': 'Rogue HG 2.0 Bumper Plates', 'URL': 'https://www.roguefitness.com/rogue-hg-2-0-bumper-plates', 'COMPANY': 'ROGUE'}, {'STOCK': True, 'ID': '7192274', 'TYPE': 'BARBELL', 'NAME': 'The Ohio Bar - Cerakote', 'URL': 'https://www.roguefitness.com/the-ohio-bar-cerakote', 'COMPANY': 'ROGUE'}, {'STOCK': True, 'ID': '8034030', 'TYPE': 'RACK', 'NAME': 'Rogue SML-2C Squat Stand', 'URL': 'https://www.roguefitness.com/rogue-sml-2c-squat-stand', 'COMPANY': 'ROGUE'}, {'STOCK': True, 'ID': '7892058', 'TYPE': 'BENCH', 'NAME': 'Rogue Flat Utility Bench 2.0', 'URL': 'https://www.roguefitness.com/rogue-flat-utility-bench', 'COMPANY': 'ROGUE'}, {'STOCK': True, 'ID': '8014514', 'TYPE': 'BENCH', 'NAME': 'REP FB-3000 FLAT BENCH', 'URL': 'https://www.repfitness.com/strength-equipment/strength-training/benches/rep-flat-bench-with-storage', 'COMPANY': 'REP'}, {'STOCK': False, 'ID': '9899156', 'TYPE': 'BARBELL', 'NAME': 'REP BASIC BARBELL', 'URL': 'https://www.repfitness.com/bars-plates/olympic-bars/20kg-men-s-bars/rep-basic-barbell', 'COMPANY': 'REP'}, {'STOCK': True, 'ID': '8205442', 'TYPE': 'RACK', 'NAME': 'Rogue RML-390C Power Rack 3.0', 'URL': 'https://www.roguefitness.com/rml-390c-power-rack-3-0', 'COMPANY': 'ROGUE'}, {'STOCK': False, 'ID': '1047248', 'TYPE': 'PLATES', 'NAME': 'KG COLOR URETHANE BUMPER PLATES', 'URL': 'https://www.titan.fitness/strength/weight-plates/bumper-plates/kg-color-urethane-bumper-plates/KGUBUMP_GROUP.html', 'COMPANY': 'TITAN'}, {'STOCK': False, 'ID': '3361280', 'TYPE': 'BENCH', 'NAME': 'TITAN FITNESS FLAT WEIGHT BENCH 1,000 LBS. CAPACITY W/ HANDLE & WHEELS', 'URL': 'https://www.titan.fitness/strength/benches/titan-fitness-flat-weight-bench-1000-lbs.-capacity-w-handle-and-wheels/400201.html', 'COMPANY': 'TITAN'}, {'STOCK': True, 'ID': '8903903', 'TYPE': 'BENCH', 'NAME': 'Rogue Bolt Together Utility Bench', 'URL': 'https://www.roguefitness.com/rogue-bt-bench', 'COMPANY': 'ROGUE'}, {'STOCK': True, 'ID': '9885190', 'TYPE': 'BENCH', 'NAME': 'Rogue Adjustable Bench 2.0', 'URL': 'https://www.roguefitness.com/rogue-adjustable-bench-2-0', 'COMPANY': 'ROGUE'}, {'STOCK': False, 'ID': '8530129', 'NAME': 'The Ohio Bar - Black Oxide', 'TYPE': 'BARBELL', 'COMPANY': 'ROGUE', 'URL': 'https://www.roguefitness.com/rogue-ohio-bar-black-oxide'}, {'STOCK': True, 'ID': '5889156', 'TYPE': 'RACK', 'NAME': 'REP PR-1100 HOME GYM POWER RACK', 'URL': 'https://www.repfitness.com/strength-equipment/power-racks/pr-1000-series/rep-pr-1100', 'COMPANY': 'REP'}, {'STOCK': True, 'ID': '4117809', 'TYPE': 'PLATES', 'NAME': 'Rogue Olympic Plates', 'URL': 'https://www.roguefitness.com/rogue-olympic-plates', 'COMPANY': 'ROGUE'}, {'STOCK': True, 'ID': '7174345', 'TYPE': 'BARBELL', 'NAME': 'ECONOMY OLYMPIC BAR – 84-IN', 'URL': 'https://www.titan.fitness/strength/barbells/olympic/economy-olympic-bar-–-84-in/430085.html', 'COMPANY': 'TITAN'}]
    dynamodbclient=boto3.resource('dynamodb')
    sample_table = dynamodbclient.Table('stock-items')
    
    id = str(random.randint(0,10000000))
    for item in items:
        sample_table.put_item(
                            Item={
                                'ID' : item['ID'],
                                'COMPANY' : item['COMPANY'],
                                'NAME' : item['NAME'],
                                'TYPE' : item['TYPE'],
                                'URL' : item['URL'],
                                'STOCK' : item['STOCK']
                            }
                        )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
