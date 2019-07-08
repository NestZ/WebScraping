# -*- coding: utf-8 -*-
import requests
p = "เชียงราย"
a = "เชียงของ"
t = "สถาน"
url = "http://www.noplink.com/postcode_t.php?t=" + t + "&a=" + a + "&p=" + p
data = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')
x = soup.find_all("td")[26]

for i in range(2,len(x.find_all("tr")) - 1):
    a = x.find_all("tr")[i]
    count = len(a.find_all("td"))
    for j in range(0,2):
        c = a.find_all("td")[j]
        print c.text
