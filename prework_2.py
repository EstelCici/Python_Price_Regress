pip install yfinance

import yfinance as yf

tickers = ['AAPL','GOOG','TSLA','^GSPC']

D = yf.download(tickers, start='2022-9-15', end='2023-9-15')

P = D['Adj Close']

Returns = P/P.shift(1) - 1

Returns.head()

R = P.pct_change()

R2 = R.tail(100)

R2.columns

R2.rename(columns = {'^GSPC':'SnP'},inplace=True)

R2.tail()

import statsmodels.formula.api as smf
import pandas as pd

results = smf.ols(formula = 'TSLA ~ SnP', data = R2).fit()

results.params

mystocks = R.columns[:3]

betalist = []


for mystock in mystocks:
  myformula = mystock + " ~ SnP"
  print(myformula)
  results = smf.ols(formula = myformula, data = R2).fit()
  print(results.params['SnP'])
  betalist.append(results.params['SnP'])

betalist

import numpy as np
betavec = np.array(betalist)

notional = 100
notional * betavec

sum(notional*betavec)

