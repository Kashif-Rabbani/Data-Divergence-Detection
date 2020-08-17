# An Up-to-Date overview of LOD Cloud

Steps followed to obtain an updated overview of [LOD Cloud.](https://www.lod-cloud.net)
# 

 1. Parse LOD Cloud. Extract endpoints, full_download, and other_download links.
     - First approach: Importing LODCloud to MongoDB and query the database. [LOD Cloud documentation.](https://github.com/lod-cloud/lod-cloud-site)
     - Second approach: Using [JQ](https://stedolan.github.io/jq/). Example:
		> a. jq '.[] | select(.sparql[].access_url?) | [.identifier, .sparql[].access_url, .other_download[].access_url, .full_download[].download_url]' lod-data.json

 2. Evaluate the availability of the endpoints using an [SPARQLES implementation](https://github.com/berezovskyi/sparqles).
 3. Download endpoints which are available. Different approaches:
     - Complete download using Python (WrapperComplete).
     - Offset download in Python (WrapperOffset).
     - Complete download using Jena (WrapperJena).
     - Command line tools. Example:
		> curl 'http:// rdf.muninn-project .org/sparql?query=SELECT+DISTINCT+*+WHERE+%7B+%3Fs+%3Fp+%3Fo+%7D+LIMIT+10000+OFFSET+10000&output=tsv&jsonp=&key=' > 1.tsv
 4. Download dumps:
       - Full download available (DumpsDownload).
       - Other links that are available. Go to the website, look for the dump, and download it manually.
 5. Convert files to TSV, if it is necessary. Example:
	> ./arq --data muziekweb.trig --query query.rq --results tsv > muziekweb.tsv
 6. Run [RDFev](https://gitlab.com/opelgrin/rdfev) in lowdiff mode. Example:
	> ./lowdiff ~/Endpoints/curriculum.tsv ~/Dumps/curriculum.tsv onmemory ~/Comparisons/curriculum.tsv
 7. Tabulate the data and import it to PowerBi.
 8. Build the dashboard.
