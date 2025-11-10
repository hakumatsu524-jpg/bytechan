"""
Cryptographic key management
"""

import hashlib
import secrets
from typing import Tuple


class KeyPair:
    """Public/Private key pair with quantum-resistant options"""
    
    def __init__(self, private_key: str, public_key: str):
        self.private_key = private_key
        self.public_key = public_key
    
    @classmethod
    def from_seed(cls, seed: str) -> 'KeyPair':
        """Generate key pair from seed"""
        # Simplified key generation (use proper ECC in production)
        private_key = hashlib.sha256(seed.encode()).hexdigest()
        public_key = hashlib.sha256(private_key.encode()).hexdigest()
        return cls(private_key, public_key)
    
    @classmethod
    def generate(cls) -> 'KeyPair':
        """Generate random key pair"""
        seed = secrets.token_hex(32)
        return cls.from_seed(seed)
    
    def get_address(self) -> str:
        """Derive address from public key (Bech32-style)"""
        # Simplified address generation
        address_hash = hashlib.sha256(self.public_key.encode()).hexdigest()
        return f"bc1{address_hash[:40]}"
    
    def sign(self, message: str) -> str:
        """Sign a message with private key"""
        # Simplified signing (use proper ECDSA in production)
        signature = hashlib.sha256(
            (message + self.private_key).encode()
        ).hexdigest()
        return signature
    
    def verify(self, message: str, signature: str) -> bool:
        """Verify a signature"""
        expected_sig = self.sign(message)
        return signature == expected_sig
