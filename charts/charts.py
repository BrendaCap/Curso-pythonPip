import matplotlib.pyplot as plt

#file to execute on terminal and file(png) saved on folder charts(VScode)
def generate_pie_charts():
    labels = ['a','b','c']
    values = [200,34,120]

    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png') #guarda grafica en archivo de tipo png
    plt.close()