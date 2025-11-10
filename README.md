# ByteChan (BTC) - Privacy-First Cryptocurrency

CA: soon

<p align="center">
  <img src="assets/bytechan-logo.png" alt="ByteChan Logo" width="300"/>
</p>

<p align="center">
  <strong>Infrastructure for the Private Internet</strong>
</p>

<p align="center">
  <em>Every action is tracked. Personal data flows through unseen markets. Public chains expose financial activity to anyone who looks. Privacy has vanished.</em>
</p>

<p align="center">
  ByteChan is changing that. We're turning advanced cryptography into simple tools for private computation, protected ownership, and secure interaction that give people real control.
</p>

---

## 🔒 Core Privacy Features

### Advanced Cryptography
- **Ring Signatures** - Hide transaction sender among a group of possible signers
- **Stealth Addresses** - One-time addresses for every transaction
- **Confidential Transactions** - Encrypted transaction amounts using Pedersen commitments
- **Bulletproofs** - Efficient zero-knowledge range proofs
- **RingCT** - Combination of ring signatures and confidential transactions

### Enhanced Features (Beyond Monero)
- **Multi-Layer Privacy** - Optional privacy layers for different use cases
- **Encrypted Messaging** - On-chain encrypted communication
- **Private Smart Contracts** - Privacy-preserving computation
- **Decentralized VPN Integration** - Built-in private networking
- **Zero-Knowledge Identity** - Prove attributes without revealing identity
- **Time-Locked Transactions** - Future-dated private transactions
- **Atomic Swaps** - Cross-chain private exchanges
- **Quantum-Resistant Signatures** - Future-proof cryptography

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenSSL
- GCC/Clang compiler

### Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/yourusername/bytechan.git
cd bytechan

# Install Python dependencies
pip install -r requirements.txt

# Build the project
python setup.py build

# Run tests
python -m pytest tests/
\`\`\`

### Quick Start

\`\`\`python
from bytechan import Wallet, Transaction, Network

# Create a new wallet
wallet = Wallet.create()
print(f"Address: {wallet.get_address()}")

# Send a private transaction
tx = Transaction.create_private(
    from_wallet=wallet,
    to_address="bc1...",
    amount=1.5,
    privacy_level=PrivacyLevel.HIGH
)

# Broadcast to network
Network.broadcast(tx)
\`\`\`

## 📚 Documentation

### Architecture

\`\`\`
bytechan/
├── core/              # Core blockchain logic
│   ├── blockchain.py  # Blockchain implementation
│   ├── block.py       # Block structure
│   ├── transaction.py # Transaction handling
│   └── consensus.py   # Proof-of-Work consensus
├── crypto/            # Cryptographic primitives
│   ├── ring_signature.py
│   ├── stealth_address.py
│   ├── bulletproofs.py
│   ├── pedersen.py
│   └── zkp.py
├── network/           # P2P networking
│   ├── p2p.py
│   ├── sync.py
│   └── protocol.py
├── wallet/            # Wallet functionality
│   ├── wallet.py
│   ├── keys.py
│   └── address.py
├── privacy/           # Enhanced privacy features
│   ├── mixing.py
│   ├── messaging.py
│   ├── smart_contracts.py
│   └── vpn_integration.py
└── utils/             # Utility functions
    ├── serialization.py
    └── encoding.py
\`\`\`

## 🔐 Privacy Levels

ByteChan offers multiple privacy levels to balance privacy, speed, and cost:

| Level | Ring Size | Proof Type | Speed | Privacy | Use Case |
|-------|-----------|------------|-------|---------|----------|
| **LOW** | 5 | Standard | Fast | Good | Small transactions |
| **MEDIUM** | 11 | Enhanced | Normal | High | General use |
| **HIGH** | 21 | Bulletproofs | Slower | Very High | Sensitive transactions |
| **MAXIMUM** | 51+ | Advanced ZK | Slowest | Absolute | Maximum privacy needed |

## 🛠️ Technical Specifications

- **Algorithm**: RandomX (CPU-friendly PoW)
- **Block Time**: 2 minutes
- **Block Reward**: 10 BTC (decreasing)
- **Max Supply**: 21,000,000 BTC
- **Ring Size**: 11 (default), up to 51
- **Address Format**: Bech32 with privacy prefix
- **Transaction Version**: v3 (RingCT)

## 📖 Usage Examples

### Creating a Stealth Address

\`\`\`python
from bytechan.crypto import StealthAddress

# Generate stealth address
stealth = StealthAddress.generate()
one_time_address = stealth.create_one_time_address()
print(f"One-time address: {one_time_address}")
\`\`\`

### Ring Signature Transaction

\`\`\`python
from bytechan.crypto import RingSignature
from bytechan import Transaction

# Create transaction with ring signature
tx = Transaction.create_with_ring(
    inputs=my_utxos,
    outputs=[{"address": recipient, "amount": 5.0}],
    ring_size=11,
    mixin_sources=network.get_mixin_outputs(11)
)
\`\`\`

### Encrypted Messaging

\`\`\`python
from bytechan.privacy import SecureMessaging

# Send encrypted message on-chain
msg = SecureMessaging.encrypt(
    message="Hello, privately!",
    recipient_address="bc1..."
)
Network.broadcast_message(msg)
\`\`\`

### Zero-Knowledge Proof

\`\`\`python
from bytechan.crypto import ZKProof

# Prove you own > 10 BTC without revealing amount
proof = ZKProof.create_range_proof(
    amount=my_balance,
    min_amount=10.0
)
print(f"Valid: {proof.verify()}")
\`\`\`

## 🔬 Security Considerations

- **Quantum Resistance**: Implements NIST post-quantum algorithms
- **Side-Channel Protection**: Constant-time operations for cryptographic functions
- **Network Privacy**: Built-in Tor/I2P support
- **Key Management**: Hardware wallet support (Ledger, Trezor)
- **Regular Audits**: Open-source security audits every quarter

## 🌐 Network

### Mainnet
- **Network ID**: bytechan-mainnet
- **Default Port**: 18080
- **RPC Port**: 18081
- **Genesis Block**: [View on Explorer](https://explorer.bytechan.org)

### Testnet
- **Network ID**: bytechan-testnet
- **Default Port**: 28080
- **RPC Port**: 28081
- **Faucet**: [Get Test BTC](https://faucet.bytechan.org)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

\`\`\`bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/bytechan.git
cd bytechan

# Create a development environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ --cov=bytechan

# Run linter
flake8 bytechan/
black bytechan/
\`\`\`

## ⚠️ Disclaimer

ByteChan is experimental software. Use at your own risk. Always verify addresses and test with small amounts first. Privacy features do not guarantee absolute anonymity. Follow local regulations regarding cryptocurrency usage.

## 🙏 Acknowledgments

Built with inspiration from:
- Monero (XMR) - Ring signatures and stealth addresses
- Zcash (ZEC) - Zero-knowledge proofs
- MimbleWimble - Confidential transactions
- Bitcoin (BTC) - Blockchain fundamentals

---

<p align="center">
  <strong>ByteChan - Privacy is a right, not a privilege</strong>
</p>
