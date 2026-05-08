# Binance Futures Testnet Trading Bot

Simple CLI-based Binance Futures Testnet trading bot using Python.

Supports:
- MARKET Orders
- LIMIT Orders
- BUY and SELL
- Input Validation
- Logging
- Error Handling

---

# Features

- Binance Futures Testnet support
- CLI interface
- MARKET and LIMIT orders
- BUY and SELL support
- Clean modular architecture
- Logs API requests and responses
- Handles validation and network errors

---

# Project Structure

```bash
app/
    client.py
    orders.py
    validators.py
    logger.py
    cli.py
```

---

# Setup Instructions

## 1. Clone Project

```bash
git clone <repo_url>
cd binance-futures-bot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create Binance Futures Testnet Account

Testnet URL:

https://testnet.binancefuture.com

Generate:
- API Key
- Secret Key

---

## 5. Configure Environment Variables

Create `.env`

```env
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

---

# Run Application

```bash
python main.py
```

---

# Example MARKET Order

```bash
Enter Symbol (example BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): BUY
Enter Order Type (MARKET/LIMIT): MARKET
Enter Quantity: 0.001
```

---

# Example LIMIT Order

```bash
Enter Symbol (example BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): SELL
Enter Order Type (MARKET/LIMIT): LIMIT
Enter Quantity: 0.001
Enter Price: 95000
```

---

# Logs

Logs stored in:

```bash
logs/trading.log
```

Contains:
- API requests
- API responses
- Errors

---

# Bonus Feature Added

Improved CLI user experience with:
- Clear menus
- Structured output
- Better validation messages

---

# Tech Stack

- Python 3
- Requests
- Binance Futures REST API
