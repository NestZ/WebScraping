coding=<cp874>
import requests
pr = "เชียงราย"
ar = "เชียงของ"
tr = "สถาน"
p = pr.encode(encoding='cp874')
a = ar.encode(encoding='cp874')
t = tr.encode(encoding='cp874')
url = "http://www.noplink.com/postcode_t.php?t=" + t + "&a=" + a + "&p=" + p
data = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')
x = soup.find_all("td")[26]

for i in range(2,len(x.find_all("tr")) - 1):
    a = x.find_all("tr")[i]
    count = len(a.find_all("td"))
    for j in range(0,2):
        print a.find_all("td")[j]
