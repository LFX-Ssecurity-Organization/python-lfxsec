
import requests
import flask
import django
#slave

password = "api123"
secret = "api"
apikey = "test123"

resp = requests.get("https://ipinfo.io")

print(resp.json())
