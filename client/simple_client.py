import requests
import httpx

# Using requests
params = {"who": "Dad"}
r = requests.get("http://localhost:8000/hi", params=params)
r.json()

r = requests.post("http://localhost:8000/hi", json={"who": "Mom"})
r.json()



# Using httpx
rx = 