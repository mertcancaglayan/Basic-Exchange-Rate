
import requests
import json

"""result = requests.get('https://api.exchangerate.host/latest')

data = json.loads(result.text)

currency = input('Lütfen para birimi giriniz: ')

print(f"1 Euro = {data['rates'][currency]} {currency} ")"""


url = 'https://api.exchangerate.host/convert?from='

bozulan = input('Bozmak istediğiniz dövizi giriniz: ')
alınan = input('Almak istediğiniz dövizi giriniz: ')
miktar = int(input(f"Ne kadarlık {bozulan} bozdurmak istiyorsunuz?: "))


response = requests.get(url+bozulan+'&to='+alınan)
data = json.loads(response.text)

no1 = data['info']['rate']

result = no1*miktar
print(f'{miktar} {bozulan} {result} {alınan} yapmaktadır.')
