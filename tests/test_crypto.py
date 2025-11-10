"""
Unit tests for cryptographic functions
"""

import pytest
from bytechan.crypto import RingSignature, StealthAddress, Bulletproof
from bytechan.wallet import Wallet


def test_ring_signature():
    """Test ring signature generation and verification"""
    ring_sig = RingSignature(ring_size=11)
    
    wallet = Wallet.create()
    decoys = [f"decoy_{i}" for i in range(10)]
    
    ring = ring_sig.generate_ring(wallet.get_address(), decoys)
    assert len(ring) == 11
    assert wallet.get_address() in ring


def test_stealth_address():
    """Test stealth address generation"""
    wallet = Wallet.create()
    stealth_gen = StealthAddress(wallet.keypair)
    
    addr1 = stealth_gen.generate_stealth_address()
    addr2 = stealth_gen.generate_stealth_address()
    
    assert addr1 != addr2
    assert addr1.startswith("st1")
    assert addr2.startswith("st1")


def test_bulletproof():
    """Test bulletproof range proof"""
    bp = Bulletproof()
    
    # Generate proof
    proof = bp.generate_range_proof(value=100.0, min_value=0, max_value=1000)
    
    assert proof["commitment"]
    assert proof["proof"]
    assert bp.verify_range_proof(proof) == True


def test_bulletproof_out_of_range():
    """Test bulletproof rejects out-of-range values"""
    bp = Bulletproof()
    
    with pytest.raises(ValueError):
        bp.generate_range_proof(value=2000.0, min_value=0, max_value=1000)


def test_key_generation():
    """Test key pair generation"""
    wallet = Wallet.create()
    
    assert wallet.keypair.private_key
    assert wallet.keypair.public_key
    assert wallet.keypair.private_key != wallet.keypair.public_key
