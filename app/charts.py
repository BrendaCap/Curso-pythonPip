#modulo
import matplotlib.pyplot as plt

#ax: coordenadas
#fig: figura
def generate_bar_chart(name,labels,values):
  '''labels = ['a','b','c'] #son necesarios para graficar
  values = [100,200,80] #son necesarios para graficar'''   
  fig, ax = plt.subplots()
  ax.bar(labels,values) #graficar datos, generando 1 graf de barras
  #plt.show() detiene el programa
  plt.savefig(f'./img/{name}.png') #guarda grafica en archivo de tipo png
  plt.close()

def generate_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')#centra la grafica
  #plt.show()
  plt.savefig('pie.png') #guarda grafica en archivo de tipo png
  plt.close()

if __name__ == '__main__':
  labels = []
  values = []
  generate_bar_chart(labels,values)
  #generate_pie_chart(labels,values)