import json
import boto3
import random

def lambda_handler(event, context):
    items = [
        {
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
            'Type': 'DUMBELL',
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
            'Type': 'DUMBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rubber-coated-hex-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Rubber Grip Hex Dumbbell Pairs',
            'ID': 'REP Rubber Grip Hex Dumbbell Pairs',
            'Type': 'DUMBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rep-rubber-grip-hex-dumbbells',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Rubber Hex Dumbbell Sets',
            'ID': 'REP Rubber Hex Dumbbell Sets',
            'Type': 'DUMBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rep-rubber-hex-dumbbell-sets',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Urethane Coated Round Dumbbell Pairs',
            'ID': 'REP Urethane Coated Round Dumbbell Pairs',
            'Type': 'DUMBELL',
            'URL': 'https://www.repfitness.com/conditioning/strength-equipment/dumbbells/rep-urethane-coated-round-dumbbell-pairs',
            'LastUpdate': '2021-04-23 5:30:28'
        }, {
            'InStock': 'False',
            'Manufacturer': 'REP',
            'Product': 'REP Urethane Coated Round Dumbbell Sets',
            'ID': 'REP Urethane Coated Round Dumbbell Sets',
            'Type': 'DUMBELL',
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
