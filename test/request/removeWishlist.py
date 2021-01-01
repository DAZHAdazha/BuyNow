import requests

url = "https://dazhadazha.pythonanywhere.com//removeWishlist"

payload={'product_id': '3'}
files=[

]
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
