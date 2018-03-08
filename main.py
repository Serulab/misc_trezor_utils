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

ADRS_TOTAL = 5000

devices = HidTransport.enumerate()
# Check whether we found any
if len(devices) == 0:
    print('No TREZOR found')
    sys.exit()
# Use first connected device

transport = devices[0]
# Creates object for manipulating TREZOR
client = TrezorClient(transport)

# Print out TREZOR's features and settings
#print(client.features)


adrs = []
for i in tqdm(range(ADRS_TOTAL)):
    bip32_path = client.expand_path("49'/0'/0'/0/{0}".format(i))
    adrs.append(client.get_address('Bitcoin', bip32_path, script_type=proto.InputScriptType.SPENDP2SHWITNESS))
client.close()
#print(adrs)
pickle.dump(adrs, open('BTC.pickle', 'wb'))

# SPENDWITNESS
# SPENDP2SHWITNESS

# (trezorfeb) sbassi@Us-IT00354:~/projects/takocoin/takomisc/trezorfeb$ trezorctl get_address --coin Bitcoin --script-type segwit --address "m/49'/0'/0'/0/0"
# bc1qrwl055767s26920eq7tfpaa4m97m302cnkh6w4
#
