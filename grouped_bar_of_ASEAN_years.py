import csv
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

asean_population_over_years = {}

asean_countries = {'Brunei', 'Cambodia','Indonesia', 'Laos', 'Malaysia', 'Myanmar','Philippines','Singapore','Thailand', 'Vietnam'}

def fill_asean_population_over_years(eachrow):

    if eachrow['Region'] in asean_countries:

        if eachrow['Region'] in asean_population_over_years:
            if int(eachrow['Year']) in range(2004 , 2015):
                asean_population_over_years[eachrow['Region']].append(int(float(eachrow['Population'])))
        else :
            asean_population_over_years[eachrow['Region']] = []
            if int(eachrow['Year']) in range(2004 , 2015):
                asean_population_over_years[eachrow['Region']].append(int(float(eachrow['Population'])))

        


def calculate():

    with open('data/population-estimates.csv') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            fill_asean_population_over_years(eachrow)



def plot ():

    years = [str(j) for j in range(2004, 2015)]
    countries = []

    populations = []

    for country , population in asean_population_over_years.items():
        countries.append(country)
        populations.append(population)
    
    print(countries)
    print(populations)
    x_axis = np.arange(11)
    width = 0.3
    bars = []
    plt.xticks(x_axis , years)
    bar = plt.bar(x_axis , populations[0],width=width,label=countries[0])
    bars.append(bar)
    for i in range(1, len(countries)):
        bar = plt.bar(x_axis, populations[i],width=width,label=countries[i])
        x_axis = [width+j for j in x_axis]
        bars.append(bar)
    plt.legend(bars , countries)
    
    plt.show()

def exicute():
    calculate()
    plot()

exicute()


