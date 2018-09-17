import hashlib as hl
import datetime as date
from flask import Flask
from flask import request
node = Flask(__name__)
############################
##START OF BLOCKCHAIN CODE##
############################

#this is the blockchain code portion
class Block:
    def __init__(self, index, timeStamp, data, previousHash):
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hl.sha384()
        sha.update(str(self.index) +
               str(self.timeStamp) +
               str(self.data) +
               str(self.previousHash))
        return sha.hexdigest()

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Your current clout block is " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
def create20Blocks():
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print "Block #{} has been added to the blockchain!".format(block_to_add.index)
        print "Hash: {}\n".format(block_to_add.hash)
#######################
##END BLOCKCHAIN CODE##
#######################



this_nodes_transaction = []

@node.route('/txion', methods=['POST'])
def transaction():
    if(request.method== "POST"):
        newTXion = request.get_json()
        this_nodes_transaction.append(newTXion)
        print "New transaction"
        print "FROM: {}".format(newTXion['from'])
        print "TO: {}".format(newTXion['to'])
        print "AMOUNT: {}\n".format(new_txion['amount'])
        return("Transaction successful\n")

node.run()
