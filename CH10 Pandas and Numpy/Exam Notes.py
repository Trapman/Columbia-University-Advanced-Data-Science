#1 Use np.array to create an array to match the sample
ans1 = np.array([[0.34, 1.2, 4.3, 2.2], 
                 [0.35, 1.2, 4.5, 1.8], 
                 [0.38, 1.2, 4.8, 1.7], 
                 [0.35, 1.1, 4.9, 1.2]
                 ])

#2 Find the sum of the entries in this array
ans1.sum()

#3 Find the sum of each COLUMN
# use axis = 1
ans1.sum(axis =1 )

#4 Find the sum of each ROW
# use axis = 0
ans1.sum(axis = 0)

#5 Find the mean of each COLUMN
ans1.mean(axis = 1)

#6 Find the STD of each COLUMN
ans1.std(axis=1)

#7 Array Indexing
# slice the last row of this array
ans1[-1, :]  #or simple ans1[-1]

#8 Mutliply Array
# multiply your array by 1.03
ans8 = ans1*1.03

#9 Identity Matrix
# matrix with diag element = 1, and 0 otherwise
# use np.identity()
ans9 = np.identity(ans1.shape[0])

#10 Transpose
# use .T
ans10 = ans1.T

#11 Dot Product
# this is the sum of the products of the corresponding entries of the two arrays
# save the results of the dot product of the array ans1 with the
# identity of itself to ans11
# use np.dot()
ans11 = np.dot(ans1.shape[0])

#12 Pandas and Time Series
# uses tickers.csv from data/ folder
stocks = pd.read_csv('data/tickers.csv', index_col = 0)
stocks.head()
# use describe() to get some descriptive stats on stocks df
ans12 = stocks.describe()

#13 .memory_usage
ans13 = stocks.memory_usage()

#14 .pct_change()
# use this to generate a new df with the % change for each ticker
ans14 = stocks.pct_change()

#15 .pct_change(n)
# the default period is one day, let's change this to a weekly (5 days) % change
ans15=stocks.pct_change(5)

#16 .rolling()
# compute the rolling mean within a 20 day window
ans16 = ans1.rolling(20).mean()

#17 pct_change() function
'''
Now, let's combine our percent change calculation to create a new column that  identifies whether or not a stock had a positive or negative percent change. 
You must first write a function called up_or_down that takes in a dataframe object and returns a dataframe object whose values are a count of the periods, by column, of positive percent change.
'''
def up_or_down(series):
    return series.pct_change().apply(lambda x: np.where(x>0, 1, 0)).sum()

ans17 = up_or_down(pd.read_csv('data/tickers.csv', index_col=0))

#18 .corr()
#examine the correlation between percent change in ticker symbols
ans18 = stocks.pct_change().corr()

#19 .corr function
'''
sing the assumption that correlated stocks are not good to have in a single portfolio, determine whether there are any symbol(s) you should drop if you own tan.

Using the .corr() dataframe on percent change, determine if any symbols correlation with tan is above 0.5. Save the symbols as set of strings below, i.e. {'cmg', 'flsr'}
'''
def stocks_to_drop_ans(df, stock='tan'):
    s = df.pct_change().corr()[stock] > 0.5
    return set([ x for x in list(s[s == True].index) if x != stock])

ans19 = stocks_to_drop_ans(pd.read_csv('data/tickers.csv', index_col=0))

