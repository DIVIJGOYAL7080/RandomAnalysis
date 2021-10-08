import pandas as pd
import random
import csv
import statistics
import plotly.figure_factory as ff 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()
print("population mean:- ",statistics.mean(data))
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("Sampling mean for the data is :- ", statistics.mean(mean_list))

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

setup()