import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

years = []
population = []

def fill_india_population(eachrow):
    ''' 
    Function that fills the population over the years
    '''
    if str(eachrow['Region']).upper() == 'INDIA':
        years.append(eachrow['Year'])
        population.append(int(float(eachrow['Population'])))
        
        


def calculate():
    """
    Function That reads the csv file and calls fill_india_population() s
    """
    with open('data/population-estimates.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            fill_india_population(eachrow)

def plot():
    """
    Function that plots the graph between years and population
    """
    plt.title('India Population Over the Years')
    plt.xlabel('Years')
    plt.ylabel('Population')
    
    plt.bar(years, population ,width=0.4 ,align='edge')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    
    

def exicute():
    """
    FUnction that exicutes the calculate() plot() function
    """
    calculate()
    plot()

exicute()
print(years)
print(population)