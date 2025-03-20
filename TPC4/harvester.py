import json 
import requests
from query import query_graphdb

filmes = []

with open("filmes.json") as f: 
    filmes = json.load(f)

endpoint = "https://dbpedia.org/sparql"

dataset = []
for d in filmes: 

    sparql_query = f""" 

        select distinct ?nome ?abs ?dataLan ?pais ?realizador where {{
        <{d}> dbo:abstract ?abs .
        <{d}>  rdfs:label ?nome.
        OPTIONAL {{ <{d}> dbo:releaseDate ?dataLan. }}
        OPTIONAL {{ <{d}>  dbp:country ?pais .}}
        OPTIONAL {{ <{d}>  dbp:director ?realizador .}}
        filter (lang (?abs) = "en").
        filter (lang (?nome) = "en").
        }} 
    """
    result = query_graphdb(endpoint,sparql_query)

    sparql_query2 = f"""

    select distinct ?ator ?nome ?dn ?origem where {{
        <{d}> dbo:starring ?ator . 
        ?ator a dbo:Person .       
        ?ator foaf:name ?nome .
        ?ator dbo:birthDate ?dn .
        ?ator dbp:birthPlace ?origem .    

        }} 


    """ 
    
    print(result)
    result2 = query_graphdb(endpoint,sparql_query2)
    print(result2)
    atores = []
    if 'results' in result and 'bindings' in result['results'] and len(result['results']['bindings']) > 0:
        bindings = result['results']['bindings'][0]
        
        titulo = bindings.get('nome', {}).get('value', 'Desconhecido')
        sinopse = bindings.get('abs', {}).get('value', 'Sem sinopse disponível')
        data_lancamento = bindings.get('dataLan', {}).get('value', 'Data desconhecida') 
        pais = bindings.get('pais', {}).get('value', 'Pais Desconhecido')
        realizador = bindings.get('realizador', {}).get('value', 'Realizador Desconhecido')

    else:
        titulo, sinopse, data_lancamento, pais, realizador = "Desconhecido", "Sem sinopse disponível", "Data desconhecida", "Pais Desconhecido", "Realizador Desconhecido"
    
    if 'results' in result2 and 'bindings' in result2['results']:
        for a in result2['results']['bindings']:
            atores.append({
                "id": a.get('ator', {}).get('value', 'Desconhecido'),
                "nome": a.get('nome', {}).get('value', 'Nome desconhecido'),
                "data_nascimento": a.get('dn', {}).get('value', 'Desconhecido'),
                "naturalidade": a.get('origem', {}).get('value', 'Desconhecido')
            })
    
    dataset.append({
        "id": d, 
        "titulo": titulo,
        "sinopse": sinopse,  
        "data_Lancamento": data_lancamento, 
        "pais_origem" : pais,
        "realizador": realizador,  
        "atores": atores
    })
    
    

with open ("dataset.json", "w") as fout: 
    json.dump(dataset,fout)