import pandas as pd
import plotly.figure_factory as pff
df= pd.read_csv("C:/Users/mhrat/OneDrive/Desktop/python/c108/data.csv")
hieght=df["Height(Inches)"].tolist()
graph=pff.create_distplot([hieght],["Hieght Graph"],show_hist=False)
graph.show()

