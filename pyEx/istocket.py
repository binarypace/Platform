# Import initial libraries

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objs as go
#%matplotlib inline


#%matplotlib notebook

import matplotlib.pyplot as plt

# Imports in order to be able to use Plotly offline.
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__) # requires version >= 1.9.0

init_notebook_mode(connected=True)

# Import the Sample worksheet with acquisition dates and initial cost basis:

portfolio_df = pd.read_excel('Sample stocks acquisition dates_costs.xlsx', sheetname='Sample')

portfolio_df.head(10)

