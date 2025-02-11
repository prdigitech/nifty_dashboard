import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Set title for the Streamlit dashboard
st.title("📊 Nifty 50 Market Dashboard with Candlestick and Moving Averages")

# Fetch the last 30 days of Nifty 50 data
nifty = yf.Ticker("^NSEI")
data = nifty.history(period="1mo")  # Fetch 1 month of data

# Check if data is available
if data.empty:
    st.warning("No data available for the given timeframe.")
else:
    # Reset index for better plotting
    data.reset_index(inplace=True)

    # Calculate moving averages
    data['20_MA'] = data['Close'].rolling(window=20).mean()
    data['50_MA'] = data['Close'].rolling(window=50).mean()

    # Create candlestick chart
    fig = go.Figure()

    # Add candlestick trace
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Price Candlestick'
    ))

    # Add 20-day moving average trace
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['20_MA'],
        mode='lines',
        name='20-Day MA',
        line=dict(color='orange')
    ))

    # Add 50-day moving average trace
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['50_MA'],
        mode='lines',
        name='50-Day MA',
        line=dict(color='green')
    ))

    # Layout configurations
    fig.update_layout(
        title="Nifty 50 Last 30 Days Candlestick Chart with Moving Averages",
        xaxis_title="Date",
        yaxis_title="Price (INR)",
        xaxis_rangeslider_visible=False,
        template="plotly_dark"
    )

    # Render Plotly chart in Streamlit
    st.plotly_chart(fig)
