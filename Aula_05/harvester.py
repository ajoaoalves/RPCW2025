import json 
import requests
from query import query_graphdb

desportos = []

with open("desportos.json") as f: 
    desportos = json.load(f)

endpoint = "https://dbpedia.org/sparql"

dataset = []
for d in desportos: 

    sparql_query = f""" 

        select distinct ?nome ?abs where {{
        <{d}> dbo:abstract ?abs .
        <{d}>  rdfs:label ?nome.
        filter (lang (?abs) = "en").
        filter (lang (?nome) = "en").
        }} 
    """
    result = query_graphdb(endpoint,sparql_query)

    sparql_query2 = f"""

    select distinct ?atleta ?nome ?origem ?dataNasc where {{
        ?atleta a schema:Person.
        ?atleta dbp:sport  <{d}> .
        ?atleta dbp:name ?nome . 
        ?atleta dbp:nationality ?origem . 
        ?atleta dbo:birthDate ?dataNasc . 



        }} 


    """ 
    
    print(result)
    result2 = query_graphdb(endpoint,sparql_query2)
    print(result2)
    atletas = []
    print
    for a in result2 ['results']['bindings']:
        atletas.append({

            "id" : a['atleta']['value'], 
            "nome" : a['nome']['value'], 
            "origem" : a['origem']['value'], 
            "dataNasc" :a['dataNasc']['value']

        })

    dataset.append(
        {
            "id": d, 
            "designacao" : result['results']['bindings'][0]['nome']['value'],
            "abs":result['results']['bindings'][0]['abs']['value']   ,  
            "atletas": atletas
                  }
    )


with open ("dataset.json", "w") as fout: 
    json.dump(dataset,fout)