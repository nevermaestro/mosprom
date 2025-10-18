def parse():
    print("test")
def grep():
    import json
    import requests
    import wget
    from dadata import Dadata

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

    def total1(new_data, filename):
        with open(filename,"r", encoding="utf-8") as file:
            dataNew = json.load(file)
        dataNew['Название'] = new_data["items"][0]["ЮЛ"]["НаимСокрЮЛ"]
        dataNew['ИНН'] = new_data["items"][0]["ЮЛ"]["ИНН"]
        dataNew['ОГРН'] = new_data["items"][0]["ЮЛ"]["ОГРН"]
        with open(filename,"w", encoding="utf-8") as file:
            json.dump(dataNew, file, indent=4, ensure_ascii=False)


    def total2(new_data, filename):
        with open(filename,"r", encoding="utf-8") as file:
            dataNew = json.load(file)
        dataNew['Название'] = new_data['suggestions'][0]['value']
        dataNew['ИНН'] = new_data['suggestions'][0]['data']['inn']
        dataNew['ОГРН'] = new_data['suggestions'][0]['data']['ogrn']
        with open(filename,"w", encoding="utf-8") as file:
            json.dump(dataNew, file, indent=4, ensure_ascii=False)

    data3 = suggest('7706043263', 'party')
    print(data3)


    print('Название: ' + data3['suggestions'][0]['value'])
    print('КПП: ' + data3['suggestions'][0]['data']['kpp'])
    print('ОГРН: ' + data3['suggestions'][0]['data']['ogrn'])

    # fns('7706043263')
    # fns_egr('7706043263')
    with open('C:/Users/untit/OneDrive/Документы/mosprom/bo',"r", encoding="utf-8") as file:
        data = json.load(file)
    with open('C:/Users/untit/OneDrive/Документы/mosprom/egr',"r", encoding="utf-8") as file:
        data1 = json.load(file)
    print('Название: ' + data1["items"][0]["ЮЛ"]["НаимСокрЮЛ"])
    print('КПП: ' + data1["items"][0]["ЮЛ"]["КПП"])
    print('ОГРН: ' + data1["items"][0]["ЮЛ"]["ОГРН"])

    total1(data1, 'C:/Users/untit/OneDrive/Документы/mosprom/HELP')
    total2(data3, 'C:/Users/untit/OneDrive/Документы/mosprom/HELP')
