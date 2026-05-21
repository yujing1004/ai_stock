# 📈 ai_stock: Autonomous Financial Health Dashboard

> **Autonomous financial health dashboard** tracking 9 multi-factor indicators to compute real-time market sentiment and risk-mitigation signals.

---

## 🚀 Overview

`ai_stock` is a sophisticated real-time sentiment analysis and risk-mitigation tool designed for the modern trader. By tracking 9 critical multi-factor indicators, it provides a holistic view of market health and generates actionable trading recommendations.

### 🔍 Market Indicators Tracked
- **Sentiment**: VIX (Volatility Index), Fear & Greed Index
- **Fixed Income**: Credit Spreads, Bond Yields (10Y/2Y)
- **Macro**: Commodities (Gold, Oil, Copper)
- **Market Breadth**: Real-time compute of sentiment signals

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Data Analysis**: Pandas, NumPy
- **Financial Data**: `yfinance` API
- **Framework**: Antigravity IDE Agent Framework
- **Frontend**: Tailwind CSS (via Flask templates)

---

## 📦 Installation Guide

Follow these steps to get your local environment up and running:

### 1. Clone the Repository
```bash
git clone https://github.com/yujing1004/ai_stock.git
cd ai_stock
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask pandas yfinance numpy
```

### 4. Boot the Server
```bash
python app.py
```
*Note: Make sure to implement `app.py` before running.*

---

## 🗺 Roadmap

- [ ] Core data ingestion engine (yfinance)
- [ ] Multi-factor sentiment algorithm implementation
- [ ] Real-time dashboard with Tailwind CSS
- [ ] Risk-mitigation signal alert system

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.