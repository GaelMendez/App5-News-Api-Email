import requests

api_key = "bc9de7877a3f455284a043fa0f3a14f9"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-10-18&sortBy=publishedAt&apiKey=" \
      "bc9de7877a3f455284a043fa0f3a14f9"

request = requests.get(url)
content = request.text
print(content)
