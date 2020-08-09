import pandas as pd
import numpy as np
import preprocess as pre
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator
import seaborn as sns

def plot_stocks_timeseries():
    df = pre.preprocess()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    xtick_locator = AutoDateLocator()
    xtick_formatter = AutoDateFormatter(xtick_locator)
    
    # the two stocks to compare
    df["AAPL"].plot()
    df["AMZN"].plot()
    ax.xaxis.set_major_locator(xtick_locator)
    ax.xaxis.set_major_formatter(xtick_formatter)
    plt.show()


if __name__ == "__main__":
    plot_stocks_timeseries()
