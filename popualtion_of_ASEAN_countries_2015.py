import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

asean_countries = {'Brunei', 'Cambodia','Indonesia', 'Laos', 'Malaysia', 'Myanmar','Philippines','Singapore','Thailand', 'Vietnam'}
countires_population_dict = {} 

def fill_countries_population(eachrow):

    if eachrow['Region'] in asean_countries and eachrow['Year'] == '2014':
        countires_population_dict[eachrow['Region']] = int(float(eachrow['Population']))

def calculate():

    with open('data/population-estimates.csv') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            fill_countries_population(eachrow)


def plot():

    countries = []
    population = []
    
    for country , count in countires_population_dict.items():

        countries.append(country)
        population.append(count)
    
    plt.title('ASEAN Countries Population in 2014')
    plt.xlabel("Countires")
    plt.ylabel('Population')
    plt.bar(countries, population)
    plt.tight_layout()
    plt.show()

def exicute():
    calculate()
    plot()

exicute()
