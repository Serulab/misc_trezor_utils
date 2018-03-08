

"""
test script to test deleting auth tokens
"""

import time

import boto3
from boto3.dynamodb.conditions import Key, Attr


# TTL in hours
TTL = 1
TTL_SECS = TTL * 60 * 60

# TODO: get time, get a day before and delete them all

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('adrs')

for i, item in enumerate(table.scan()['Items']):
    table.delete_item(Key={
            'crypto': item['crypto'],
            'adr': item['adr']
                }
            )

print('Deleted {0} items'.format(i+1))
