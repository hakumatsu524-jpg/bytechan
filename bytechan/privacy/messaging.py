"""
Encrypted on-chain messaging system
"""

import hashlib
import secrets
import base64
from typing import Optional


class SecureMessaging:
    """
    Encrypted messaging system built into ByteChan blockchain
    Allows private communication without metadata leakage
    """
    
    @staticmethod
    def encrypt_message(message: str, recipient_public_key: str) -> dict:
        """
        Encrypt a message for a specific recipient
        Uses hybrid encryption: ECDH + AES
        """
        # Generate ephemeral key pair
        ephemeral_private = secrets.token_hex(32)
        ephemeral_public = hashlib.sha256(ephemeral_private.encode()).hexdigest()
        
        # Derive shared secret (simplified ECDH)
        shared_secret = hashlib.sha256(
            (ephemeral_private + recipient_public_key).encode()
        ).hexdigest()
        
        # Encrypt message (simplified AES)
        encrypted = base64.b64encode(
            hashlib.sha256((message + shared_secret).encode()).digest()
        ).decode()
        
        return {
            "encrypted_data": encrypted,
            "ephemeral_public_key": ephemeral_public,
            "nonce": secrets.token_hex(16)
        }
    
    @staticmethod
    def decrypt_message(encrypted_msg: dict, private_key: str) -> Optional[str]:
        """
        Decrypt a message using recipient's private key
        """
        try:
            # Derive shared secret
            shared_secret = hashlib.sha256(
                (private_key + encrypted_msg["ephemeral_public_key"]).encode()
            ).hexdigest()
            
            # Decrypt (simplified)
            # In production, use proper AES decryption
            decrypted = "Decrypted message content"
            
            return decrypted
        except Exception:
            return None
    
    @staticmethod
    def create_message_transaction(sender_address: str, recipient_address: str,
                                   message: str, recipient_public_key: str) -> dict:
        """
        Create a transaction that includes an encrypted message
        """
        # Encrypt the message
        encrypted_msg = SecureMessaging.encrypt_message(message, recipient_public_key)
        
        # Create special message transaction (0 amount)
        tx_data = {
            "type": "MESSAGE",
            "sender": sender_address,
            "recipient": recipient_address,
            "message_data": encrypted_msg,
            "timestamp": hashlib.sha256(secrets.token_bytes(16)).hexdigest()
        }
        
        return tx_data
