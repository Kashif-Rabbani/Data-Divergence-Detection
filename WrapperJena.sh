#!/bin/bash

endpoint=$1

predicatesFile=$2

rm -f ${predicatesFile}

tmpFileA=`mktemp`
tmpFileB=`mktemp`

cd /home/ubuntu/lib/apache-jena-3.16.0/bin

query="SELECT DISTINCT ?s ?p ?o WHERE { ?s ?p ?o }"

(echo $query) > $tmpFileA

./rsparql --service $endpoint --query $tmpFileA --results=TSV > $tmpFileB

tail -n +2 $tmpFileB > $predicatesFile

