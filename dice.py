import random as ran
import plotly.figure_factory as pff
list=[]
for i in range(1,101):
    dise1=ran.randint(1,6)
    dise2=ran.randint(1,6)
    tolal=dise1+dise2
    list.append(tolal)
graph=pff.create_distplot([list],["dice"],show_hist=False)
graph.show()

    