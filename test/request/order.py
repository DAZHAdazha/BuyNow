import requests

url = "https://dazhadazha.pythonanywhere.com//cart.html"

payload={'data': '{"products": [{"id": 3, "name": "Digital Camera", "price": 200, "quantity": 3, "sum": 600}, {"id": 2, "name": "Protable Speakers", "price": 200, "quantity": 2, "sum": 400}], "total": 1030, "product_sum": 5}'}
files=[

]
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
