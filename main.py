from dotenv import load_dotenv
import os
import requests

topic = input("Enter topic you are interested in: ")

load_dotenv()
news_api_key = os.getenv("NEWS_API_KEY")
#
url = (f"https://newsapi.org/v2/everything?q={topic}&from=2026-10-14&"
       f"apiKey={news_api_key}")
response = requests.get(url)
data = response.json()

for article in data["articles"]:
    print(article["title"])
    print(article["description"])
