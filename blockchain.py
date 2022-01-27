
# Importing the libraries
import datetime
import hashlib
import json

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(data = {})

    def create_block(self, data):
        if len(self.chain) == 0:
            initial_block = {
                'index': len(self.chain) + 1,
                'timestamp': str(datetime.datetime.now()),
                'data': data,
                'previous_hash': 0,
                'nonce': 1}

            initial_block = self.calculate_nonce(initial_block)
            print(initial_block)

            self.chain.append(initial_block)
            return initial_block
        else:
            block = {
                'index': len(self.chain) + 1,
                'timestamp': str(datetime.datetime.now()),
                "data": data,
                "previous_hash": self.get_previous_block()["hash"],
                "nonce" : 1}  # nonce always starts at 1 and increments up

            block = self.calculate_nonce(block)

            self.chain.append(block)
            return block

    def get_previous_block(self):
        return self.chain[-1]

    def calculate_nonce(self, block):
        check_nonce = False
        while check_nonce is False:

            # Hash the block
            hash_value = self.hash(block)

            # need to find a hexadecimal hash that is less than target
            # The target in this case is any hexadecimal number with 4 zeros at the start
            if hash_value[:4] == '0000':
                print(f"hash value: ${hash_value}")
                print(f"nonce: ${block['nonce']}")
                check_nonce = True
                block["hash"] = hash_value  # Assign hash key to the block
            else:
                # Adjust the nonce until the target hash is met
                block["nonce"] += 1
        return block
    
    def hash(self, block):
        # The encode() method encodes the string, using the specified encoding. If no encoding is specified,
        # UTF-8 will be used. Encoding is the process of converting characters in human languages into binary
        # sequences that computers can process.
        # https://blog.hubspot.com/website/what-is-utf-8
        # json.dumps() function converts a Python object into a json string
        encoded_block = json.dumps(block, sort_keys=True).encode('utf8')
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0].copy()
        previous_block.pop("hash")  # remove hash value so that i can re-hash the whole block
        block_index = 1
        while block_index < len(chain):
            current_block = chain[block_index].copy()
            current_block.pop("hash")
            # check if the (current block's previous hash key) is different than the hash of the previous block
            if current_block["previous_hash"] != self.hash(previous_block):
                print("previous hash is wrong")
                return False
            # check if the hash (proof of work) of the current block matches the target given
            hash_operation = self.hash(current_block)
            if hash_operation[:4] != '0000':
                print("current hash is wrong")
                return False
            previous_block = current_block
            block_index += 1
        return True
    
