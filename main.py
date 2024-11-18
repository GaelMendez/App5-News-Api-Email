import requests
import os
import functions
from send_email import send_email

api_key = os.getenv("APIKEY")

params = {
"language": "en"
}

# Make request
request = requests.get(functions.get_url(),params)

# Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"]:
      body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)


