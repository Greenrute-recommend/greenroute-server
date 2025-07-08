import requests

url = "https://greenroute-server.onrender.com/recommend"
data = {
    "day": "금요일",
    "weather": "맑음",
    "location": "서울",
    "schedule": "외출",
    "completed": []
}

response = requests.post(url, json=data)
print(response.json())
