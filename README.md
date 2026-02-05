# Trader Performance vs Market Sentiment

This project analyzes how Bitcoin market sentiment (Fear vs Greed)
influences trader behavior and performance on Hyperliquid.

## Objective
- Study trader performance across sentiment regimes
- Identify behavioral changes in trade frequency, position sizing, and bias
- Propose actionable trading strategies
- Build a lightweight interactive dashboard

## Data
- Bitcoin Fear & Greed Index
- Hyperliquid historical trader data

## Methodology
- Data cleaning and daily aggregation
- Feature engineering (PnL, win rate, trade frequency, position size)
- Sentiment-based performance and behavior analysis
- Trader segmentation and strategy formulation

## Dashboard
A Streamlit dashboard (`app.py`) allows interactive exploration of
performance and behavior across Fear and Greed regimes.

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
