#lee un csv(archivo con datos)
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data)) #filtra los paises por continente
  
  countries = list(map(lambda x : x['Country/Territory'],data))
  percentages = list(map(lambda x : x['World Population Percentage'],data))
  charts.generate_pie_chart(countries,percentages)

  country = input('type country: ')

  result = utils.my_population_country(data,country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels,values)

if __name__ == '__main__':
  run()

'''def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Ingresa un pais: ')
  
  result = utils.my_population_country(data, country)

  if len(result) > 0:
    country = result[0] #se envia pais
    labels, values = utils.get_population(country)
    #print(keys, values)
    charts.generate_bar_chart(labels,values)

if __name__ == '__main__':
  run()

keys, values = utils.my_population()
print(keys, values)

data = [
  {
    'Country': 'Mexico',
    'Population': 500
  },
  {
    'Country': 'Colombia',
    'Population': 700
  },
  {
    'Country': 'Argentina',
    'Population': 300
  }
]

def run():
  country = input('Ingresa un pais: ')
  
  result = utils.my_population_country(data, country.lower())
  print(result)

#la dualidad de un modulo sig: poder mandarlo a llamar desde un archivo o llamarlo desde la consola
si main.py se quiere ejecutar desde la consola(como un script), esta linea lo hara posible, python app/main.py '''

