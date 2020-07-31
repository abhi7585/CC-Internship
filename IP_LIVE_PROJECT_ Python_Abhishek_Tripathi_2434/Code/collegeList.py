from bs4 import BeautifulSoup
from urllib.request import urlopen

# Url which we want to scrape
url = "http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=3&RegionName=Mumbai"

uClient = urlopen(url)
HTMLpage = uClient.read()
uClient.close()

soup = BeautifulSoup(HTMLpage, "html.parser")

container = soup.findAll("td", {"class": "Item"})

collegeLinks = []

for i in range(len(container)):
    for link in container[i].findAll('a'):
        if link.get('href') is not None:
            # Creating College URL list
            collegeLinks.append(
                "http://dtemaharashtra.gov.in/" + link.get('href'))


def getLink():
    return collegeLinks
