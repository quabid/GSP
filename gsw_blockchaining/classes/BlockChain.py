import hashlib
import json
from time import time
from .Block import block


class blockchain:
    def __init__(this):
        this.chain = []
        this.pending_transactions = []
        this.new_block(
            previous_hash=
            "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.",
            proof=100)

    def createGenesis(this):
        return block(time.ctime(), "genesisBlock", "00000")

    def new_block(this, proof, previous_hash=None):
        block = {
            'index': len(this.chain) + 1,
            'timestamp': time(),
            'transactions': this.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or this.hash(this.chain[-1])
        }
        this.pending_transactions = []
        this.chain.append(block)

    @property
    def last_block(this):
        return this.chain[-1]

    def new_transaction(this, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        this.pending_transactions.append(transaction)
        return this.last_block['index'] + 1

    def hash(this, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
