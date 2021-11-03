import requests
URL='https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=USD'
def get_values():
    response = requests.get(URL)
    if response.status_code == 200:
        request=response.json()
        # print(request)
        bitcoin=request['BTC']['USD']
        ether=request['ETH']['USD']
        litecoin=request['LTC']['USD']
        
    else:
        print('ERROR')
    
    return [bitcoin, ether, litecoin]

