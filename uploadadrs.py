

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Grabs all content from csv file upload it to dynamoDB table adrs
"""

import csv
import pickle
import boto3
from tqdm import tqdm

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('adrs')

def upload2dynamo(filename, crypto):
    with open(filename, 'rb') as f:
        ards_list = pickle.load(f)

    with table.batch_writer() as batch:
        for adr in tqdm(ards_list):
            batch.put_item(
                Item={
                    'adr': adr,
                    'crypto': crypto,
                }
            )

upload2dynamo('BCH.pickle', 'BCH')
upload2dynamo('ETH.pickle', 'ETH')
upload2dynamo('BTC.pickle', 'BTC')
upload2dynamo('LTC.pickle', 'LTC')
