"""
Blockchain implementation for ByteChan
"""

import hashlib
import time
from typing import List, Optional
from bytechan.core.block import Block
from bytechan.core.transaction import Transaction


class Blockchain:
    """Main blockchain class managing the chain of blocks"""
    
    def __init__(self):
        self.chain: List[Block] = []
        self.difficulty = 4
        self.pending_transactions: List[Transaction] = []
        self.mining_reward = 10.0
        self.create_genesis_block()
    
    def create_genesis_block(self) -> Block:
        """Create the first block in the chain"""
        genesis_block = Block(
            index=0,
            timestamp=1704067200,  # Jan 1, 2024
            transactions=[],
            previous_hash="0" * 64,
            nonce=0
        )
        genesis_block.hash = genesis_block.calculate_hash()
        self.chain.append(genesis_block)
        return genesis_block
    
    def get_latest_block(self) -> Block:
        """Get the most recent block in the chain"""
        return self.chain[-1]
    
    def mine_pending_transactions(self, mining_reward_address: str):
        """Mine all pending transactions and add them to a new block"""
        # Create reward transaction
        reward_tx = Transaction(
            sender="NETWORK",
            recipient=mining_reward_address,
            amount=self.mining_reward,
            privacy_level="MEDIUM"
        )
        self.pending_transactions.append(reward_tx)
        
        # Create new block
        block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )
        
        # Mine the block
        block.mine_block(self.difficulty)
        
        # Add to chain
        self.chain.append(block)
        
        # Reset pending transactions
        self.pending_transactions = []
    
    def add_transaction(self, transaction: Transaction) -> bool:
        """Add a new transaction to pending transactions"""
        if not transaction.is_valid():
            return False
        
        self.pending_transactions.append(transaction)
        return True
    
    def get_balance(self, address: str) -> float:
        """Get the balance of an address"""
        balance = 0.0
        
        for block in self.chain:
            for tx in block.transactions:
                if tx.sender == address:
                    balance -= tx.amount
                if tx.recipient == address:
                    balance += tx.amount
        
        return balance
    
    def is_chain_valid(self) -> bool:
        """Validate the entire blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verify block hash
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Verify previous hash linkage
            if current_block.previous_hash != previous_block.hash:
                return False
            
            # Verify all transactions
            for tx in current_block.transactions:
                if not tx.is_valid():
                    return False
        
        return True
    
    def adjust_difficulty(self):
        """Dynamically adjust mining difficulty based on block time"""
        if len(self.chain) < 10:
            return
        
        last_10_blocks = self.chain[-10:]
        time_taken = last_10_blocks[-1].timestamp - last_10_blocks[0].timestamp
        expected_time = 10 * 120  # 10 blocks * 2 minutes
        
        if time_taken < expected_time * 0.8:
            self.difficulty += 1
        elif time_taken > expected_time * 1.2:
            self.difficulty = max(1, self.difficulty - 1)
