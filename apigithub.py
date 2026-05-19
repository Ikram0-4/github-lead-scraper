from dotenv import load_dotenv
import requests 
import os
import csv

load_dotenv()

TOKEN = os.getenv("GitHub_TOKEN")
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def searchDev(query):

    response = requests.get(
        "https://api.github.com/search/users",
        headers=headers,
        params={"q": query, "per_page": 10}
    )


    data = response.json()
    return data["items"]

def enrichDev(username):
    response = requests.get(
        f"https://api.github.com/users/{username}",
        headers=headers
    )

    dev = response.json()

    return {
        "login": dev.get("login"),
        "name": dev.get("name"),
        "email": dev.get("email"),
        "company": dev.get("company"),
        "location": dev.get("location"),
        "public_repos": dev.get("public_repos"),
        "profile": dev.get("html_url")
    }

def exportCSV(devs, filename="leads.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=devs[0].keys())
        writer.writeheader()
        writer.writerows(devs)

    print(f"{len(devs)} leads exportés dans {filename}")

devs = searchDev("cybersecurity location:Paris language:Python")
for dev in devs:
    print(dev["login"], "" ,dev["url"])

    leads = [enrichDev(dev["login"]) for dev in devs]
    exportCSV(leads)