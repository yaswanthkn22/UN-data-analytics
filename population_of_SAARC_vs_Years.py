import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')


saarc_countries = {'Afghanistan','Bangladesh','Bhutan','India','Maldives','Nepal','Pakistan','Sri Lanka'}

saarc_country_population = {}


def fill_countries_population(eachrow):

    if eachrow['Region'] in saarc_countries:

        if eachrow['Year'] in saarc_country_population:

            saarc_country_population[eachrow['Year']] += int(float(eachrow['Population']))
        else :
            saarc_country_population[eachrow['Year']] = int(float(eachrow['Population']))
    





def calculate():

    with open('data/population-estimates.csv') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            fill_countries_population(eachrow)


def plot():

    years = []
    population = []
    
    for year , count in saarc_country_population.items():

        years.append(year)
        population.append(count)
    x_axis = np.arange(len(years))
    plt.title('SAARC Countries Population over the Years')
    plt.xlabel("Years")
    
    plt.ylabel('Population')
    plt.bar(x_axis, population )
    plt.xticks(x_axis,years)
    plt.tight_layout()
    plt.show()

def exicute():
    calculate()
    plot()

exicute()

