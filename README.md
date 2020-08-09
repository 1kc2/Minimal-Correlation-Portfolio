This project is a portfolio selection algorithm that address some of the shortcomings of the efficient frontier model of modern portfolio theory (MPT). The algorithm is designed to handle historical time series of unequal dimensions and detect non-linear associations between assets, enabling optimization across asset classes with sparse data.

# Usage

First, it necessary to collect the relevant data for the candidate stocks in consideration by running `data_collector.py`. This will collect OHLC data from Yahoo and store it in the `data` directory in an individual file for each symbol. Additionlly, a file is created in the root directory which collates the data for each symbol into a singular file.

Then run the scripts from the terminal with

```
python3 {filename}.py
```

For example
```
python plot_correlation_network.py
```

will plot a time series correlation network using the data in the repository.

# Dependencies

A comprehensive list of current dependencies include the following libraries

```
Pandas (data manipulation)
Numpy (scientific computing)
Scipy (statistical computing)
dcor (energy statistics)
NetworkX (graph analytics)
Matplotlib (plotting)
Seaborn (plotting)
pypfopt (portfolio optimization)
datetime (dates & times)
```
# Context

## Wrestling with Imperfect Data

By selecting assets whose pairwise correlations are minimal, in theory, an optimal allocation that yields superior risk-adjusted returns can be obtained. The difficulty of this approach is that the correlations are non-stationary (e.g., see the [Financial 15 Index of South Africa](http://www.turingfinance.com/wp-content/uploads/2014/09/financial-fifteen-correlations.png)) and are known to harbor non-linear effects ([Haluszczynski, 2017](https://arxiv.org/pdf/1712.02661.pdf); [Hsieh, 1995](https://faculty.fuqua.duke.edu/~dah7/faj1995.pdf)). To make matters worse financial data is incredibly sparse. While there's plenty of historical data for stocks, the same can't be said, for example, of fixed income or alternative assets. In practice, and more often than not, quantitative analysts face the problem of estimating correlations between time series of unequal dimension.

There are two types of missing data in financial time series: periodically missing values and entirely missing trajectories (i.e. time series that end abruptly). In the case where most of the assets have missing trajectories, and hence replacing their missing values becomes a problem of forecasting. Pearson's correlation coefficient is of no help here since it:
- only captures linear associations in the data,
- only works for time series of equal dimension.

## A Network-based Approach

There's been accumulating evidence that asset correlation networks follow a power-law degree distribution, which roughly means only a few nodes are weakly correlated with the rest of the network ([Tse, et al. 2010](http://cktse.eie.polyu.edu.hk/pdf-paper/JoEF-1009.pdf); [Boginski, et al. 2005](https://www.sciencedirect.com/science/article/pii/S0167947304000258)). An asset correlation network is a graph whose nodes are assets and whose edges are the pairwise correlations between the assets' historical time series (usually taken as the daily closing prices or logarithmic returns). The emergence of complex networks and the study of their fundamental organizing principles have garnered significant attention from the scientific community, large in part from the seminal works of Albert Barabasi that show most of these networks are governed by simple "scale-free" laws. Forecasting financial time series is known to be [notoriously difficult](https://towardsdatascience.com/3-facts-about-time-series-forecasting-that-surprise-experienced-machine-learning-practitioners-69c18ee89387), but perhaps forecasting the evolution of asset correlation networks isn't? If asset correlation networks are driven by simple laws, then it's reasonable to assume these laws can be learned by a single ML algorithm (as opposed to learning a model for each time series). What's more, these observations suggest the degree distribution of asset correlation networks are stationary, further suggesting the selected ML model need only be trained once (as opposed to continuously).

## Communicability of Complex Networks

In the case of an asset correlation network, we're interested in how volatility spreads between assets and how we can act on such insights to optimize our portfolio. For example, suppose Apple suddenly loses 40% of its value, wiping out, say, two years of explosive gains. How would this highly volatile event ripple throughout our portfolio? Which of our assets would bear the brunt of the impact? Which would parry it unscathed? To this end, the aim is to build a portfolio selection algorithm that can ingest imperfect data, anticipate changes in an asset correlation network, and predict how volatility propagates asset to asset.