import pandas as pd
import plotly.figure_factory as pff
df= pd.read_csv("C:/Users/mhrat/OneDrive/Desktop/python/c108/data.csv")
weight=df["Weight(Pounds)"].tolist()
graph=pff.create_distplot ([weight],["weight graph"],show_hist=False)
graph.show()
