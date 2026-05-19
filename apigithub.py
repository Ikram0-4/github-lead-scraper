from dotenv import load_dotenv
import requests 
import os

load_dotenv()

TOKEN = os.getenv("GitHub_API_KEY")
def searchDev(query):

    response = requests.get(
        "https://api.github.com/search/users",
        headers={"Authorization": f"token {TOKEN}"},
        params={"q": query, "per_page": 10}
    )


    data = response.json()
    return data["items"]

devs = searchDev("cybersecurity location:Paris language:Python")

for dev in devs:
    print(dev["login"], "" ,dev["url"])