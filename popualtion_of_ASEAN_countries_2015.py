import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

asean_countries = {'Brunei Darussalam', 'Cambodia',
                    'Indonesia', 'Laos', 'Malaysia',
                     'Myanmar','Philippines','Singapore',
                     'Thailand', 'Vietnam'}
                     
countires_population_dict = {} 

def fill_countries_population(eachrow):
    """filling countries_population_dict"""
    if eachrow['Region'] in asean_countries and eachrow['Year'] == '2014':
        countires_population_dict[eachrow['Region']] = int(float(eachrow['Population']))

def calculate():
    """Reading csv file and calling fill_countries_population()"""
    with open('data/population-estimates.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            fill_countries_population(eachrow)


def plot():
    """ploting countries and population"""
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
    """Calliing calculate() and plot()"""
    calculate()
    plot()

exicute()
