from flask import Flask, render_template
import yfinance as yf
import pandas as pd
import requests
import io
import math
import fear_greed
from datetime import datetime

app = Flask(__name__)

def fetch_metrics():
    metrics = {
        "vix": {"name": "VIX Index", "value": "N/A", "suffix": "", "status": "neutral"},
        "yield": {"name": "10Y Treasury Yield", "value": "N/A", "suffix": "%", "status": "neutral"},
        "oil": {"name": "WTI Crude Oil", "value": "N/A", "suffix": "", "status": "neutral"},
        "gold": {"name": "Gold", "value": "N/A", "suffix": "", "status": "neutral"},
        "drawdown": {"name": "SPX / NDX Drawdown", "value": "N/A", "suffix": "%", "status": "neutral"},
        "fear_greed": {"name": "CNN Fear & Greed", "value": "N/A", "suffix": "", "status": "neutral"},
        "credit_spread": {"name": "Credit Spread (HY)", "value": "N/A", "suffix": "%", "status": "neutral"},
        "bank_risk": {"name": "Bank Credit Risk", "value": "Placeholder", "suffix": "", "status": "neutral"},
        "market_breadth": {"name": "Market Breadth", "value": "Placeholder", "suffix": "", "status": "neutral"}
    }

    # 1. Fetch yfinance tickers
    try:
        tickers = {
            "^VIX": "vix",
            "^TNX": "yield",
            "CL=F": "oil",
            "GC=F": "gold"
        }
        data = yf.download(list(tickers.keys()), period="1d", progress=False)['Close']
        for ticker, key in tickers.items():
            val = data[ticker].iloc[-1]
            metrics[key]["value"] = round(val, 2)
            if key == "vix":
                metrics[key]["status"] = "risk-off" if val > 20 else "risk-on"
    except Exception as e:
        print(f"Error fetching yfinance: {e}")

    # 2. Calculate SPY & QQQ Drawdown
    try:
        # Fetching 1y data for both indexes
        indexes = yf.download(["SPY", "QQQ"], period="1y", progress=False)['Close']
        
        # Calculate SPY Drawdown
        spy_series = indexes['SPY'].dropna()
        spy_dd = ((spy_series.iloc[-1] - spy_series.max()) / spy_series.max()) * 100
        
        # Calculate QQQ Drawdown
        qqq_series = indexes['QQQ'].dropna()
        qqq_dd = ((qqq_series.iloc[-1] - qqq_series.max()) / qqq_series.max()) * 100
        
        # Store as dictionary for two-column layout in template
        metrics["drawdown"]["value"] = {"spy": round(spy_dd, 1), "qqq": round(qqq_dd, 1)}
        metrics["drawdown"]["status"] = "risk-off" if (spy_dd < -5 or qqq_dd < -5) else "risk-on"
    except Exception as e:
        print(f"Error calculating combined drawdown: {e}")

    # 3. Fetch CNN Fear & Greed
    try:
        score = fear_greed.get_score()
        metrics["fear_greed"]["value"] = int(score)
        metrics["fear_greed"]["status"] = "risk-off" if score < 40 else "risk-on"
    except Exception as e:
        print(f"Error fetching Fear & Greed: {e}")

    # 4. Fetch Credit Spread (FRED)
    try:
        url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2"
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text))
        # Get the last row which is not '.' (placeholder for missing data)
        valid_data = df[df['BAMLH0A0HYM2'] != '.']
        latest_val = float(valid_data['BAMLH0A0HYM2'].iloc[-1])
        metrics["credit_spread"]["value"] = latest_val
        metrics["credit_spread"]["status"] = "risk-off" if latest_val > 4.5 else "risk-on"
    except Exception as e:
        print(f"Error fetching FRED: {e}")

    return metrics

@app.route('/')
def index():
    metrics = fetch_metrics()
    last_updated = datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', metrics=metrics, last_updated=last_updated)

if __name__ == '__main__':
    app.run(debug=True, port=8888)
