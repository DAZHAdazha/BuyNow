import requests

url = "https://dazhadazha.pythonanywhere.com//search?q=phone"

payload={}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
