__author__ = "Satish Palaniappan"

import pickle
from bs4 import BeautifulSoup
import urllib.request
import urllib
from urllib.request import Request, urlopen

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f,  protocol=2)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

with urllib.request.urlopen("http://www.netlingo.com/acronyms.php") as url:
    html_doc = url.read().decode("utf-8")
    soup = BeautifulSoup(html_doc)

    box = soup.find_all("div", "list_box3")[0]

    abrr = dict()

    for item in box.ul.find_all("li"):
        print(item.contents)
        if len(item.contents) < 2:
            continue
        data = item.contents[1].strip()
        data = data.replace("-or-", "")
        data = data.replace(",", "")
        data = data.replace("it means", "")
        data = data.lower().strip()
        abrr[item.span.a.get_text().lower()] = data

        save_obj(abrr, "acronymsDict")

# Test
for a in abrr.keys():
    print(a + " : " + abrr[a])
