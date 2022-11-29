# TrendBot
## Purpose of the project


Create `class` object for analyzing trend of financial time series

###### Function

- `TrendBot('ticker_name').get_data()`: return pandas dataframe by calculating **std,mean price and log return** as column of (_High,Low,Open,Close_)
- `TrendBot('ticker_name').stationarity()`: check if the time series is stationary by using [Augmented Dickey–Fuller test](https://en.wikipedia.org/wiki/Augmented_Dickey%E2%80%93Fuller_test)
- `TrendBot('ticker_name').detrend()`: analyzing signal by detrending series (if any exists) with `scipy` library
- `TrendBot('ticker_name').seasonality()`: plotting autocorrelation 
- `TrendBot('ticker_name').autocorrelation()`:  plotting _ACF plot_ _PACF plot_
- `TrendBot('ticker_name').plott()`: visualizing time series
- `TrendBot('ticker_name').decomposition()`: applying **multiplicative and additive decomposition**
- `TrendBot('ticker_name').summary_stats()` summarize statistics
- `TrendBot('ticker_name').trend()`: calculates Kendall’s tau, a correlation measure for ordinal data. [Kendall-Tau](https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.kendalltau.html)

