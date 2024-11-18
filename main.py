import requests
import os
import functions
from send_email import send_email

api_key = os.getenv("APIKEY")

params = {
"language": "en"
}

topic = "tesla"

# Make request
request = requests.get(functions.get_url(topic),params)

# Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"][:20]:
      body = "Subject: Today's news"\
             + "\n" +body + article["title"] + "\n"\
             + str(article["description"]) + "\n"\
             + article["url"] +2*"\n"

body = body.encode("utf-8")
send_email(message=body)


