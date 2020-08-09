import pandas as pd
import numpy as np
import preprocess as pre
from stocks import tickers

cols = ["Date", "Open", "High", "Low", "Close", "Volume", "Name"]
names = tickers


def detrend():
    df = pre.preprocess()

    # detrends each stock time series using the difference method
    for n in names:
        df[n] = df[n].diff()

    return df


if __name__ == "__main__":
    detrend()
