from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [
        OP_2DUP, OP_ADD, OP_10, OP_EQUALVERIFY, OP_SUB, OP_4, OP_EQUAL
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0000001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'fee3d451c372fd78ad98e04ce9886f9bc52c28bda31d3133422e8f844fc88940')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
