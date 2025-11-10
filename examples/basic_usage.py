"""
Basic usage examples for ByteChan
"""

from bytechan import Blockchain, Wallet, Transaction, Network
from bytechan.crypto import RingSignature
from bytechan.privacy import TransactionMixer


def example_basic_transaction():
    """Create and mine a basic transaction"""
    print("=== Basic Transaction Example ===\n")
    
    # Create blockchain
    blockchain = Blockchain()
    
    # Create wallets
    alice = Wallet.create()
    bob = Wallet.create()
    
    print(f"Alice's address: {alice.get_address()}")
    print(f"Bob's address: {bob.get_address()}\n")
    
    # Mine initial coins for Alice
    print("Mining initial coins for Alice...")
    blockchain.mine_pending_transactions(alice.get_address())
    alice.update_balance(blockchain)
    print(f"Alice's balance: {alice.balance} BTC\n")
    
    # Create transaction from Alice to Bob
    tx = Transaction(
        sender=alice.get_address(),
        recipient=bob.get_address(),
        amount=5.0,
        privacy_level="MEDIUM"
    )
    
    blockchain.add_transaction(tx)
    
    # Mine the transaction
    print("Mining transaction...")
    blockchain.mine_pending_transactions(alice.get_address())
    
    # Update balances
    alice.update_balance(blockchain)
    bob.update_balance(blockchain)
    
    print(f"Alice's balance: {alice.balance} BTC")
    print(f"Bob's balance: {bob.balance} BTC")


def example_private_transaction():
    """Create a private transaction with ring signature"""
    print("\n=== Private Transaction Example ===\n")
    
    blockchain = Blockchain()
    
    # Create wallets
    alice = Wallet.create()
    bob = Wallet.create()
    
    # Mine coins for Alice
    blockchain.mine_pending_transactions(alice.get_address())
    alice.update_balance(blockchain)
    
    print(f"Alice's balance: {alice.balance} BTC")
    
    # Create private transaction
    tx = Transaction(
        sender=alice.get_address(),
        recipient=bob.get_address(),
        amount=3.0,
        privacy_level="HIGH"
    )
    
    # Apply privacy features
    tx.apply_ring_signature(ring_size=21)
    tx.apply_stealth_address()
    tx.apply_confidential_transaction()
    
    print(f"\nPrivate transaction created:")
    print(f"  TX ID: {tx.tx_id[:16]}...")
    print(f"  Sender: {tx.sender} (obfuscated with ring signature)")
    print(f"  Recipient: {tx.recipient} (stealth address)")
    print(f"  Amount: {tx.amount if not tx.is_confidential else 'CONFIDENTIAL'}")
    print(f"  Privacy Level: {tx.privacy_level}")


def example_stealth_addresses():
    """Demonstrate stealth address generation"""
    print("\n=== Stealth Address Example ===\n")
    
    wallet = Wallet.create()
    
    print(f"Regular address: {wallet.get_address()}\n")
    print("Generating stealth addresses:")
    
    for i in range(5):
        stealth = wallet.get_stealth_address()
        print(f"  {i+1}. {stealth}")
    
    print("\nEach stealth address is unique and unlinkable!")


def example_network_privacy():
    """Demonstrate network-level privacy features"""
    print("\n=== Network Privacy Example ===\n")
    
    # Create node with Tor support
    network = Network(port=18080, use_tor=True)
    
    print("Node created with Tor support")
    print(f"Node ID: {network.node_id}")
    print(f"Max peers: {network.max_peers}")


if __name__ == "__main__":
    example_basic_transaction()
    example_private_transaction()
    example_stealth_addresses()
    example_network_privacy()
    
    print("\n=== Examples Complete ===")
