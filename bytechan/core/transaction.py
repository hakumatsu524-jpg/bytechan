"""
Transaction handling with privacy features
"""

import hashlib
import json
import time
from typing import Optional
from enum import Enum


class PrivacyLevel(Enum):
    """Privacy levels for transactions"""
    LOW = "LOW"           # Ring size: 5
    MEDIUM = "MEDIUM"     # Ring size: 11
    HIGH = "HIGH"         # Ring size: 21
    MAXIMUM = "MAXIMUM"   # Ring size: 51+


class Transaction:
    """Transaction with privacy features"""
    
    def __init__(self, sender: str, recipient: str, amount: float, 
                 privacy_level: str = "MEDIUM", 
                 ring_signature: Optional[str] = None,
                 stealth_address: Optional[str] = None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
        self.privacy_level = privacy_level
        self.ring_signature = ring_signature
        self.stealth_address = stealth_address
        self.tx_id = self.calculate_id()
        self.is_confidential = False
    
    def calculate_id(self) -> str:
        """Calculate unique transaction ID"""
        tx_string = json.dumps({
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "privacy_level": self.privacy_level
        }, sort_keys=True)
        
        return hashlib.sha256(tx_string.encode()).hexdigest()
    
    def apply_ring_signature(self, ring_size: int = 11):
        """Apply ring signature for sender privacy"""
        # Simplified ring signature (in production, use actual cryptography)
        self.ring_signature = f"ring_sig_{ring_size}_{self.tx_id[:16]}"
        self.sender = "RING_" + self.sender[:10]  # Obfuscate sender
    
    def apply_stealth_address(self):
        """Apply stealth address for recipient privacy"""
        # Simplified stealth address (in production, use actual cryptography)
        self.stealth_address = f"stealth_{self.recipient[:16]}"
        self.recipient = self.stealth_address  # Replace with stealth address
    
    def apply_confidential_transaction(self):
        """Apply confidential transaction to hide amount"""
        self.is_confidential = True
        # In production, use Pedersen commitments and range proofs
    
    def is_valid(self) -> bool:
        """Validate transaction"""
        if self.amount <= 0:
            return False
        
        if self.sender == self.recipient:
            return False
        
        # Network rewards are always valid
        if self.sender == "NETWORK":
            return True
        
        return True
    
    def to_dict(self) -> dict:
        """Convert transaction to dictionary"""
        return {
            "tx_id": self.tx_id,
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount if not self.is_confidential else "CONFIDENTIAL",
            "timestamp": self.timestamp,
            "privacy_level": self.privacy_level,
            "ring_signature": self.ring_signature,
            "stealth_address": self.stealth_address
        }
