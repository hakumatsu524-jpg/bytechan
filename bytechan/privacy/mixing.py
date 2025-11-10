"""
Advanced transaction mixing for enhanced privacy
"""

import secrets
from typing import List
from bytechan.core.transaction import Transaction


class TransactionMixer:
    """
    Advanced mixing service for additional transaction privacy
    """
    
    def __init__(self):
        self.mix_pool: List[Transaction] = []
        self.min_mix_size = 10
    
    def add_to_pool(self, transaction: Transaction):
        """Add transaction to mixing pool"""
        self.mix_pool.append(transaction)
    
    def mix_transactions(self) -> List[Transaction]:
        """
        Mix transactions in pool to obscure linkages
        Returns mixed transactions when pool is large enough
        """
        if len(self.mix_pool) < self.min_mix_size:
            return []
        
        # Shuffle transactions
        mixed = self.mix_pool.copy()
        secrets.SystemRandom().shuffle(mixed)
        
        # Add time delays (represented as timestamp adjustments)
        for tx in mixed:
            tx.timestamp += secrets.randbelow(300)  # Random 0-5 minute delay
        
        # Clear pool and return mixed transactions
        self.mix_pool = []
        return mixed
    
    def create_chained_mix(self, transaction: Transaction, 
                          num_hops: int = 3) -> List[Transaction]:
        """
        Create a chain of intermediate transactions for mixing
        Each hop adds an additional layer of privacy
        """
        chain = []
        current_tx = transaction
        
        for i in range(num_hops):
            # Create intermediate address
            intermediate_address = f"mix_{secrets.token_hex(20)}"
            
            # Create hop transaction
            hop_tx = Transaction(
                sender=current_tx.sender,
                recipient=intermediate_address,
                amount=current_tx.amount,
                privacy_level=current_tx.privacy_level
            )
            hop_tx.apply_ring_signature()
            hop_tx.apply_stealth_address()
            
            chain.append(hop_tx)
            current_tx = hop_tx
        
        # Final transaction to actual recipient
        final_tx = Transaction(
            sender=current_tx.recipient,
            recipient=transaction.recipient,
            amount=transaction.amount,
            privacy_level=transaction.privacy_level
        )
        final_tx.apply_ring_signature()
        final_tx.apply_stealth_address()
        chain.append(final_tx)
        
        return chain
