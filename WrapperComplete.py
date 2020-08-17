import csv
import logging
from datetime import datetime
from SPARQLWrapper import SPARQLWrapper

now = datetime.utcnow().strftime("%Y%m%d-%H:%M:%S")
logging.basicConfig(level=logging.DEBUG, filename="./Wrapper_"+ now +".txt", filemode="a+",format="%(message)s")


with open ("./DownloadEndpoints.txt") as download:
	records = csv.reader(download)
	formats = ['tsv', 'csv', 'json', 'xml', 'turtle', 'n3', 'rdf', 'rdf+xml']
	for line in records:
		sparql = SPARQLWrapper(line[1])
		try:
			sparql.setQuery(""" SELECT DISTINCT * WHERE { ?s ?p ?o } """)

			validFormat = False
			availableFormat = ''
			i = 0
			while (validFormat == False and i < 9):
				validFormat = sparql.supportsReturnFormat(formats[i])
				availableFormat = formats[i]
				i = i + 1

			sparql.setReturnFormat(availableFormat)
			result = sparql.query().convert()

			file = open(line[0] + '.' + availableFormat, 'wb')
			file.write(result)
			file.close()
			logging.info(line[0] + "," + now + ",Success")
		except Exception as e:
			now = datetime.utcnow().strftime("%Y%m%d-%H:%M:%S")
			logging.info(line[0] + "," + now + "," + str(e))
