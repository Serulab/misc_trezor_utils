#!/usr/bin/env python3

"""
Generate btc address using Trezor and store them into a list and save it
into a pickle.
"""
from trezorlib.client import TrezorClient
from trezorlib.transport_hid import HidTransport
from trezorlib import messages as proto
from tqdm import tqdm
import pickle

ADRS_TOTAL = 5

devices = HidTransport.enumerate()
# Check whether we found any
if len(devices) == 0:
    print('No TREZOR found')
    sys.exit()
# Use first connected device

transport = devices[0]
# Creates object for manipulating TREZOR
client = TrezorClient(transport)

adrs = []
for i in tqdm(range(1, ADRS_TOTAL+1)):
    bip32_path = client.expand_path("44'/145'/0'/0/{0}".format(i))
    adrs.append(client.get_address('Bcash', bip32_path))
client.close()
print(adrs)
#pickle.dump(adrs, open('BCH.pickle', 'wb'))
