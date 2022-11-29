import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from statsmodels.tsa.stattools import adfuller
from scipy import signal
from pandas.plotting import autocorrelation_plot
import matplotlib as mpl
import matplotlib.pyplot as plt   
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
import scipy.stats as stats


class TrendBot():
    def __init__(self,ticker) -> None:
        self.ticker = ticker.upper()
  
    def get_data(self):

        df = yf.download(self.ticker,interval='1d',period='max')
        df.drop(['Volume','Adj Close'],axis=1,inplace=True)
        df['std'] = df.std(axis='columns')
        df['mean_price'] = df.mean(axis='columns')
        df['lag_1'] = df['Close'] - df['Close'].shift(1)
        df['log_ret'] = np.log(df['mean_price']).diff()
        
        df.dropna(inplace=True)

        return df
    
    def stationarity(self):
        df = self.get_data()
        if adfuller(df['std'])[1] < 0.5:
            return True,print("{} is stationary".format(self.ticker))
        else: return False

    def detrend(self):
        if self.stationarity():
            df = self.get_data()
            detr = signal.detrend(df['std'].values)
            plt.plot(detr)
            plt.title("{} detrended by subtracting the least squares fit".format(self.ticker), fontsize=16)
            return df['std'].mean(), plt.show()
        else: return False
    
    def seasonality(self):
        df = self.get_data()
        plt.rcParams.update({'figure.figsize':(10,6), 'figure.dpi':120})
        autocorrelation_plot(df['std'].tolist())
        return plt.show()

    def autocorrelation(self):
        df = self.get_data()
        fig, axes = plt.subplots(1,2,figsize=(16,3), dpi= 100)
        plot_acf(df['std'].tolist(), lags=50, ax=axes[0])
        plot_pacf(df['std'].tolist(), lags=50, ax=axes[1])
        return plt.show()

    def plott(self):
        df = self.get_data()
        fig = go.Figure([go.Scatter(x=df.index, y = df['std'])])
        return fig.show()

    def decomposition(self):
        df = self.get_data()
        #multiplicative decomposition
        mult_dec = seasonal_decompose(df['std'],model='multiplicative',period=1)

        #additive decomposition
        add_dec = seasonal_decompose(df['std'],model='additive',period=1)

        #plot
        plt.rcParams.update({'figure.figsize': (14,10)})
        mult_dec.plot().suptitle('Multiplicatiev Decomposition',fontsize=14)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        add_dec.plot().suptitle('Additive Decomposition', fontsize=14)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        return plt.show()

    def summary_stats(self):
        df = self.get_data()
        return print(df['log_ret'].describe())

    def trend(self):
        df = self.get_data()
        x1 = [i for i in range(len(df['std']))]
        tau,p_value = stats.kendalltau(x1,df['std'])
        return "tau is: {} with p value: {}".format(tau,p_value)

print(TrendBot('gld').plott())
print(TrendBot('gld').detrend())