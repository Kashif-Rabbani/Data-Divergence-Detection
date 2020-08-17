import logging
import csv
from datetime import datetime
from SPARQLWrapper import SPARQLWrapper

now = datetime.utcnow().strftime("%Y%m%d-%H:%M:%S")
logging.basicConfig(level=logging.DEBUG, filename="./Wrapper_"+ now +".txt", filemode="a+",format="%(message)s")

sparql = SPARQLWrapper('http://dati.camera.it/sparql')

for iteration in range(0,5000):
	try:
		sparql.setQuery(" SELECT DISTINCT * WHERE { ?s ?p ?o } LIMIT 10000 OFFSET "+str(iteration*10000))

		sparql.setReturnFormat('tsv')	
		result = sparql.query().convert()

		file = open(str(iteration) + '.tsv', 'wb')
		file.write(result)
		file.close()
		logging.info("Success," + now + ",Success")
	except Exception as e:
		now = datetime.utcnow().strftime("%Y%m%d-%H:%M:%S")
		logging.info("Error," + now + "," + str(e))
