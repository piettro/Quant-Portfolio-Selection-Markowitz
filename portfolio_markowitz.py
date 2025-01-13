import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

portfolio = [
    {
        'Asset':'S&P 500',
        'Code':'^GSPC',
    },
    {
        'Asset':'Gold',
        'Code':'GC=F',
    },
    {
        'Asset':'Treasury Yield 5 Years',
        'Code':'^FVX',
    },
    {
        'Asset':'Bitcoin USD',
        'Code':'BTC-USD',
    }
]

portfolio = pd.DataFrame(portfolio)

start_date = '2022-01-01'
end_date = '2024-12-31'
data = yf.download(portfolio['Code'].to_list(), start=start_date, end=end_date)['Close']

returns = data.pct_change().dropna()

mean_returns = returns.mean()
cov_matrix = returns.cov()
risk_free_rate = 0.02

def portfolio_performance(weights, mean_returns, cov_matrix):
    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return portfolio_return, portfolio_std

def monte_carlo_simulation(mean_returns, cov_matrix, num_portfolios=10000):
    results = np.zeros((3, num_portfolios))
    weights_record = []

    for i in range(num_portfolios):
        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)
        weights_record.append(weights)

        portfolio_return, portfolio_std = portfolio_performance(weights, mean_returns, cov_matrix)
        results[0, i] = portfolio_std
        results[1, i] = portfolio_return
        results[2, i] = (portfolio_return - risk_free_rate) / portfolio_std  # Índice de Sharpe

    return results, weights_record

results, weights_record = monte_carlo_simulation(mean_returns, cov_matrix)

max_sharpe_idx = np.argmax(results[2])
sdp, rp = results[0, max_sharpe_idx], results[1, max_sharpe_idx]
max_sharpe_allocation = pd.DataFrame(weights_record[max_sharpe_idx], index=returns.columns, columns=['allocation'])
max_sharpe_allocation['allocation'] = [round(i * 100, 2) for i in max_sharpe_allocation['allocation']]
print(max_sharpe_allocation)

plt.figure(figsize=(10, 7))
plt.scatter(results[0, :], results[1, :], c=results[2, :], cmap='YlGnBu', marker='o')
plt.colorbar(label='Sharpe Index')
plt.scatter(sdp, rp, marker='*', color='r', s=200, label='Max Sharpe Portfolio')
plt.xlabel('Risk')
plt.ylabel('Expected Return')
plt.title('Markowitz Portfolio')
plt.legend(loc='best')
plt.grid(True)
plt.show()
