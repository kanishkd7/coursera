#Q1
import yfinance as yf
import pandas as pd

# Extract Tesla stock data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

# Display first five rows
tesla_data.head()

#Q2
import requests
from bs4 import BeautifulSoup
# Tesla revenue scraping
url_tesla = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_tesla = requests.get(url_tesla).text
soup_tesla = BeautifulSoup(html_tesla, "html.parser")
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for table in soup_tesla.find_all("table"):
    if "Tesla Quarterly Revenue" in str(table):
        tesla_revenue = pd.read_html(str(table))[0]
tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r"\$|,", "", regex=True)
tesla_revenue.dropna(inplace=True)
# Display last five rows
tesla_revenue.tail()

#Q3
# Extract GameStop stock data
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
# Display first five rows
gme_data.head()

#Q4
# GameStop revenue scraping
url_gme = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_gme = requests.get(url_gme).text
soup_gme = BeautifulSoup(html_gme, "html.parser")
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for table in soup_gme.find_all("table"):
    if "GameStop Quarterly Revenue" in str(table):
        gme_revenue = pd.read_html(str(table))[0]
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(r"\$|,", "", regex=True)
gme_revenue.dropna(inplace=True)
# Display last five rows
gme_revenue.tail()

#Q5
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock_name):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        subplot_titles=(f"{stock_name} Stock Price", f"{stock_name} Revenue"), 
                        vertical_spacing=0.3)

    fig.add_trace(go.Scatter(x=stock_data['Date'], y=stock_data['Close'], 
                             name="Stock Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=revenue_data['Date'], y=revenue_data['Revenue'].astype(float), 
                             name="Revenue"), row=2, col=1)

    fig.update_layout(title_text=f"{stock_name} Stock Price & Revenue Dashboard", showlegend=False)
    fig.show()
make_graph(tesla_data, tesla_revenue, "Tesla")

#Q6
make_graph(gme_data, gme_revenue, "GameStop")
