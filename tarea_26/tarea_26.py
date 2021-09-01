"""
Lo primero que hace el programa es descargarse todos los datos de:
https://datos.gob.es/catalogo/a16003011-evolucion-del-coronavirus-covid-19-en-euskadi1
"""

import requests 
import json
import io

if __name__ == "__main__":
    print("Hello world")

    response = requests.get('https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-pcr-positives.json')
    records = json.loads(response.content.decode('iso-8859-1').encode('utf8'))

    
    #print(records)
    print(json.dumps(records, indent=1))

