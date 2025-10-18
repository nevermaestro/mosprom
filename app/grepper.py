import json
import requests
import wget
import os
from dadata import Dadata
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')
API_KEY1 = os.environ.get('API_KEY1')
BASE_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/'
BASE_URL1 = 'https://api-fns.ru/api/bo'


def suggest(query, resource):
    url = BASE_URL + resource
    headers = {
        'Authorization': 'Token ' + API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    data = {
        'query': query
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)
    return res.json()

def fns_bo(inn):
    url = 'https://api-fns.ru/api/bo?req=' + inn + '&key=' + API_KEY1
    result = wget.download(url)
    return result

def fns_egr(inn):
    url = 'https://api-fns.ru/api/egr?req=' + inn + '&key=' + API_KEY1
    result = wget.download(url)
    return result

def total1(new_data, filename, id):
    with open(filename,"r", encoding="utf-8") as file:
        dataNew = json.load(file)
    dataNew[id]['Выручка предприятия, тыс. руб. 2024'] = new_data[dataNew[id]['ИНН']]["2024"]["2110"]
    with open(filename,"w", encoding="utf-8") as file:
        json.dump(dataNew, file, indent=4, ensure_ascii=False)


def total2(new_data, filename, id):
    with open(filename,"r", encoding="utf-8") as file:
        dataNew = json.load(file)
    dataNew[id]['Наименование организации'] = new_data['suggestions'][0]['value']
    dataNew[id]['ОГРН'] = new_data['suggestions'][0]['data']['ogrn']
    with open(filename,"w", encoding="utf-8") as file:
        json.dump(dataNew, file, indent=4, ensure_ascii=False)

def update(filename):
    with open(filename,"r", encoding="utf-8") as file:
        dataNew = json.load(file)
    j = 0
    for i in dataNew:
        print(dataNew[j]["ИНН"])
        da_data = suggest(dataNew[j]["ИНН"], 'party')
        fns_bo(dataNew[j]["ИНН"])
        fns_egr(dataNew[j]["ИНН"])
        with open('bo',"r", encoding="utf-8") as file:
            data = json.load(file)
        with open('egr',"r", encoding="utf-8") as file:
            data1 = json.load(file)  
        total1(data, filename, j)
        total2(da_data, filename, j)
        os.remove("bo")
        os.remove("egr")
        j = j + 1
    return 200
