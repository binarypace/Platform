import requests
import re
import json
import time as time

def inicio():
    nombre = 'FB'
    inicial = '2017-9-1'
    final = '2018-12-31'

    start = int(time.mktime(time.strptime(str(inicial), '%Y-%m-%d'))) # convertir fechas
    end = int(time.mktime(time.strptime(str(final), '%Y-%m-%d')))

    abc = descargar(nombre,start,end)
    abc = abc.decode('utf-8')

    with open('{}.csv.'.format(nombre), "w") as salida:
        salida.writelines(str(abc))


def descargar(symbol, start, end):
    ses = requests.session()
    resp = ses.get(
        f'https://finance.yahoo.com/quote/{symbol}/history?period1={start}&period2={end}&interval=1d&filter=history&frequency=1d')
    resp.raise_for_status()
    data = resp.content.decode('utf-8')
    crumb_m = re.search(r'"CrumbStore":\{"crumb":("[^"]+")\}', data)
    assert crumb_m
    crumb = json.loads(crumb_m.group(1))
    csvresp = ses.get(
        f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={start}&period2={end}&interval=1d&events=history&crumb={crumb}'
    )
    csvresp.raise_for_status()
    #print(type(csvresp))
    return csvresp.content


if __name__=="__main__":
    inicio()
