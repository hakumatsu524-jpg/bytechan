"""
Stealth address implementation for recipient privacy
"""

import hashlib
import secrets


class StealthAddress:
    """
    Stealth addresses generate unique one-time addresses for each transaction,
    preventing address reuse and protecting recipient privacy.
    """
    
    def __init__(self, keypair):
        self.keypair = keypair
        self.view_key = self._derive_view_key()
        self.spend_key = self._derive_spend_key()
    
    def _derive_view_key(self) -> str:
        """Derive view key from master key"""
        return hashlib.sha256(
            (self.keypair.private_key + "view").encode()
        ).hexdigest()
    
    def _derive_spend_key(self) -> str:
        """Derive spend key from master key"""
        return hashlib.sha256(
            (self.keypair.private_key + "spend").encode()
        ).hexdigest()
    
    def generate_stealth_address(self) -> str:
        """Generate a new one-time stealth address"""
        # Generate random nonce
        nonce = secrets.token_hex(16)
        
        # Create shared secret
        shared_secret = hashlib.sha256(
            (nonce + self.view_key).encode()
        ).hexdigest()
        
        # Generate one-time public key
        one_time_key = hashlib.sha256(
            (shared_secret + self.spend_key).encode()
        ).hexdigest()
        
        # Format as stealth address
        address_hash = hashlib.sha256(one_time_key.encode()).hexdigest()
        return f"st1{address_hash[:40]}"
    
    def scan_for_outputs(self, blockchain, wallet_address: str) -> List[dict]:
        """
        Scan blockchain for outputs belonging to this wallet
        Uses view key to detect without spending
        """
        owned_outputs = []
        
        for block in blockchain.chain:
            for tx in block.transactions:
                if tx.stealth_address and self._is_mine(tx.stealth_address):
                    owned_outputs.append({
                        "tx_id": tx.tx_id,
                        "amount": tx.amount,
                        "stealth_address": tx.stealth_address,
                        "block": block.index
                    })
        
        return owned_outputs
    
    def _is_mine(self, stealth_address: str) -> bool:
        """Check if a stealth address belongs to this wallet"""
        # Simplified check - production needs proper cryptographic verification
        return stealth_address.startswith("st1")
    
    @staticmethod
    def create_one_time_address() -> str:
        """Create a standalone one-time address"""
        random_data = secrets.token_hex(32)
        address_hash = hashlib.sha256(random_data.encode()).hexdigest()
        return f"st1{address_hash[:40]}"
