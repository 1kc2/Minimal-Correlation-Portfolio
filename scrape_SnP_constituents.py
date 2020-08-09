from bs4 import BeautifulSoup
import csv
from os import mkdir
from os.path import exists, join
import urllib.request as request


datadir = "data"
if not exists(datadir):
    mkdir(datadir)

if not exists("tmp"):
    mkdir("tmp")

source = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
cache = join("tmp", "List_of_S%26P_500_companies.html")


def retrieve():
    request.urlretrieve(source, cache)


def extract():
    source_page = open(cache).read()
    soup = BeautifulSoup(source_page, "html.parser")
    table = soup.find("table", {"class": "wikitable sortable"})

    # Fail now if we haven't found the right table
    header = table.findAll("th")
    if header[0].text.rstrip() != "Symbol" or header[1].string != "Security":
        raise Exception("Can't parse Wikipedia's table!")

    # Retrieve the values in the table
    records = []
    symbols = []
    rows = table.findAll("tr")
    for row in rows:
        fields = row.findAll("td")
        if fields:
            symbol = fields[0].text.rstrip()
            # fix as now they have links to the companies on WP
            name = fields[1].text.replace(",", "")
            sector = fields[3].text.rstrip()
            records.append([symbol, name, sector])
            symbols.append(symbol)
    return symbols


def get_constituents():
    retrieve()
    return extract()


if __name__ == "__main__":
    get_constituents()