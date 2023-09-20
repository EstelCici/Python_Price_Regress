pip install yfinance

import yfinance as yf
import statsmodels.formula.api as smf
import pandas as pd

stocks = ['TSLA','^GSPC']

D = yf.download(stocks, start='2022-9-15', end='2023-9-15')

P = D['Adj Close']

Returns = P/P.shift(1) - 1

R = P.pct_change()

R2 = R.tail(100)

R2.rename(columns = {'^GSPC':'SnP'},inplace=True)

mystocks = R.columns[:1]

mystocks

betalist = []

for mystock in mystocks:
  myformula = mystock + " ~ SnP"
  print(myformula)
  results = smf.ols(formula = myformula, data = R2).fit()
  print(results.params['SnP'])
  betalist.append(results.params['SnP'])


