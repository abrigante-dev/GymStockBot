import json
import boto3
import random

def lambda_handler(event, context):
    items = [    
        {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Monster Lite Strap Safety System 2.0',
            'ID': 'ROGUE AU Monster Lite Strap Safety System 2.0',
            'Type': 'ACCESSORY',
            'URL': 'https://www.rogueaustralia.com.au/monster-lite-strap-safety-system-2-0-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Rogue RML-490C Power Rack 3.0',
            'ID': 'ROGUE AU Rogue RML-490C Power Rack 3.0',
            'Type': 'RACK',
            'URL': 'https://www.rogueaustralia.com.au/rogue-rml-490-power-rack-color-3-0-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Pyrros Bar - 28MM - Stainless Steel',
            'ID': 'ROGUE Pyrros Bar - 28MM - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-pyrros-bar-28mm-stainless-steel',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Cerakote Sleeve Barbells',
            'ID': 'ROGUE Cerakote Sleeve Barbells',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/stainless-shaft-cerakote-sleeve-barbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite Double Change Plate Storage',
            'ID': 'ROGUE Monster Lite Double Change Plate Storage',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monsterlite-double-change-plate-storage',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Technique Plates',
            'ID': 'ROGUE Technique Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-technique-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'PowerBlock Dumbbells - Commercial Use',
            'ID': 'ROGUE PowerBlock Dumbbells - Commercial Use',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/powerblocks-commercial-use',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'VersaSpot Dumbbell Spotter System',
            'ID': 'ROGUE VersaSpot Dumbbell Spotter System',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/versaspot-dumbbell-spotter-system-black',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 6-Shooter Olympic Grip Plates',
            'ID': 'ROGUE 6-Shooter Olympic Grip Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-6-shooter-olympic-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 6-Shooter Urethane Olympic Grip Plates',
            'ID': 'ROGUE 6-Shooter Urethane Olympic Grip Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-6-shooter-urethane-olympic-grip-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Black Training KG Plates',
            'ID': 'ROGUE Black Training KG Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-black-training-kg-striped-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Black Training LB Plates',
            'ID': 'ROGUE Black Training LB Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-black-training-lb-color-stripe-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue LB Training 2.0 Plates',
            'ID': 'ROGUE LB Training 2.0 Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-lb-training-2-0-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Calibrated LB Steel Plates',
            'ID': 'ROGUE Calibrated LB Steel Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-calibrated-lb-steel-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Calibrated KG Steel Plates',
            'ID': 'ROGUE Calibrated KG Steel Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-calibrated-kg-steel-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue LB Change Plates',
            'ID': 'ROGUE LB Change Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-lb-change-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue KG Change Plates (IWF)',
            'ID': 'ROGUE KG Change Plates (IWF)',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-kg-change-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue KG Competition Plates (IWF)',
            'ID': 'ROGUE KG Competition Plates (IWF)',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-kg-competition-plates-iwf',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue LB Competition Plates',
            'ID': 'ROGUE LB Competition Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-competition-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Color LB Training 2.0 Plates',
            'ID': 'ROGUE Color LB Training 2.0 Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-color-lb-training-2-0-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue LB Training 2.0 Plates (White Print)',
            'ID': 'ROGUE LB Training 2.0 Plates (White Print)',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-lb-training-2-0-plates-white-print',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Deep Dish Plates',
            'ID': 'ROGUE Deep Dish Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-deep-dish-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Color Echo Bumper Plates',
            'ID': 'ROGUE Color Echo Bumper Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-color-echo-bumper-plate',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Echo Bumper Plates V1',
            'ID': 'ROGUE Echo Bumper Plates V1',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-echo-bumper-plates-with-white-text-v1',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Echo Bumper Plates V2',
            'ID': 'ROGUE Echo Bumper Plates V2',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-echo-bumper-plates-with-white-text',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Fleck Plate',
            'ID': 'ROGUE Fleck Plate',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-fleck-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue LB Fractional Plates',
            'ID': 'ROGUE LB Fractional Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-lb-fractional-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue HG 2.0 Bumper Plates',
            'ID': 'ROGUE HG 2.0 Bumper Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-hg-2-0-bumper-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue HG 2.0 KG Bumper Plates',
            'ID': 'ROGUE HG 2.0 KG Bumper Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/kg-rogue-bumpers',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Bumper Plates by Hi-Temp',
            'ID': 'ROGUE Bumper Plates by Hi-Temp',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-hi-temp-bumper-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Hi-Temp Competition Training Plates',
            'ID': 'ROGUE Hi-Temp Competition Training Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-hi-temp-competition-training-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Machined Olympic Plates',
            'ID': 'ROGUE Machined Olympic Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-machined-olympic-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue US-MIL Spec Bumper',
            'ID': 'ROGUE US-MIL Spec Bumper',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-us-mil-sprc-bumper-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue MIL Spec Echo Bumper',
            'ID': 'ROGUE MIL Spec Echo Bumper',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-mil-echo-bumper-plates-black',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Olympic Plates',
            'ID': 'ROGUE Olympic Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-olympic-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Technique Plates',
            'ID': 'ROGUE Technique Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-technique-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue KG Training 2.0 Plates',
            'ID': 'ROGUE KG Training 2.0 Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-kg-training-2-0-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Urethane Plates',
            'ID': 'ROGUE Urethane Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-urethane-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 12-Sided Urethane Grip Plate',
            'ID': 'ROGUE 12-Sided Urethane Grip Plate',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-12-sided-urethane-grip-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 26 ER Wagon Wheel Pair',
            'ID': 'ROGUE 26 ER Wagon Wheel Pair',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/rogue-26-er-wagon-wheel-pair',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'York Legacy Iron Plates',
            'ID': 'ROGUE York Legacy Iron Plates',
            'Type': 'PLATES',
            'URL': 'https://www.roguefitness.com/york-legacy-iron-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 25MM IWF Olympic Weightlifting Bar - Cerakote',
            'ID': 'ROGUE 25MM IWF Olympic Weightlifting Bar - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-25mm-iwf-oly-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 25MM IWF Olympic Weightlifting Bar - Bright Zinc',
            'ID': 'ROGUE 25MM IWF Olympic Weightlifting Bar - Bright Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-25mm-wmns-oly-bar-dome-cap',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue B-R Bar 2.0',
            'ID': 'ROGUE B-R Bar 2.0',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-29mm-burgener-rippetoe-bar-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue C-70 Bar',
            'ID': 'ROGUE C-70 Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-rogue-c-70-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Castro Bar',
            'ID': 'ROGUE The Castro Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-castro-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Chan Bar - Cerakote',
            'ID': 'ROGUE Chan Bar - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/chan-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Ohio Deadlift Bar - Cerakote',
            'ID': 'ROGUE Ohio Deadlift Bar - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-ohio-deadlift-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Echo Bar 2.0',
            'ID': 'ROGUE Echo Bar 2.0',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-echo-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Freedom Bar - 28.5MM',
            'ID': 'ROGUE Freedom Bar - 28.5MM',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/cerakote-28-5-mm-freedom-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 25MM Freedom Bar',
            'ID': 'ROGUE 25MM Freedom Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-25-mm-freedom-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 28MM IWF Olympic Weightlifting Bar w/ Center Knurl - Bright Zinc',
            'ID': 'ROGUE 28MM IWF Olympic Weightlifting Bar w/ Center Knurl - Bright Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-iwf-olympic-wl-bar-w-center-knurl-bright-zinc',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 28MM IWF Olympic Weightlifting Bar - Cerakote',
            'ID': 'ROGUE 28MM IWF Olympic Weightlifting Bar - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-28mm-iwf-oly-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Ohio Bar - Cerakote',
            'ID': 'ROGUE The Ohio Bar - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-ohio-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Ohio Bar - E-Coat',
            'ID': 'ROGUE The Ohio Bar - E-Coat',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-ohio-bar-2-0-e-coat',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Athlete Cerakote Ohio Bar - Fraser Edition',
            'ID': 'ROGUE Athlete Cerakote Ohio Bar - Fraser Edition',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-athlete-ohio-bar-fraser-cerakote-edition',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Ohio Bar - Black Oxide',
            'ID': 'ROGUE The Ohio Bar - Black Oxide',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-ohio-bar-black-oxide',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Ohio Bar - Stainless Steel',
            'ID': 'ROGUE The Ohio Bar - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/stainless-steel-ohio-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Ohio Bar - Black Zinc',
            'ID': 'ROGUE The Ohio Bar - Black Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-ohio-bar-black-zinc',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 45LB Ohio Power Bar - Cerakote',
            'ID': 'ROGUE 45LB Ohio Power Bar - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-45lb-ohio-powerlift-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 45LB Ohio Power Bar - E-Coat',
            'ID': 'ROGUE 45LB Ohio Power Bar - E-Coat',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-ohio-power-bar-e-coat',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 45LB Ohio Power Bar - Stainless Steel',
            'ID': 'ROGUE 45LB Ohio Power Bar - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-45lb-ohio-power-bar-stainless',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 20KG Ohio Power Bar - Stainless Steel',
            'ID': 'ROGUE 20KG Ohio Power Bar - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-20-kg-ohio-power-bar-stainless-steel',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 45LB Ohio Power Bar - Bare Steel',
            'ID': 'ROGUE 45LB Ohio Power Bar - Bare Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-45lb-ohio-power-bar-bare-steel',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 45LB Ohio Power Bar - Black Zinc',
            'ID': 'ROGUE 45LB Ohio Power Bar - Black Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-45lb-ohio-power-bar-black-zinc',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Operator Bar 3.0',
            'ID': 'ROGUE Operator Bar 3.0',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-operator-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Pyrros Bar - 28MM - Stainless Steel',
            'ID': 'ROGUE Pyrros Bar - 28MM - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-pyrros-bar-28mm-stainless-steel',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Rogue Bar 2.0',
            'ID': 'ROGUE The Rogue Bar 2.0',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-rogue-bar-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 32MM Squat Bar',
            'ID': 'ROGUE 32MM Squat Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-32-mm-squat-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Cerakote Sleeve Barbells',
            'ID': 'ROGUE Cerakote Sleeve Barbells',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/stainless-shaft-cerakote-sleeve-barbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'SB-1 - Rogue Safety Squat Bar',
            'ID': 'ROGUE SB-1 - Rogue Safety Squat Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/sb-1-rogue-safety-squat-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue T-15LB Technique Bar',
            'ID': 'ROGUE T-15LB Technique Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-t-15-lb-technique-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Bella Bar - Cerakote - Tia-Clair Toomey Edition',
            'ID': 'ROGUE The Bella Bar - Cerakote - Tia-Clair Toomey Edition',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-athlete-bella-bar-cerakote-toomey',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 28MM Training Bar - Cerakote',
            'ID': 'ROGUE 28MM Training Bar - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-28mm-training-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 28MM Training Bar - Black Zinc',
            'ID': 'ROGUE 28MM Training Bar - Black Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-28mm-training-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Westside Power Bar 2.0',
            'ID': 'ROGUE Westside Power Bar 2.0',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-westside-power-bar-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 25MM Womens B-R Bar 2.0',
            'ID': 'ROGUE 25MM Womens B-R Bar 2.0',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-25mm-womens-b-r-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Bella Bar 2.0 - Cerakote',
            'ID': 'ROGUE The Bella Bar 2.0 - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-bella-rogue-womens-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Bella Bar 2.0 - E-Coat',
            'ID': 'ROGUE The Bella Bar 2.0 - E-Coat',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-bella-bar-2-0-e-coat',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Bella Bar 2.0 - Stainless Steel',
            'ID': 'ROGUE The Bella Bar 2.0 - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/the-bella-bar-2-0-stainless',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'The Bella Bar 2.0 - Black Zinc',
            'ID': 'ROGUE The Bella Bar 2.0 - Black Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-bella-bar-2-0-black-zinc',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 25MM Boneyard Bars',
            'ID': 'ROGUE 25MM Boneyard Bars',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-25mm-boneyard-bars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Boneyard 28mm Bars',
            'ID': 'ROGUE Boneyard 28mm Bars',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-28mm-boneyard-bars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Boneyard 28.5mm Bars',
            'ID': 'ROGUE Boneyard 28.5mm Bars',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-28-5-mm-boneyard-bars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Boneyard 29mm Bars',
            'ID': 'ROGUE Boneyard 29mm Bars',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-29mm-boneyard-bars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Boneyard Curl Bars',
            'ID': 'ROGUE Boneyard Curl Bars',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-boneyard-curl-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Boneyard Deadlift Bars',
            'ID': 'ROGUE Boneyard Deadlift Bars',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-boneyard-ohio-deadlift-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Boneyard OSO Pro Collars',
            'ID': 'ROGUE Boneyard OSO Pro Collars',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/boneyard-oso-pro-collars-closeout',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Used Barbells',
            'ID': 'ROGUE Used Barbells',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/miscellaneous-barbells-used',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AB-2 Adjustable Bench',
            'ID': 'ROGUE AB-2 Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/ab-2-adjustable-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue AB-3 Adjustable Bench',
            'ID': 'ROGUE AB-3 Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-ab-3-adjustable-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Adjustable Bench 2.0',
            'ID': 'ROGUE Adjustable Bench 2.0',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-adjustable-bench-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Competition Fat Pad',
            'ID': 'ROGUE Competition Fat Pad',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-competition-fat-pad',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Flat Utility Bench 2.0',
            'ID': 'ROGUE Flat Utility Bench 2.0',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-flat-utility-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Fold Up Utility Bench',
            'ID': 'ROGUE Fold Up Utility Bench',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-fold-up-utility-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Utility Bench 2.0',
            'ID': 'ROGUE Monster Utility Bench 2.0',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/monster-utility-bench-2-0-mg-black',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Westside Bench',
            'ID': 'ROGUE Monster Westside Bench',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-monster-westside-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Thompson Fat Pad',
            'ID': 'ROGUE Thompson Fat Pad',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/thompson-fatpad',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Westside Bench 2.0',
            'ID': 'ROGUE Westside Bench 2.0',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-westside-bench-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Echo Squat Stand 2.0',
            'ID': 'ROGUE Echo Squat Stand 2.0',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-echo-squat-stand-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue S-1 Squat Stand 2.0',
            'ID': 'ROGUE S-1 Squat Stand 2.0',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-s-1-squat-stand-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue S-2 Squat Stand 2.0',
            'ID': 'ROGUE S-2 Squat Stand 2.0',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-s2-squat-stand-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue S-4 Squat Stand 2.0',
            'ID': 'ROGUE S-4 Squat Stand 2.0',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-s-4-squat-stand-2',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'SML-2 Rogue 90" Monster Lite Squat Stand',
            'ID': 'ROGUE SML-2 Rogue 90" Monster Lite Squat Stand',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/sml-2-rogue-90-monster-lite-squat-stand',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'SML-3 Rogue 108" Monster Lite Squat Stand',
            'ID': 'ROGUE SML-3 Rogue 108" Monster Lite Squat Stand',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/sml-3-rogue-108-monster-lite-squat-stand',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Combo Rack',
            'ID': 'ROGUE Combo Rack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-combo-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'S-1 to S-2 Conversion Kit',
            'ID': 'ROGUE S-1 to S-2 Conversion Kit',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/s-1-to-s-2-conversion-kit',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'HR-2 Half Rack Conversion Kit',
            'ID': 'ROGUE HR-2 Half Rack Conversion Kit',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/infinity-hr2-half-rack-conversion-kit',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue R-3 Power Rack',
            'ID': 'ROGUE R-3 Power Rack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-r-3-power-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Bolt-Together R-3',
            'ID': 'ROGUE Bolt-Together R-3',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-bolt-together-r-3',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue RM-3 Fortis Rack',
            'ID': 'ROGUE RM-3 Fortis Rack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-rm-3-fortis-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue RM-4 Fortis Rack',
            'ID': 'ROGUE RM-4 Fortis Rack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-rm-4-fortis-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue RML-390C Power Rack 3.0',
            'ID': 'ROGUE RML-390C Power Rack 3.0',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rml-390c-power-rack-3-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'RML-390F Flat Foot Monster Lite Rack',
            'ID': 'ROGUE RML-390F Flat Foot Monster Lite Rack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rml-390f-flat-foot-monster-lite-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite RML-390FULLW Fold Back Wall Mount Power Rack',
            'ID': 'ROGUE Monster Lite RML-390FULLW Fold Back Wall Mount Power Rack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-lite-rml-390-fullw-fold-back-wall-mount-power-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue RML-490 Power Rack',
            'ID': 'ROGUE RML-490 Power Rack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-rml-490-power-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue RML-490C Power Rack 3.0',
            'ID': 'ROGUE RML-490C Power Rack 3.0',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-rml-490-power-rack-color-3-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue RML-690 Power Rack',
            'ID': 'ROGUE RML-690 Power Rack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rml-690-power-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue RML-690C Power Rack 3.0',
            'ID': 'ROGUE RML-690C Power Rack 3.0',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rml-690c-power-rack-3-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Assault AirBike',
            'ID': 'ROGUE Assault AirBike',
            'Type': 'BIKE',
            'URL': 'https://www.roguefitness.com/assault-airbike-and-accessories',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Echo Bike',
            'ID': 'ROGUE Echo Bike',
            'Type': 'BIKE',
            'URL': 'https://www.roguefitness.com/rogue-echo-bike',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Concept 2 BikeErg',
            'ID': 'ROGUE Concept 2 BikeErg',
            'Type': 'BIKE',
            'URL': 'https://www.roguefitness.com/concept2-bike-erg',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Black Concept 2 Model D Rower - PM5',
            'ID': 'ROGUE Black Concept 2 Model D Rower - PM5',
            'Type': 'ROWER',
            'URL': 'https://www.roguefitness.com/black-concept-2-model-d-rower-pm5',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Black Concept 2 Model E Rower - PM5',
            'ID': 'ROGUE Black Concept 2 Model E Rower - PM5',
            'Type': 'ROWER',
            'URL': 'https://www.roguefitness.com/concept2-model-e-rower-pm5-black',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Concept 2 SkiErg',
            'ID': 'ROGUE Concept 2 SkiErg',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/concept-2-skierg-2',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue DB-10 Loadable Dumbbell',
            'ID': 'ROGUE DB-10 Loadable Dumbbell',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/rogue-loadable-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue DB-15 Loadable Dumbbell',
            'ID': 'ROGUE DB-15 Loadable Dumbbell',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/rogue-loadable-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Dumbbell Bumpers',
            'ID': 'ROGUE Dumbbell Bumpers',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/rogue-dumbbell-bumpers',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Dumbbell Sets',
            'ID': 'ROGUE Dumbbell Sets',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/rogue-rubber-hex-dumbbell-sets',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Dumbbells',
            'ID': 'ROGUE Dumbbells',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/rogue-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Urethane Dumbbells',
            'ID': 'ROGUE Urethane Dumbbells',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/rogue-urethane-dumbbells-new',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Thompson Fatbells',
            'ID': 'ROGUE Thompson Fatbells',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/rogue-thompson-fatbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Kettlebells',
            'ID': 'ROGUE Kettlebells',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.roguefitness.com/rogue-kettlebells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Competition Kettlebells',
            'ID': 'ROGUE Competition Kettlebells',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.roguefitness.com/rogue-competition-kettlebells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Kettlebell - E Coat',
            'ID': 'ROGUE Kettlebell - E Coat',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.roguefitness.com/rogue-kettlebell-e-coat',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Rubber Coated Kettlebells',
            'ID': 'ROGUE Rubber Coated Kettlebells',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.roguefitness.com/rogue-rubber-coated-kettlebells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Medicine Balls',
            'ID': 'ROGUE Medicine Balls',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-medicine-balls',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'ONNIT Steel Clubs',
            'ID': 'ROGUE ONNIT Steel Clubs',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/onnit-steel-clubs',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'PowerBlock Dumbbells - Commercial Use',
            'ID': 'ROGUE PowerBlock Dumbbells - Commercial Use',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/powerblocks-commercial-use',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Quick-Lock Dumbbell – 120 lb Add on Kit ',
            'ID': 'ROGUE Quick-Lock Dumbbell – 120 lb Add on Kit ',
            'Type': 'DUMBBELL',
            'URL': 'https://www.ironmaster.com/products/add-on-kit-to-120-lbs-quick-lock/',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Quick-Lock Adjustable Dumbbell System 45 lb Set',
            'ID': 'ROGUE Quick-Lock Adjustable Dumbbell System 45 lb Set',
            'Type': 'DUMBBELL',
            'URL': 'https://www.ironmaster.com/products/quick-lock-dumbbell-system-45-lb-set/',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Quick-Lock Adjustable Dumbbell System 75 lb Set',
            'ID': 'ROGUE Quick-Lock Adjustable Dumbbell System 75 lb Set',
            'Type': 'DUMBBELL',
            'URL': 'https://www.ironmaster.com/products/quick-lock-adjustable-dumbbells-75/',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'H-1 Articulating Handle Kit',
            'ID': 'ROGUE H-1 Articulating Handle Kit',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-ah-1-articulating-handle-kit',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Rack Mount 4-Bar Hanger',
            'ID': 'ROGUE Monster Rack Mount 4-Bar Hanger',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-rack-mount-4-bar-hanger',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Attachment Post',
            'ID': 'ROGUE Monster Attachment Post',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-attachment-post',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Band Peg 2.0 - 4 Pack',
            'ID': 'ROGUE Monster Band Peg 2.0 - 4 Pack',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-band-pegs-2-0-4-pack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Crossmembers',
            'ID': 'ROGUE Monster Crossmembers',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-crossmembers',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Grip Triangle',
            'ID': 'ROGUE Monster Grip Triangle',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-grip-triangle',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster J-Cup Pairs',
            'ID': 'ROGUE Monster J-Cup Pairs',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-j-cup-pairs',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Knurled Knob',
            'ID': 'ROGUE Monster Knurled Knob',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-knurled-knob',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Landmine 2.0',
            'ID': 'ROGUE Monster Landmine 2.0',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-landmine-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lat Pulldown/Low Row (Rack Mounted)',
            'ID': 'ROGUE Monster Lat Pulldown/Low Row (Rack Mounted)',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/lat-pulldown-low-row-rackmounted',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lat Pulldown/Low Row (Stand Alone)',
            'ID': 'ROGUE Monster Lat Pulldown/Low Row (Stand Alone)',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/lat-pulldown-low-row-stand-alone',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Matador',
            'ID': 'ROGUE Monster Matador',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-matador',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Mini Feet',
            'ID': 'ROGUE Monster Mini Feet',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-mini-feet',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Adjustable Monolift - Monster',
            'ID': 'ROGUE Adjustable Monolift - Monster',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-adjustable-monolift-monster',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Plate Storage Channel',
            'ID': 'ROGUE Monster Plate Storage Channel',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-plate-storage-channel',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'SP33100 Plate Storage Pair - Long for 3x3 Monster',
            'ID': 'ROGUE SP33100 Plate Storage Pair - Long for 3x3 Monster',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/sp33100-plate-storage-long-for-3x3-monster',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Rhino Belt Squat - Stand Alone',
            'ID': 'ROGUE Monster Rhino Belt Squat - Stand Alone',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-rhino-belt-squat-stand-alone-mg-black',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Shackle',
            'ID': 'ROGUE Monster Shackle',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-shackle',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Single Post Storage Shelf',
            'ID': 'ROGUE Monster Single Post Storage Shelf',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-single-post-storage-shelf',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Slinger',
            'ID': 'ROGUE Monster Slinger',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-slinger',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Socket Pull-up Bar',
            'ID': 'ROGUE Monster Socket Pull-up Bar',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-socket-pull-up-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Socket Pull-up Curl Bar',
            'ID': 'ROGUE Monster Socket Pull-up Curl Bar',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-socket-pull-up-bar-curl-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Safety Spotter Arms 2.0',
            'ID': 'ROGUE Monster Safety Spotter Arms 2.0',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-safety-spotter-arms-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Plate Storage Pin',
            'ID': 'ROGUE Monster Plate Storage Pin',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/rogue-monster-keyhole-keyless-plate-storage-pin',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Safety Strap System 2.0',
            'ID': 'ROGUE Monster Safety Strap System 2.0',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-monster-safety-strap-2-0-systems',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster 43 Top Beam',
            'ID': 'ROGUE Monster 43 Top Beam',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/monster-43-top-beam',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Utility Seat',
            'ID': 'ROGUE Monster Utility Seat',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-monster-utility-seat',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'XM-43M Monster Multi Grip Crossmember',
            'ID': 'ROGUE XM-43M Monster Multi Grip Crossmember',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/xm-43m-monster-multi-grip-crossmember',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Landmines',
            'ID': 'ROGUE Landmines',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/landmines',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Lite Adjustable Pull-up Bar',
            'ID': 'ROGUE Monster Lite Adjustable Pull-up Bar',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-monster-lite-adjustable-pull-up-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Lite/Infinity Band Pegs - 4 Pack',
            'ID': 'ROGUE Monster Lite/Infinity Band Pegs - 4 Pack',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/extra-set-of-band-pegs',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite Crossmembers',
            'ID': 'ROGUE Monster Lite Crossmembers',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/monster-lite-crossmembers',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite Double Change Plate Storage',
            'ID': 'ROGUE Monster Lite Double Change Plate Storage',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monsterlite-double-change-plate-storage',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite J-Cups',
            'ID': 'ROGUE Monster Lite J-Cups',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/j-3358-monster-lite-j-cups',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Lite Matador',
            'ID': 'ROGUE Monster Lite Matador',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-monster-lite-matador',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Adjustable Monolift - Monster Lite',
            'ID': 'ROGUE Adjustable Monolift - Monster Lite',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-adjustable-monolift-monster-lite',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Infinity/ML Pin and Pipe Safeties',
            'ID': 'ROGUE Infinity/ML Pin and Pipe Safeties',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/infinity-ml-pin-pipe-safeties',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'SP3358 Plate Storage Pair - Long for Monster Lite',
            'ID': 'ROGUE SP3358 Plate Storage Pair - Long for Monster Lite',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/sp3358-plate-storage-long-for-monster-lite',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite Sandwich J-Cup Pair',
            'ID': 'ROGUE Monster Lite Sandwich J-Cup Pair',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/monster-lite-sandwich-j-cup-pair',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Lite Shackle',
            'ID': 'ROGUE Monster Lite Shackle',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-monster-lite-shackle',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite Short Plate Storage Post Pair',
            'ID': 'ROGUE Monster Lite Short Plate Storage Post Pair',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-lite-short-plate-storage-post-pair',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Lite Slinger',
            'ID': 'ROGUE Monster Lite Slinger',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-monster-lite-slinger',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Lite Socket Pull-up Bar',
            'ID': 'ROGUE Monster Lite Socket Pull-up Bar',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-monster-lite-socket-pull-up-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Lite Socket Pull-up Curl Bar',
            'ID': 'ROGUE Monster Lite Socket Pull-up Curl Bar',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/ml-socket-pull-up-bar-curl-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'SAML-24 Monster Lite Safety Spotter Arms (Pair)',
            'ID': 'ROGUE SAML-24 Monster Lite Safety Spotter Arms (Pair)',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/saml-24-monster-lite-spotter-arms-pair',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite Stabilizer Kit',
            'ID': 'ROGUE Monster Lite Stabilizer Kit',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/monster-lite-stabilizer-kit',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite Strap Safety System 2.0',
            'ID': 'ROGUE Monster Lite Strap Safety System 2.0',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/monster-lite-strap-safety-system-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Monster Lite Rack Wall Mount Kit',
            'ID': 'ROGUE Monster Lite Rack Wall Mount Kit',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/monster-lite-rack-wall-mount-kit',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Infinity J-Cup Set',
            'ID': 'ROGUE Infinity J-Cup Set',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/extra-infinity-j-cup-set',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Infinity Matador',
            'ID': 'ROGUE Infinity Matador',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-infinity-matador',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Infinity Safety Spotter Arms',
            'ID': 'ROGUE Infinity Safety Spotter Arms',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/set-of-safety-spotter-arms',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Infinity Strap Safety System 2.0',
            'ID': 'ROGUE Infinity Strap Safety System 2.0',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/infinity-strap-safety-system-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'CB-1 Rogue Camber Bar',
            'ID': 'ROGUE CB-1 Rogue Camber Bar',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/cb-1-rogue-camber-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Curl Bar',
            'ID': 'ROGUE Curl Bar',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-curl-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Curl Bar - Cerakote',
            'ID': 'ROGUE Curl Bar - Cerakote',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-curl-bar-cerakote',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Rackable Curl Bar',
            'ID': 'ROGUE Rackable Curl Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-rackable-curl-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue MG-2 Multi Grip Bars',
            'ID': 'ROGUE MG-2 Multi Grip Bars',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-mg-2-multi-grip-bars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue MG-3 Multi Grip Bar',
            'ID': 'ROGUE MG-3 Multi Grip Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-mg-3-multi-grip-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue TB-1 Trap Bar 2.0',
            'ID': 'ROGUE TB-1 Trap Bar 2.0',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-tb-1-trap-bar-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue TB-2 Trap Bar',
            'ID': 'ROGUE TB-2 Trap Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-tb-2-trap-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Ab Wheel',
            'ID': 'ROGUE Ab Wheel',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/ab-wheel',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Deadlift Bar Jack',
            'ID': 'ROGUE Deadlift Bar Jack',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/bar-jack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Echo Gym Timer',
            'ID': 'ROGUE Echo Gym Timer',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-echo-gym-timer',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Grip Triangle (Standard Grip)',
            'ID': 'ROGUE Grip Triangle (Standard Grip)',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-grip-triangle-standard-grip',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue HG 2.0 Axle Collars',
            'ID': 'ROGUE HG 2.0 Axle Collars',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-hg-axle-collars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Home Timer',
            'ID': 'ROGUE Home Timer',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-home-timer',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Horizontal Plate Rack 2.0',
            'ID': 'ROGUE Horizontal Plate Rack 2.0',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/horizontal-plate-rack-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Landmine Handles',
            'ID': 'ROGUE Landmine Handles',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-landmine-handles',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Post Landmine',
            'ID': 'ROGUE Post Landmine',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/post-landmine',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Loading Pin',
            'ID': 'ROGUE Loading Pin',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-loading-pin',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue LP-2 Lat Pulldown / Low Row',
            'ID': 'ROGUE LP-2 Lat Pulldown / Low Row',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-lp-2-lat-pulldown-low-row',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Mini Deadlift Bar Jack',
            'ID': 'ROGUE Mini Deadlift Bar Jack',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/mini-deadlift-bar-jack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'OSO Barbell Collars',
            'ID': 'ROGUE OSO Barbell Collars',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/oso-barbell-collars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue P-4 Pull-up System',
            'ID': 'ROGUE P-4 Pull-up System',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/p4-pullup-system',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Parallel Landmine Handle',
            'ID': 'ROGUE Parallel Landmine Handle',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-parallel-landmine-handle',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'York Olympic A-Frame Plate Tree',
            'ID': 'ROGUE York Olympic A-Frame Plate Tree',
            'Type': 'RACK',
            'URL': 'https://www.roguefitness.com/york-olympic-a-frame-plate-tree',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Rig Mount Speed Bag Platforms',
            'ID': 'ROGUE Rig Mount Speed Bag Platforms',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-rig-mount-speed-bag-platforms',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Squat Stand Base Storage - Pair',
            'ID': 'ROGUE Squat Stand Base Storage - Pair',
            'Type': 'BENCH',
            'URL': 'https://www.roguefitness.com/rogue-squat-stand-base-storage-pair',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Stainless Lat Bar',
            'ID': 'ROGUE Stainless Lat Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-stainless-steel-lat-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue T Bar Row',
            'ID': 'ROGUE T Bar Row',
            'Type': 'BARBELL',
            'URL': 'https://www.roguefitness.com/rogue-t-bar-row',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Tricep Push Down Attachment',
            'ID': 'ROGUE Tricep Push Down Attachment',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-tricep-pushdown-attachment',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue LT-1 Trolley and Lever Arm Kit',
            'ID': 'ROGUE LT-1 Trolley and Lever Arm Kit',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-lt-1-50-cal-trolley-lever-arms-kit',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue USA Aluminum Collars',
            'ID': 'ROGUE USA Aluminum Collars',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-usa-aluminum-collars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'VersaSpot Dumbbell Spotter System',
            'ID': 'ROGUE VersaSpot Dumbbell Spotter System',
            'Type': 'DUMBBELL',
            'URL': 'https://www.roguefitness.com/versaspot-dumbbell-spotter-system-black',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Westside Scout Hyper',
            'ID': 'ROGUE Westside Scout Hyper',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/westside-scout-hyper',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Abram GHD 2.0',
            'ID': 'ROGUE Abram GHD 2.0',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-abram-glute-ham-developer-2-0',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Deadlift Platform',
            'ID': 'ROGUE Deadlift Platform',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-deadlift-platform',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue 3x3 Echo GHD',
            'ID': 'ROGUE 3x3 Echo GHD',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-echo-ghd',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue Monster Swing Arm GHD',
            'ID': 'ROGUE Monster Swing Arm GHD',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-monster-swing-arm-ghd',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Y-1 Rogue Yoke',
            'ID': 'ROGUE Y-1 Rogue Yoke',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/rogue-yoke',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Y-2 Rogue Yoke',
            'ID': 'ROGUE Y-2 Rogue Yoke',
            'Type': 'ACCESSORY',
            'URL': 'https://www.roguefitness.com/y2-yoke',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK The Bella Bar 2.0 - Black Zinc',
            'ID': 'ROGUE UK The Bella Bar 2.0 - Black Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.rogueeurope.eu/rogue-bella-bar-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK AB-2 Adjustable Bench',
            'ID': 'ROGUE UK AB-2 Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.rogueeurope.eu/ab-2-adjustable-bench-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue KG Dumbbells',
            'ID': 'ROGUE UK Rogue KG Dumbbells',
            'Type': 'DUMBBELL',
            'URL': 'https://www.rogueeurope.eu/rogue-kg-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue Echo Bumper Plates V2',
            'ID': 'ROGUE UK Rogue Echo Bumper Plates V2',
            'Type': 'PLATES',
            'URL': 'https://www.rogueeurope.eu/rogue-echo-bumper-plates-with-white-text-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue Color Echo Bumper Plates',
            'ID': 'ROGUE UK Rogue Color Echo Bumper Plates',
            'Type': 'PLATES',
            'URL': 'https://www.rogueeurope.eu/rogue-color-echo-bumper-plate-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue Home Timer',
            'ID': 'ROGUE UK Rogue Home Timer',
            'Type': 'ACCESSORY',
            'URL': 'https://www.rogueeurope.eu/rogue-home-timer-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue Kettlebells',
            'ID': 'ROGUE UK Rogue Kettlebells',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.rogueeurope.eu/rogue-kettlebells-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue 20KG Ohio Power Bar - Stainless Steel',
            'ID': 'ROGUE UK Rogue 20KG Ohio Power Bar - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.rogueeurope.eu/rogue-20-kg-ohio-power-bar-stainless-steel-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue 20KG Ohio Power Bar - Black Zinc',
            'ID': 'ROGUE UK Rogue 20KG Ohio Power Bar - Black Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.rogueeurope.eu/rogue-20-kg-ohio-power-bar-black-zinc-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'Rogue P-4 Pull-up System',
            'ID': 'ROGUE P-4 Pull-up System',
            'Type': 'ACCESSORY',
            'URL': 'https://www.rogueeurope.eu/rogue-p-4-pull-up-system',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue Vertical Plate Tree 2.0',
            'ID': 'ROGUE UK Rogue Vertical Plate Tree 2.0',
            'Type': 'RACK',
            'URL': 'https://www.rogueeurope.eu/rogue-vertical-plate-tree-2-0-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'UK Rogue RR Plates',
            'ID': 'ROGUE UK Rogue RR Plates',
            'Type': 'PLATES',
            'URL': 'https://www.rogueeurope.eu/rogue-rr-bumper-plates-eu',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Rogue 20KG Ohio Power Bar - Stainless Steel',
            'ID': 'ROGUE AU Rogue 20KG Ohio Power Bar - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.rogueaustralia.com.au/rogue-20-kg-ohio-power-bar-stainless-steel-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Rogue 20KG Ohio Power Bar - Black Zinc',
            'ID': 'ROGUE AU Rogue 20KG Ohio Power Bar - Black Zinc',
            'Type': 'BARBELL',
            'URL': 'https://www.rogueaustralia.com.au/rogue-20-kg-ohio-power-bar-black-zinc-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU AB-2 Adjustable Bench',
            'ID': 'ROGUE AU AB-2 Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.rogueaustralia.com.au/ab-2-adjustable-bench-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Rogue Curl Bar',
            'ID': 'ROGUE AU Rogue Curl Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.rogueaustralia.com.au/rogue-curl-bar-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU SAML-24 Monster Lite Safety Spotter Arms (Pair)',
            'ID': 'ROGUE AU SAML-24 Monster Lite Safety Spotter Arms (Pair)',
            'Type': 'ACCESSORY',
            'URL': 'https://www.rogueaustralia.com.au/saml-24-monster-lite-spotter-arms-pair-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Monster Lite Strap Safety System 2.0',
            'ID': 'ROGUE AU Monster Lite Strap Safety System 2.0',
            'Type': 'ACCESSORY',
            'URL': 'https://www.rogueaustralia.com.au/monster-lite-strap-safety-system-2-0-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Black Concept 2 Model D Rower - PM5',
            'ID': 'ROGUE AU Black Concept 2 Model D Rower - PM5',
            'Type': 'ROWER',
            'URL': 'https://www.rogueaustralia.com.au/black-concept-2-model-d-rower-pm5-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Rogue Calibrated KG Steel Plates',
            'ID': 'ROGUE AU Rogue Calibrated KG Steel Plates',
            'Type': 'PLATES',
            'URL': 'https://www.rogueaustralia.com.au/rogue-calibrated-kg-steel-plates-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Rogue Color Echo Bumper Plates',
            'ID': 'ROGUE AU Rogue Color Echo Bumper Plates',
            'Type': 'PLATES',
            'URL': 'https://www.rogueaustralia.com.au/rogue-color-echo-bumper-plate-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU RML-390F Flat Foot Monster Lite Rack',
            'ID': 'ROGUE AU RML-390F Flat Foot Monster Lite Rack',
            'Type': 'RACK',
            'URL': 'https://www.rogueaustralia.com.au/rml-390f-flat-foot-monster-lite-rack-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU Rogue RML-490C Power Rack 3.0',
            'ID': 'ROGUE AU Rogue RML-490C Power Rack 3.0',
            'Type': 'RACK',
            'URL': 'https://www.rogueaustralia.com.au/rogue-rml-490-power-rack-color-3-0-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'ROGUE',
            'Product': 'AU SML-1 Rogue 70" Monster Lite Squat Stand',
            'ID': 'ROGUE AU SML-1 Rogue 70" Monster Lite Squat Stand',
            'Type': 'BENCH',
            'URL': 'https://www.rogueaustralia.com.au/sml-1-rogue-70-monster-lite-squat-stand-au',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Basic Barbell',
            'ID': 'REP Basic Barbell',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/rep-basic-barbell',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Excalibur Bar',
            'ID': 'REP Excalibur Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/bars-plates/excalibur-olympic-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Excalibur 20 kg - Stainless Steel',
            'ID': 'REP Excalibur 20 kg - Stainless Steel',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/excalibur-20-kg-stainless-steel',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP EZ Curl Barbell',
            'ID': 'REP EZ Curl Barbell',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/rep-ez-curl-barbell',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Rackable EZ Curl Barbell',
            'ID': 'REP Rackable EZ Curl Barbell',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/bars-plates/rep-rackable-ez-curl-barbell',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Gladiator WL Bearing Bar',
            'ID': 'REP Gladiator WL Bearing Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/bars-plates/olympic-bars/20kg-men-s-bars/rep-gladiator-olympic-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Stainless Steel Power Bar v2',
            'ID': 'REP Stainless Steel Power Bar v2',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/rep-stainless-steel-power-bar',
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
            'Manufacturer': 'REP',
            'Product': 'REP Deep Knurl Power Bar EX',
            'ID': 'REP Deep Knurl Power Bar EX',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/rep-deep-knurl-power-bar-ex',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Sabre Bar',
            'ID': 'REP Sabre Bar',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/bars-plates/olympic-bars/rep-sabre-bar',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Black Sabre Barbell',
            'ID': 'REP Black Sabre Barbell',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/rep-black-sabre-barbell',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP V2 Sleeve Battle Rope',
            'ID': 'REP V2 Sleeve Battle Rope',
            'Type': 'ROPE',
            'URL': 'https://www.repfitness.com/rep-v2-battle-rope-slv',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Battle Rope Strap Anchor',
            'ID': 'REP Battle Rope Strap Anchor',
            'Type': 'ROPE',
            'URL': 'https://www.repfitness.com/bodyweight-gymnastics/ropes/battling-ropes/rep-battle-rope-strap-anchor',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Battle Rope Wall Mount Anchor',
            'ID': 'REP Battle Rope Wall Mount Anchor',
            'Type': 'ROPE',
            'URL': 'https://www.repfitness.com/rep-battle-rope-wall-mount-attachment',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'AB-3000 FID Adjustable Bench',
            'ID': 'REP AB-3000 FID Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/rep-ab3000-fid-adj-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'AB-3100 Adjustable Bench',
            'ID': 'REP AB-3100 Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/strength-equipment/strength-training/benches/rep-ab-3100-fi-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'AB-5000 ZERO GAP Adjustable Bench',
            'ID': 'REP AB-5000 ZERO GAP Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/strength-equipment/strength-training/benches/rep-ab-5000',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'AB-5100 Adjustable Bench',
            'ID': 'REP AB-5100 Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/strength-equipment/strength-training/benches/rep-ab-5100',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP AB-5200 Adjustable Bench',
            'ID': 'REP AB-5200 Adjustable Bench',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/strength-equipment/strength-training/benches/ab-5200-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'AB-5000/5100 Leg Attachment',
            'ID': 'REP AB-5000/5100 Leg Attachment',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/strength-equipment/strength-training/benches/ab-5000-5100-leg-attachment',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'FB-3000 Flat Bench',
            'ID': 'REP FB-3000 Flat Bench',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/rep-flat-bench-with-storage',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'FB-4000 Comp Lite Bench',
            'ID': 'REP FB-4000 Comp Lite Bench',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/rep-fb-4000-comp-lite-bench-2396',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'FB-5000 Competition Flat Bench',
            'ID': 'REP FB-5000 Competition Flat Bench',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/rep-fb-5000-competition-flat-bench',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'FB-5000 with Wide Pad',
            'ID': 'REP FB-5000 with Wide Pad',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/strength-equipment/strength-training/benches/rep-competition-bench-with-wide-pad',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Wide Pad',
            'ID': 'REP Wide Pad',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/rep-wide-pad',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'Concept2 Indoor Rower',
            'ID': 'REP Concept2 Indoor Rower',
            'Type': 'ROWER',
            'URL': 'https://www.repfitness.com/concept-2-model-d-e-rower',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Adjustable Dumbbells',
            'ID': 'REP Adjustable Dumbbells',
            'Type': 'DUMBBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rep-adjustable-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Dumbbell Rack',
            'ID': 'REP Dumbbell Rack',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/bars-plates/storage/dumbbell-storage/rep-dumbbell-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'Victory 2-Tier Dumbbell Rack',
            'ID': 'REP Victory 2-Tier Dumbbell Rack',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/2-tier-commercial-dumbbell-rack-2826',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Rubber Coated Hex Dumbbell Pairs',
            'ID': 'REP Rubber Coated Hex Dumbbell Pairs',
            'Type': 'DUMBBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rubber-coated-hex-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Rubber Grip Hex Dumbbell Pairs',
            'ID': 'REP Rubber Grip Hex Dumbbell Pairs',
            'Type': 'DUMBBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rep-rubber-grip-hex-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Rubber Hex Dumbbell Sets',
            'ID': 'REP Rubber Hex Dumbbell Sets',
            'Type': 'DUMBBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rep-rubber-hex-dumbbell-sets',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Urethane Coated Round Dumbbell Pairs',
            'ID': 'REP Urethane Coated Round Dumbbell Pairs',
            'Type': 'DUMBBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rep-urethane-coated-round-dumbbell-pairs',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Urethane Coated Round Dumbbell Sets',
            'ID': 'REP Urethane Coated Round Dumbbell Sets',
            'Type': 'DUMBBELL',
            'URL': 'https://www.repfitness.com/rep-urethane-coated-round-dumbbell-sets',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP FT-3000 Compact Functional Trainer',
            'ID': 'REP FT-3000 Compact Functional Trainer',
            'Type': 'TRAINER',
            'URL': 'https://www.repfitness.com/compact-functional-trainer-2446',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP FT-5000 Functional Trainer',
            'ID': 'REP FT-5000 Functional Trainer',
            'Type': 'TRAINER',
            'URL': 'https://www.repfitness.com/strength-equipment/commercial-equipment/rep-multi-grip-functional-trainer',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP GHD - Glute Ham Developer',
            'ID': 'REP GHD - Glute Ham Developer',
            'Type': 'BENCH',
            'URL': 'https://www.repfitness.com/rep-ghd',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'Gym Chalk 1 lb (8-2 oz Blocks)',
            'ID': 'REP Gym Chalk 1 lb (8-2 oz Blocks)',
            'URL': 'https://www.repfitness.com/gym-chalk-1-lb-8-2-oz-blocks',
            'Type': 'ACCESSORY',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Wood Gymnastic Rings',
            'ID': 'REP Wood Gymnastic Rings',
            'Type': 'ROPE',
            'URL': 'https://www.repfitness.com/rep-wood-gymnastic-rings',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Kettlebells',
            'ID': 'REP Kettlebells',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/kettlebells/rep-kettlebells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Adjustable KBs',
            'ID': 'REP Adjustable KBs',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/kettlebells/adjustable-kettlebell',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP LB Kettlebells',
            'ID': 'REP LB Kettlebells',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.repfitness.com/rep-kettlebells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'Kettlebell Storage Rack',
            'ID': 'REP Kettlebell Storage Rack',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/rep-kettlebell-storage-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'Free Standing Landmine',
            'ID': 'REP Free Standing Landmine',
            'Type': 'BARBELL',
            'URL': 'https://www.repfitness.com/free-standing-landmine',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'Landmine attachment for Power Racks',
            'ID': 'REP Landmine attachment for Power Racks',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/rack-attachments/1000-series-attachments/power-rack-landmine',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Modular Storage System',
            'ID': 'REP Modular Storage System',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/bars-plates/storage/dumbbell-storage/rep-modular-storage-system',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Black Bumper Plates',
            'ID': 'REP Black Bumper Plates',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/bars-plates/olympic-plates/rep-black-bumper-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Color Bumper Plates',
            'ID': 'REP Color Bumper Plates',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/bars-plates/olympic-plates/rep-color-bumper-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Weight Set - Color Bumpers',
            'ID': 'REP Weight Set - Color Bumpers',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/rep-weight-set-color-bumpers',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP kg Change Plates',
            'ID': 'REP kg Change Plates',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/bars-plates/rep-kg-change-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP LB Change Plates',
            'ID': 'REP LB Change Plates',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/rep-lb-change-plates-2503',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP LB Fractional Change Plates',
            'ID': 'REP LB Fractional Change Plates',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/rep-lb-change-plates-2503',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Competition Bumper Plates (LB)',
            'ID': 'REP Competition Bumper Plates (LB)',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/rep-competition-bumper-plates-lb',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Competition Bumper Plates (KG)',
            'ID': 'REP Competition Bumper Plates (KG)',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/bars-plates/olympic-plates/rep-competition-bumper-plates-kg',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Equalizer Iron Olympic Plates',
            'ID': 'REP Equalizer Iron Olympic Plates',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/bars-plates/rep-equalizer-iron-olympic-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Iron Plates',
            'ID': 'REP Iron Plates',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/rep-iron-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP V2 Rubber Coated Olympic Plates',
            'ID': 'REP V2 Rubber Coated Olympic Plates',
            'Type': 'PLATES',
            'URL': 'https://www.repfitness.com/rep-rubber-coated-olympic-plates',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP 3-in-1 Soft Plyo Boxes',
            'ID': 'REP 3-in-1 Soft Plyo Boxes',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/rep-3-in-1-soft-plyo-boxes',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Street Parking 3-in-1 Soft Plyo Boxes',
            'ID': 'REP Street Parking 3-in-1 Soft Plyo Boxes',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/rep-street-parking-3-in-1-soft-plyo-boxes',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Pull-Up Bands',
            'ID': 'REP Pull-Up Bands',
            'Type': 'ROPE',
            'URL': 'https://www.repfitness.com/rep-pull-up-bands',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'J-Cups for 1000 Series Racks',
            'ID': 'REP J-Cups for 1000 Series Racks',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/rack-attachments/1000-series-attachments/econ-power-rack-j-cups',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'Weight Horns for 1000 Series Power Racks',
            'ID': 'REP Weight Horns for 1000 Series Power Racks',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/weight-horns-for-1000-series',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP ISO Arms',
            'ID': 'REP ISO Arms',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/rack-attachments/rep-iso-arms-2020',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Lat and Row Attachment for PR-1000 and PR-1100',
            'ID': 'REP Lat and Row Attachment for PR-1000 and PR-1100',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/rep-lat-pull-down-low-row-attachment',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP PR-1050 Short Home Gym Power Rack',
            'ID': 'REP PR-1050 Short Home Gym Power Rack',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/power-racks/rep-pr-1050',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP PR-1100 Home Gym Power Rack',
            'ID': 'REP PR-1100 Home Gym Power Rack',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/power-racks/rep-pr-1100',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP PR-4000 Power Rack',
            'ID': 'REP PR-4000 Power Rack',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/power-racks/pr-4000-power-rack',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Dip Attachment',
            'ID': 'REP PR-4000 Dip Attachment',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-4000-dip',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Front Foot Extension Pair',
            'ID': 'REP PR-4000 Front Foot Extension Pair',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-4000-front-extension',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Flat Sandwich J-cups',
            'ID': 'REP PR-4000 Flat Sandwich J-cups',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-4000-flat-sandwich-jcup',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Round Sandwich J-Cups',
            'ID': 'REP PR-4000 Round Sandwich J-cups',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-4000-round-sandwich-jcup',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {        
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Standard J-cups',
            'ID': 'REP PR-4000 Standard J-cups',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/strength-equipment/rack-attachments/pr-4000-attachments/pr-4000-standard-jcup',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Landmine Attachment',
            'ID': 'REP PR-4000 Landmine Attachment',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-4000-landmine',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Leg Roller Attachment',
            'ID': 'REP PR-4000 Leg Roller Attachment',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-4000-leg-roller',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP PR-4000 Lat/Low Row Attachment',
            'ID': 'REP PR-4000 Lat/Low Row Attachment',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/rep-pr-4000-lat-low-row-attachment',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Spotter Arms',
            'ID': 'REP PR-4000 Spotter Arms',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-4000-spotter-arms',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Rear Base Stabilizer',
            'ID': 'REP PR-4000 Rear Base Stabilizer',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/rack-attachments/pr-4000-attachments/rear-base-stabilizer',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-4000 Weight Horn - 6&quot; Pair',
            'ID': 'REP PR-4000 Weight Horn Pair',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-4000-weighthorn-6',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP PR-5000 V2 Power Rack',
            'ID': 'REP PR-5000 V2 Power Rack',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/strength-equipment/power-racks/pr-5000-v2',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-5000 Crossmembers',
            'ID': 'REP PR-5000 Crossmembers',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/catalog/product/view/id/5151/s/pr-5000-crossmembers/',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-5000 V2 Dip Attachment',
            'ID': 'REP PR-5000 V2 Dip Attachment',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-5000-dip-attachment-v2',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-5000 V2 Pull-up Bar',
            'ID': 'REP PR-5000 V2 Pull-up Bar',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-5000-v2-pull-up-bars',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP PR-5000 Lat/Low Row Attachment',
            'ID': 'REP PR-5000 Lat/Low Row Attachment',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/rep-pr-5000-v2-lat-low-row-attachment',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-5000 V2 Spotter Arms - Pair',
            'ID': 'REP PR-5000 V2 Spotter Arms - Pair',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/pr-5000-spotter-arms-pair-v2',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR-5000 V2 Rear Base Stabilizer',
            'ID': 'REP PR-5000 V2 Rear Base Stabilizer',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/strength-equipment/rear-base-stabilizer-v2',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'PR5000 Uprights',
            'ID': 'REP PR5000 Uprights',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/catalog/product/view/id/5154/s/pr-4000-uprights/',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP SR-4000',
            'ID': 'REP SR-4000',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/rep-squat-rack-4000-series',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP V2 Sandbags',
            'ID': 'REP V2 Sandbags',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/rep-sandbags',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP 4-Post Push Sled',
            'ID': 'REP 4-Post Push Sled',
            'Type': 'ACCESSORY',
            'URL': 'https://www.repfitness.com/rep-4-post-push-sled',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Bar and Bumper Plate Tree',
            'ID': 'REP Bar and Bumper Plate Tree',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/bar-and-bumper-plate-tree',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP V2 Slam Balls',
            'ID': 'REP V2 Slam Balls',
            'Type': 'KETTLEBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/slam-balls/rep-v2-slam-balls',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Wall Mounted Gym Storage Rack',
            'ID': 'REP Wall Mounted Gym Storage Rack',
            'Type': 'RACK',
            'URL': 'https://www.repfitness.com/rep-wall-mounted-gym-storage-rack',
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
