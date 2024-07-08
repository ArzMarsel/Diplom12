import json
import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzZmYjc3ZjUtYzg3My00YzE1LWFlODMtNDVkMTY1MGY5MWZmIiwidHlwZSI6ImFwaV90b2tlbiJ9.pZc-OHJmVbdG0GforeTYJS2F_8Cwweh2eIi6OerimCY'
headers = {"Authorization": f"Bearer {token} "}

url = "https://api.edenai.run/v2/image/generation"
payload = {
    "providers": "openai",
    "text": "Пицца 'Пепперони'",
    "resolution": "1024x1024"
}

response = requests.post(url, json=payload, headers=headers)
result = json.loads(response.text)
print(result)