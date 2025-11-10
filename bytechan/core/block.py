"""
Block structure for ByteChan blockchain
"""

import hashlib
import json
import time
from typing import List
from bytechan.core.transaction import Transaction


class Block:
    """Individual block in the blockchain"""
    
    def __init__(self, index: int, timestamp: float, transactions: List[Transaction], 
                 previous_hash: str, nonce: int = 0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """Calculate SHA-256 hash of block contents"""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int):
        """Proof of Work mining with RandomX-like algorithm"""
        target = "0" * difficulty
        
        print(f"Mining block {self.index}...")
        start_time = time.time()
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            
            # Progress indicator
            if self.nonce % 10000 == 0:
                print(f"  Nonce: {self.nonce}, Hash: {self.hash[:10]}...")
        
        elapsed = time.time() - start_time
        print(f"Block mined! Hash: {self.hash}")
        print(f"Time taken: {elapsed:.2f} seconds, Nonce: {self.nonce}")
    
    def to_dict(self) -> dict:
        """Convert block to dictionary"""
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash
        }
