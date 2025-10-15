import requests
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(response)
response.status_code == requests.codes.ok
True
len(response.text)
178978
print(response.text[:210000])
