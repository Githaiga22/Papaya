# 🥭 Papaya - DeFi Lending on XRP Ledger

**Collateralized lending protocol powered by the XRP Ledger Testnet**

Built for NUS Fintech Summit 2026 Hackathon by Team Papaya 🚀

---

## 🎯 What is Papaya?

Papaya is a **decentralized lending platform** where users can:
- 💰 **Deposit crypto assets** as collateral
- 📈 **Borrow against your deposits** (up to 50% of collateral value)
- 🔄 **Swap between assets** with real-time market rates
- 🌍 **Access global markets** including crypto (BTC, ETH, SOL, XRP) and fiat (Kenyan Shilling)

Think of it as **your personal DeFi bank** on the blockchain.

---

## 🔗 How XRP Powers Papaya

### XRPL Testnet Integration

**Real Blockchain Features:**
- ✅ **Auto Wallet Creation**: New users get XRPL wallets automatically
- ✅ **Testnet Funding**: Wallets funded with 100 test XRP from faucet
- ✅ **Live Balance Reading**: Real-time XRP balance queries from XRPL testnet
- ✅ **Transaction Tracking**: Complete history with blockchain-ready hashes

**XRP as Collateral:**
```
Your 100 XRP ($52 @ $0.52/XRP)
   ↓
Can borrow up to $26 worth of:
   • USDC, USDT (Stablecoins)
   • ETH, BTC, SOL (Crypto)
   • KSH (Kenyan Shilling)
```

**Why XRPL?**
- ⚡ **Fast**: 3-5 second settlement
- 💵 **Cheap**: Minimal transaction fees (~0.00001 XRP)
- 🌐 **Global**: Cross-border payments built-in
- 🔒 **Secure**: Battle-tested Layer 1 blockchain

---

## ✨ Key Features

### 1. **Instant Onboarding**
- Register with username + password
- XRPL wallet created automatically
- Funded with 100 test XRP from faucet
- Start borrowing in seconds

### 2. **Multi-Asset Support**
| Asset | Type | Price Feed |
|-------|------|------------|
| XRP | Crypto | Real XRPL Testnet Balance |
| BTC, ETH, SOL | Crypto | CoinGecko API (Real-time) |
| USDC, USDT | Stablecoins | CoinGecko API (Real-time) |
| KSH | Fiat (Kenyan Shilling) | ExchangeRate API (Real-time) |

### 3. **Smart Collateralization**
- **Loan-to-Value (LTV)**: Borrow up to 50% of your collateral
- **Liquidation Threshold**: Must maintain 200% collateralization
- **Automatic Protection**: System prevents over-borrowing

### 4. **Real-Time Swaps**
- Swap between any assets instantly
- Live market rates from CoinGecko & ExchangeRate APIs
- 0.3% swap fee
- Transaction hash proof for every swap

### 5. **Transaction History**
- Complete audit trail of all operations
- Unique transaction hash for each action
- Blockchain explorer links (for real XRPL transactions)
- Timestamps and detailed breakdowns

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Githaiga22/Papaya.git
cd Papaya

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "SECRET_KEY=your-secret-key-here" > .env

# Initialize database
python3 db_setup.py

# Run the application
python3 app.py
```

Visit: `http://127.0.0.1:5005`

---

## 🎮 How to Use

### 1. **Register**
```
Username: yourusername
Password: ********
```
→ XRPL wallet created & funded automatically!

### 2. **Get Demo Tokens**
- Go to **Deposit** page
- Click **"💰 Get Demo Tokens"**
- Receive: 100K KSH, 10K USDC, 10K USDT, 5 ETH, 0.5 BTC, 100 SOL

### 3. **Check Your Balance**
- **Dashboard** shows:
  - ✅ Real 100 XRP from XRPL testnet
  - ✅ Demo tokens for testing
  - Your borrowing capacity

### 4. **Borrow Assets**
```
Example:
Collateral: 100 XRP = $52
Max Borrow: $26 (50% LTV)

Action: Borrow 26 USDC
Result: 26 USDC added to your balance
```

### 5. **Swap Assets**
```
Swap: 10 USDC → XRP
Rate: Real-time from CoinGecko
Fee: 0.3%
Result: ~19.2 XRP received
```

### 6. **View History**
- Click **"📜 History"** in menu
- See all transactions with hashes
- Click **"View on Explorer"** for XRPL transactions

---

## 🏗️ Architecture

### Smart Contract Logic (Python Backend)
```python
# Collateralization Check
collateral_value_usd = user_deposits * asset_price
max_borrow_usd = collateral_value_usd * 0.5  # 50% LTV

# Liquidation Trigger
if collateral_value < borrowed_value * 2:
    liquidate()  # Below 200% collateralization
```

