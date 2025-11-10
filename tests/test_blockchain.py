"""
Unit tests for blockchain functionality
"""

import pytest
from bytechan import Blockchain, Transaction, Wallet


def test_genesis_block():
    """Test genesis block creation"""
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1
    assert blockchain.chain[0].index == 0
    assert blockchain.chain[0].previous_hash == "0" * 64


def test_add_transaction():
    """Test adding transactions"""
    blockchain = Blockchain()
    wallet1 = Wallet.create()
    wallet2 = Wallet.create()
    
    tx = Transaction(
        sender=wallet1.get_address(),
        recipient=wallet2.get_address(),
        amount=5.0
    )
    
    assert blockchain.add_transaction(tx) == True
    assert len(blockchain.pending_transactions) == 1


def test_mining():
    """Test block mining"""
    blockchain = Blockchain()
    wallet = Wallet.create()
    
    blockchain.mine_pending_transactions(wallet.get_address())
    assert len(blockchain.chain) == 2
    assert blockchain.chain[1].index == 1


def test_balance():
    """Test wallet balance calculation"""
    blockchain = Blockchain()
    wallet = Wallet.create()
    
    # Mine reward
    blockchain.mine_pending_transactions(wallet.get_address())
    balance = blockchain.get_balance(wallet.get_address())
    
    assert balance == 10.0  # Mining reward


def test_chain_validity():
    """Test blockchain validation"""
    blockchain = Blockchain()
    wallet = Wallet.create()
    
    blockchain.mine_pending_transactions(wallet.get_address())
    assert blockchain.is_chain_valid() == True


def test_invalid_transaction():
    """Test that invalid transactions are rejected"""
    blockchain = Blockchain()
    wallet = Wallet.create()
    
    # Negative amount
    tx = Transaction(
        sender=wallet.get_address(),
        recipient=wallet.get_address(),
        amount=-5.0
    )
    
    assert blockchain.add_transaction(tx) == False
