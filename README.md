Nifty 50 Market Dashboard

A real-time stock market analytics dashboard built using Streamlit, Plotly, and Yahoo Finance API. This project visualizes Nifty 50 market data for the last 30 days and includes candlestick charts with key technical indicators such as 20-day and 50-day moving averages.

Features
Real-Time Data: Fetches the latest Nifty 50 stock prices.
Interactive Candlestick Charts: Visual representation of price movements over the last 30 days.
Trend Indicators:
20-Day Moving Average (Short-term trend)
50-Day Moving Average (Medium-term trend)
Clean UI: Interactive plots with a dark theme for better visual clarity.
Tech Stack
Backend: Streamlit for the dashboard framework
Data Source: Yahoo Finance API via yfinance
Visualization: Plotly for dynamic and customizable charts
Data Processing: Pandas for handling and manipulating stock data
Installation Guide
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/prdigitech/nifty_dashboard.git
cd nifty_dashboard
2. Create and Activate a Virtual Environment (Optional but Recommended)
On Windows:
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
On Mac/Linux:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Alternatively, you can manually install the necessary packages:

bash
Copy
Edit
pip install streamlit yfinance plotly pandas
4. Run the Application
bash
Copy
Edit
streamlit run nifty_dashboard.py
How to Use
Open the Streamlit web interface that appears in the terminal.
View real-time market data, candlestick patterns, and moving averages for Nifty 50.
Code Breakdown
Data Fetching:
Fetches the last 30 days of Nifty 50 data using the yfinance library.

Data Processing:

Calculates moving averages (20-day and 50-day) using Pandas.
Visualization:

Candlestick chart displays market trends.
Overlays moving average plots for technical analysis using Plotly.
UI:
Interactive, clean dark-themed UI powered by Streamlit.

Libraries Used
streamlit: Dashboard framework
yfinance: Fetching market data
pandas: Data manipulation
plotly: Interactive visualization
Future Enhancements
Add more technical indicators like RSI and Bollinger Bands
Support additional indices and stocks
Create a user-friendly dashboard with filtering options
Example Output
Real-time dynamic plots showcasing candlestick trends with moving averages
License
This project is open-source and free to use under the MIT License.
