import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://www.renfe.com/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")