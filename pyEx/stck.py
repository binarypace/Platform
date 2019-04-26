import datetime as dt
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib notebook
import matplotlib as mpl  

import pandas as pd
#from matplotlib import style
#import pandas as pd 
from pandas_datareader import data as web


#mpl.use('TkAgg')
#style.use('ggplot')
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("NASDAQ:FB", 'google', start, end) 
df.reset_index(inplace=True) 
df.set_index("Date", inplace=True) 
df = df.drop("Symbol", axis=1) 
print(df.head())

