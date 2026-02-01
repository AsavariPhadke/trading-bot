# Binance Futures Trading Bot (Testnet)

A simplified Python trading bot for placing orders on **Binance Futures Testnet (USDT-M)**.
Built as part of a Python Developer assignment.

---

## Features
- Place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders
- Supports **BUY** and **SELL**
- CLI-based input with validation
- Structured, reusable codebase
- Detailed logging of API requests, responses, and errors
- Robust exception handling

---

## Tech Stack
- Python 3.x
- python-binance
- argparse
- logging

---

## Setup Instructions

### 1. Create Binance Futures Testnet Account
- Register at Binance Futures Testnet
- Generate API Key and Secret

### 2. Clone Repository
```bash
git clone <your-repo-url>
cd trading_bot

## Mock Execution Mode
Due to API key creation restrictions on Binance Futures Testnet,
a mock execution mode is provided.

This mode:
- Simulates Binance Futures order placement
- Generates realistic order responses
- Preserves validation, logging, and CLI flow
- Can be switched to real API execution by toggling a flag

The application is structured to support real API execution
without any code changes to business logic.
