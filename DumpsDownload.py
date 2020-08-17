import requests
import csv

with open ("./DumpEndpoints.txt") as download:
    records = csv.reader(download)
    for line in records:
        url = line[1]
        if url.find('/'):
            name = url.rsplit('/', 1)[1]
        try:
            r = requests.get(url, allow_redirects=True)
            file = open(line[0]+ name, 'wb').write(r.content)
            file.close()
        except:
            print("Error with:" + line[0])