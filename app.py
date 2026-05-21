from flask import Flask, render_template
import pandas as pd
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    # Simple verification of packages
    data = {'Status': ['Success'], 'Package': ['Pandas']}
    df = pd.DataFrame(data)
    
    return render_template('index.html', status="Environment Setup Complete", df_html=df.to_html(classes='min-w-full divide-y divide-gray-200'))

if __name__ == '__main__':
    app.run(debug=True)
