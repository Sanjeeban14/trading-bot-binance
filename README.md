# Binance Futures Testnet Trading Bot

## Features
- Place MARKET, LIMIT, and STOP orders
- Supports BUY and SELL
- CLI-based input
- Input validation
- Logging of requests, responses, and errors

## Setup

1. Clone repo
2. Install dependencies:
```
   pip install -r requirements.txt
```
3. Create `.env`:
```
   API_KEY=your_key
   API_SECRET=your_secret
```
4. Run examples:

### Market Order
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```
### Limit Order
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

### Stop-Limit Order
```
python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.001 --price 77500 --stop_price 76500
```
## Logs
- Stored in `bot.log`

## Assumptions
- Uses Binance Futures Testnet
- Testnet may have delayed execution
