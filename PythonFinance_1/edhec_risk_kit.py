import pandas as pd

def drawdowns(return_series: pd.Series): #it is to be expected a pd series
    """
    Takes a timeseries of asset returns
    computes and returns a DataFrame that contains:
    the wealth index 
    the previous peaks
    percent drawdowns
    """
    wealth_index=1000*(1+return_series).cumprod()
    previous_peaks=wealth_index.cummax()
    drawdowns=(wealth_index-previous_peaks)/previous_peaks
    return pd.DataFrame({
        "Wealth": wealth_index,
        "Peaks": previous_peaks,
        "Drawdowns":drawdowns
    })

def get__ffme_returns():
    """
    Load the Fama-French Dataset for the returns of the Top and Bottom Deciles by MarketCap
    """
    me_m=pd.read_csv("Portfolios_Formed_on_ME_monthly_EW.csv", 
              header=0, index_col=0, parse_dates=True, na_values=-99.99)
    rets=me_m[['Lo 10', 'Hi 10']]
    rets.columns=['SmallCap', 'LargeCap']
    rets=rets/100
    rets.index=pd.to_datetime(rets.index,format="%Y%m").to_period('M')
    return rets