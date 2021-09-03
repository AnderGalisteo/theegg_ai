"""
Lo primero que hace el programa es descargarse todos los datos de:
https://datos.gob.es/catalogo/a16003011-evolucion-del-coronavirus-covid-19-en-euskadi1
"""

import requests 
import json
import numpy as np
import matplotlib.pyplot as plt

def moving_average(N,mylist):

    cumsum, moving_aves = [0], []

    for i, x in enumerate(mylist, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave)
    return moving_aves


def plot_by_sex(date,values,N,xlabeltext,ylabeltext,titletext,saveloc,variables):
    plt.figure(figsize=(10,6), tight_layout=True)#plotting
    for value,variable in zip(values,variables):
        plt.plot(moving_average(N,value), '-', linewidth=2, label=variable)#customization
    xtick_freq = 14
    plt.xticks(range(0,len(moving_average(N,value)),xtick_freq), date[0:len(moving_average(N,value)):xtick_freq], rotation = '45')
    plt.xlabel(xlabeltext)
    plt.ylabel(ylabeltext)
    plt.title(titletext)
    plt.savefig(saveloc)

def get_data_and_plot_for_variable(N,xlabeltext,url,variables):
    response = requests.get(url)
    response_fixed = json.loads(response.content.decode('iso-8859-1').encode('utf8'))


    
    values = []
    date = []
    for variable in variables:
        value = []
        value1 = []
        for element in response_fixed[variable]:
            date.append(element["date"][0:10])
            value.append(element["value"])
        values.append(value)

    plot_by_sex(date,values,N,'Fecha',xlabeltext,xlabeltext + '','tarea_26/images/' + xlabeltext + '_por_sexo_MA_' + str(N) + '.pdf',variables)


if __name__ == "__main__":
    print("Hello world")

    get_data_and_plot_for_variable(7,'Positivos','https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-pcr-positives.json',["menCountByDate","womenCountByDate"])
    get_data_and_plot_for_variable(7,'Muertos','https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-deceasedPeopleCount.json',["deceasedCountByDate"])