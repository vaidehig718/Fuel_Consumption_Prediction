import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sketch 
import plotly.express as px
import tensorflow as tf
import autokeras as ak
from dataprep.eda import plot, plot_correlation
%matplotlib inline 
pd.set_option('display.max_columns', 50)

df = pd.read_csv('/kaggle/input/fuel-concumption-ratings-2023/Fuel Consumption Ratings 2023.csv', encoding='latin-1', low_memory=False, dtype={'Vehicle Class':'category', 'Transmission':'category', 'Fuel Type':'category'})
df.dropna(inplace=True)