### XRPL Integration
```python
# Read real XRP balance
from xrpl.clients import JsonRpcClient
from xrpl.models import AccountInfo

client = JsonRpcClient("https://s.altnet.rippletest.net:51234")
response = client.request(AccountInfo(account=wallet_address))
xrp_balance = int(response.result['account_data']['Balance']) / 1_000_000
```

### Real-Time Pricing
```python
# CoinGecko API for crypto prices
def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    return requests.get(url).json()[crypto_id]["usd"]

# ExchangeRate API for fiat
def get_fiat_rate(currency_code):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    rates = requests.get(url).json()["rates"]
    return 1 / rates[currency_code]  # USD value of 1 unit
```

---

## 📊 System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         PAPAYA                              │
│                 DeFi Lending on XRPL                        │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────▼────┐          ┌────▼────┐          ┌────▼────┐
   │ Deposit │          │ Borrow  │          │  Swap   │
   │ Assets  │          │ Against │          │ Assets  │
   └────┬────┘          │Collateral│         └────┬────┘
        │               └────┬────┘               │
        │                    │                    │
   ┌────▼────────────────────▼────────────────────▼────┐
   │         XRPL Testnet (Real XRP Balance)          │
   │    CoinGecko API (Real-time Crypto Prices)       │
   │  ExchangeRate API (Real-time Fiat Rates)         │
   └──────────────────────────────────────────────────┘
```

---

## 🛡️ Security & Risk Management

### Collateralization Rules
- **Minimum Collateral Ratio**: 200%
- **Maximum LTV**: 50%
- **Liquidation Penalty**: Applied when ratio falls below threshold

### Demo vs Production
⚠️ **This is a HACKATHON DEMO**:
- ✅ Real XRPL testnet integration (reads balance)
- ✅ Real-time price feeds
- ⚠️ Demo tokens (not on blockchain except XRP)
- ⚠️ Swaps update database (not real blockchain transactions)
- ⚠️ No audit (not production-ready)

**For Production**:
- Smart contract audits required
- Real XRPL payment transactions
- Multi-signature wallets
- Insurance fund
- Decentralized governance

---

## 🎯 Use Cases

### 1. **Emergency Liquidity (No Selling Assets)**
```
Scenario: Need cash but don't want to sell XRP
Solution: Borrow USDC against XRP collateral
Benefit: Keep XRP exposure, get immediate liquidity
```

### 2. **Cross-Border Remittance**
```
Scenario: Send money to Kenya (KSH)
Solution: Deposit XRP → Borrow KSH → Send to recipient
Benefit: Instant, cheap, no forex spreads
```

### 3. **Yield Farming (Coming Soon)**
```
Scenario: Earn passive income on idle crypto
Solution: Deposit XRP → Earn interest from borrowers
Benefit: 4-8% APY on deposits
```

---

## 🔮 Roadmap

### Phase 1: ✅ Current (Hackathon MVP)
- Individual collateralized lending
- Real-time price feeds
- XRPL testnet integration
- Multi-asset support
- Transaction history

### Phase 2: 🚧 In Development (AAVE-Style)
- Shared liquidity pools
- Cross-user lending
- Interest accrual (depositors earn APY)
- Interest-bearing tokens (pXRP, pUSDC)
- Dynamic interest rates

### Phase 3: 🔮 Future
- Real XRPL payment transactions
- Flash loans
- NFT collateral
- Governance token ($PAPAYA)
- Multi-chain support (Ethereum, Polygon)

---

## 👥 Team Papaya

**Built for**: NUS Fintech Summit 2026 Hackathon
**Focus**: Financial inclusion through DeFi on XRPL

---

## 📜 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

- **XRP Ledger Foundation** - For the amazing blockchain infrastructure
- **CoinGecko** - Real-time cryptocurrency price data
- **ExchangeRate-API** - Fiat currency exchange rates
- **NUS Fintech Summit** - For the opportunity to innovate

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Githaiga22/Papaya/issues)
- **Testnet Explorer**: [XRPL Testnet](https://testnet.xrpl.org)
- **Demo Wallet**: `rfwHCz6KcUuZafbzcxYGzVCBGKVske1dwk`

---

<div align="center">

**Built with ❤️ by Team Papaya**

*Making DeFi accessible to everyone, one XRP at a time* 🥭

[Live Demo](http://127.0.0.1:5005) • [Documentation](https://github.com/Githaiga22/Papaya) • [Report Bug](https://github.com/Githaiga22/Papaya/issues)

</div>
