import requests
import csv
listOfItem=requests.get("https://raw.githubusercontent.com/spiritbro1/scraped-devshop/master/devto.csv")
devtoCsv=None
with open(listOfItem.text) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    devtoCsv=list(csv_reader)