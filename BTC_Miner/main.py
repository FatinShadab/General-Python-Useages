import sys
import json
import timeit
from config import *
from bitcoin import *
from hashlib import sha256
from datetime import datetime

from numba import jit
from numba import cuda
import numpy as np


class MINER:
    def __init__(self, mode):
        self.mode = mode
        self.json_storage = config_dict['json_file_path']
        self.prefix_str = '0'*config_dict['difficulty_lvl']

    def _SHA256(self, text):
        return sha256(text.encode("ascii")).hexdigest()

    def _get_private_keys(self):
        key1, key2, key3 = (random_key() for _ in range(3))
        return (key1, key2, key3)

    def _get_public_keys(self, private_keys):
        key1, key2, key3 = (privtopub(key) for key in private_keys)
        return (key1, key2, key3)

    def _multi_signature_address(self):
        private_key1, private_key2, private_key3 = self._get_private_keys()
        public_key1, public_key2, public_key3 = self._get_public_keys((private_key1, private_key2, private_key3))
        address = scriptaddr(mk_multisig_script(private_key1, private_key2, private_key3, 2,3))
        return {
            'private_keys':{'key_1':private_key1.encode("ascii").hex(), 'key_2':private_key2.encode("ascii").hex(), 'key_3':private_key3.encode("ascii").hex()},
            'public_keys':{'key_1':public_key1, 'key_2':public_key2, 'key_3':public_key3},
            'multi_signature_address':address,
        }

    def _for_loop(self, block_number, transaction, previous_hash, max_nonce):
        start_time = timeit.default_timer()
        for nonce in range(max_nonce+1):
            text = f"{block_number}{transaction}{previous_hash}{nonce}"
            hash_block =  self._SHA256(text)
            if hash_block.startswith(self.prefix_str):
                return {
                    'mode':0, 
                    'success':0,
                    'difficulty_lvl': self.prefix_str,
                    'block_number':block_number,
                    'transaction':transaction.encode("ascii").hex(),
                    'previous_hash':previous_hash,
                    'mined_hash':hash_block,
                    'nonce':nonce,
                    'max_nonce':max_nonce,
                    'runtime':timeit.default_timer()-start_time,
                    'date-time': str(datetime.now()),
                    }
        return {
            'mode': 0,
            'success':-1,
            'difficulty_lvl': self.prefix_str,
            'block_number':block_number,
            'transaction':transaction.encode("ascii").hex(),
            'previous_hash':previous_hash,
            'max_nonce':max_nonce,
            'runtime':timeit.default_timer()-start_time,
            'date-time': str(datetime.now()),
            }

    def _while_loop(self, block_number, transaction, previous_hash):
        start_time = timeit.default_timer()
        try:
            nonce = 0
            while True:
                text = f"{block_number}{transaction}{previous_hash}{nonce}"
                hash_block =  self._SHA256(text)
                if hash_block.startswith(self.prefix_str):
                    break
                else:
                    nonce += 1
                    #print(f"| {hash_block} | for nonce:{nonce-1} |")
                    continue
            return {
                    'mode':1, 
                    'success':0,
                    'difficulty_lvl': self.prefix_str,
                    'block_number':block_number,
                    'transaction':transaction.encode("ascii").hex(),
                    'previous_hash':previous_hash,
                    'mined_hash':hash_block,
                    'nonce':nonce,
                    'runtime':timeit.default_timer()-start_time,
                    'date-time': str(datetime.now()),
                    }
        except:
            return {
                'mode': 1,
                'success':-1,
                'difficulty_lvl': self.prefix_str,
                'block_number':block_number,
                'transaction':transaction.encode("ascii").hex(),
                'previous_hash':previous_hash,
                'max_nonce':nonce,
                'runtime':timeit.default_timer()-start_time,
                'date-time': str(datetime.now()),
                }

    def _db_entry(self, info1, info2):

        entry ={}
        for key in info1.keys():
            entry[key] = info1[key]
        for key in info2.keys():
            entry[key] = info2[key]

        with open(self.json_storage, "r") as db:
            try:
                data = json.load(db)
            except:
                data = []
            data.append(entry)
            with open(self.json_storage, "w") as db:
                json.dump(data, db)
        return 0

    def mine_btc(self, block_number, transaction, previous_hash, max_nonce=10000):
        MINER_INFO = self._multi_signature_address()
        if self.mode == 0:
            MINE_INFO = self._for_loop(block_number, transaction, previous_hash, max_nonce)
        else:
            MINE_INFO = self._while_loop(block_number, transaction, previous_hash)
        
        self._db_entry(MINER_INFO,MINE_INFO)

        if MINE_INFO['success'] == 0:
            print(f"{MINE_INFO['mined_hash']} founded at nonce: {MINE_INFO['nonce']} ({MINE_INFO['runtime']})")
        else:
            print(f"No hash found at current nonce: {MINE_INFO['max_nonce']} ({MINE_INFO['runtime']})")
        return 0


if __name__ == "__main__":
    miner = MINER(mode=1)

    miner.mine_btc(5, "turja-->omieo-->500 btc", '0000xdkabskdhbahsbdhj')