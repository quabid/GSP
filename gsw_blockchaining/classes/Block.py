from hashlib import sha256
import time

class block:
    def __init__(this, timestamp, data, previousHash=' '):
        this.timestamp = timestamp
        this.data = data
        this.previousHash = previousHash
        this.hash =  # TODO function calculateHash()

    def calculateHash(this):
        return sha256((str(this.timestamp) + str(this.data) + str(this.previousHash).encode()).hexdigest())
