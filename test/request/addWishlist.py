import requests

url = "https://dazhadazha.pythonanywhere.com//addWishlist"

payload={'product_id': '1'}
files=[

]
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
