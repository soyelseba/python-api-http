import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://api.weatherapi.com/v1/current.json"
token = f"?key={os.getenv("token")}"
ciudad = f"&q={input("Ciudad a consultar: ")}"

res = requests.get(url=url+token+ciudad)

print(res.json())