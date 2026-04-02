import re, urllib.request

url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
data = urllib.request.urlopen(url).read().decode("utf-8")

print(data)