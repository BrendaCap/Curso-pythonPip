#modulo
#lee el csv y lo tranforma en un diccionario
import csv

#reader: lector
#delimiter: forma en que se separan los datos
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = [] #lista q contendra datos en diccionarios
    for row in reader: #iteracion de los datos
      iterable = zip(header,row) #header,row[5:12]
      country_dict = {key: value for key, value in iterable} #une columna con fila 
      data.append(country_dict) #agrega cada dato a la lista 
    return data

#eejcutar como script desde la consola
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])

#posicion[5] : 8 populaciones