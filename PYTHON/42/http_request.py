import http.client
from urllib.request import urlopen, Request

http.client.HTTPConnection.debuglevel = 1


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'

request = Request('https://myaccount.google.com/personal-info', headers={'User-Agent': user_agent})

with urlopen(request) as response:
    data = response.read()


text = data.decode(encoding='UTF-8')

# print(text)
