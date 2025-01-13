Markowitz Portfolio with Multiple Assets - Efficient Frontier
This project implements a portfolio optimization model using Markowitz's Theory, also known as the Efficient Frontier. The goal is to identify the optimal asset allocation that maximizes the expected return for a given level of risk. The portfolio consists of multiple assets, including stocks, commodities, fixed-income securities, and cryptocurrencies.

📋 Project Description

The code performs the following key steps:
1.Selection of assets for the portfolio
2.Retrieval of historical price data using the Yahoo Finance API (yfinance)
3.Calculation of mean returns and the covariance matrix of the assets
4.Monte Carlo simulation to find the efficient frontier
5.Identification of the portfolio with the maximum Sharpe Ratio
6.Visualization of the efficient frontier in a graph

🧮 Calculations Performed

1️⃣ Mean Returns and Covariance Matrix

After downloading historical price data, we calculate the daily percentage returns for each asset.
These values are essential for calculating the portfolio's risk and expected return. The mean return provides an estimate of the average return of each asset, while the covariance matrix measures how the returns of different assets move together. These metrics are used to construct an optimized portfolio that balances risk and return.

2️⃣ Portfolio Performance

Given a weight vector , the portfolio's return and risk are calculated as follows:
The expected return represents the weighted average of the individual asset returns, while the risk is measured by the portfolio's standard deviation, indicating how much the portfolio's returns can deviate from the expected return.

3️⃣ Monte Carlo Simulation

To find the efficient frontier, we perform a Monte Carlo simulation with 10,000 random portfolios.
Each portfolio is generated with random weights that sum to 100%. We calculate the return, risk, and Sharpe Ratio for each portfolio.

Sharpe Ratio:
Where:
 = Portfolio return
 = Risk-free rate (2%)
 = Portfolio risk

The portfolio with the highest Sharpe Ratio is considered the most efficient, as it offers the best risk-adjusted return.

💼 Asset Selection

The selected assets represent different investment classes:

S&P 500
^GSPC
Stocks (US)

Gold
GC=F
Commodities

Treasury Yield 5 Years
^FVX
Fixed Income

Bitcoin USD
BTC-USD
Cryptocurrencies

These assets were chosen to ensure diversification, including equities, fixed income, commodities, and cryptocurrencies.

📈 Results

✅ Optimal Allocation of Maximum Sharpe Ratio Portfolio:

Asset
Allocation (%)
Bitcoin: 6.97
Gold: 57.30
Treasury: 28.24
S&P 500: 7.49

This allocation maximizes the Sharpe Ratio, offering the best risk-adjusted return.

📊 Efficient Frontier Visualization

The generated graph shows the Efficient Frontier, highlighting the maximum Sharpe Ratio portfolio in red.

The X-axis represents risk (standard deviation).
The Y-axis represents the expected return.
The blue points are randomly simulated portfolios.
The red point represents the portfolio with the highest Sharpe Ratio.

📌 Conclusion

Markowitz's Theory allows for the construction of a diversified portfolio that maximizes the expected return for a given level of risk. In this project, we identified that the optimal portfolio, considering different asset classes, has the following allocation:
57.30% in Gold
28.24% in Fixed Income (Treasury)
7.49% in Stocks (S&P 500)
6.97% in Bitcoin

This allocation shows that, during the analyzed period, gold and fixed-income securities provide the best protection against risk, while stocks and Bitcoin contribute to increasing the expected return.
