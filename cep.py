import requests


def consultar(cep : str):   
    try:
        cep = cep.strip()
        cep = cep.replace(' ', '').replace('-', '').replace('.', '')
        url = 'https://viacep.com.br/ws/%s/json/' % cep
        r = requests.get(url)
        return r.json()
    
    except:
        return 'Erro'
    
