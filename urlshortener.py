import pyshorteners

url = "https://youtu.be/WeOa2MABV2g" # Replace with your URL
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(url) # Replace tinyurl with the desired URL shortener service

print(short_url)