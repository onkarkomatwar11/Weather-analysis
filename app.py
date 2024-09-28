import requests

url = "http://api.weatherstack.com/current?access_key=b69e40835bb2e01a5053fcd164322df9&query=New York"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
