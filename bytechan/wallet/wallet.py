"""
Wallet implementation for ByteChan
"""

import hashlib
import secrets
from typing import Optional
from bytechan.crypto.keys import KeyPair
from bytechan.crypto.stealth_address import StealthAddress


class Wallet:
    """ByteChan wallet for managing keys and addresses"""
    
    def __init__(self, seed: Optional[str] = None):
        self.seed = seed or secrets.token_hex(32)
        self.keypair = KeyPair.from_seed(self.seed)
        self.stealth_generator = StealthAddress(self.keypair)
        self.balance = 0.0
    
    @classmethod
    def create(cls) -> 'Wallet':
        """Create a new wallet with random seed"""
        return cls()
    
    @classmethod
    def restore(cls, seed: str) -> 'Wallet':
        """Restore wallet from seed"""
        return cls(seed=seed)
    
    def get_address(self) -> str:
        """Get the wallet's public address"""
        return self.keypair.get_address()
    
    def get_stealth_address(self) -> str:
        """Generate a new stealth address"""
        return self.stealth_generator.generate_stealth_address()
    
    def get_seed(self) -> str:
        """Get the wallet seed (backup)"""
        return self.seed
    
    def sign_transaction(self, transaction) -> str:
        """Sign a transaction with private key"""
        return self.keypair.sign(transaction.tx_id)
    
    def update_balance(self, blockchain):
        """Update wallet balance from blockchain"""
        address = self.get_address()
        self.balance = blockchain.get_balance(address)
        return self.balance
    
    def to_dict(self) -> dict:
        """Export wallet information"""
        return {
            "address": self.get_address(),
            "balance": self.balance,
            "public_key": self.keypair.public_key
        }
