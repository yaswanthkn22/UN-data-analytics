import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

years = []
population = []

def fill_india_population(eachrow):

    if str(eachrow['Region']).upper() == 'INDIA':
        years.append(eachrow['Year'])
        population.append(int(float(eachrow['Population'])))
        
        


def calculate():
    with open('data/population-estimates.csv') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            fill_india_population(eachrow)

def plot():
    plt.title('India Population Over the Years')
    plt.xlabel('Years')
    plt.ylabel('Population')
    
    plt.bar(years, population ,width=0.4 ,align='edge')
    plt.tight_layout()
    plt.show()
    
    

def exicute():
    calculate()
    plot()

exicute()
print(years)
print(population)