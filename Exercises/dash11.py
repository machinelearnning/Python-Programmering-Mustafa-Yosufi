
import pandas as pd 
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go 

import seaborn as sns
df = sns.load_dataset("titanic")
df.info()