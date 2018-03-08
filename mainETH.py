#!/usr/bin/env python3

"""
Generate ltc address using Trezor and store them into a list and save it
into a pickle.
"""
from trezorlib.client import TrezorClient
from trezorlib.transport_hid import HidTransport
from trezorlib import messages as proto
from tqdm import tqdm
import hashlib
import pickle
import binascii
import sys
from subprocess import Popen,PIPE


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

adrs = []
for i in tqdm(range(ADRS_TOTAL)):
    bip32_path = client.expand_path("44'/60'/0'/0/{0}".format(i))
    adr = client.ethereum_get_address(bip32_path)
    adr_ascii = binascii.b2a_hex(adr)
    call = ['node', 'eth.js', adr_ascii]
    p = Popen(call, stdout=PIPE,stderr=PIPE)
    out, err = p.communicate()
    adrs.append(out[:-1].decode())
client.close()

pickle.dump(adrs, open('ETH.pickle', 'wb'))

# trezorctl ethereum_get_address -n "m/44'/60'/0'/0/0"
