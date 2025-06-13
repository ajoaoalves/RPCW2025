# --------------------------------------------------------------------
# GeraÃ§Ã£o da ontologia para o dataset dos 120 anos dos Jogos OlÃ­mpicos
# 2025-04-10 by jcr
# --------------------------------------------------------------------
# Ontologia base (estrutura) criada Ã  mÃ£o no ProtÃ©gÃ©
# --------------------------------------------------------------------
import csv
import re
import json
from rdflib import Graph, Namespace, URIRef, RDF, OWL, Literal
# --------------------------------------------------------------------
# Carregar a ontologia base para o grafo em memÃ³ria
# --------------------------------------------------------------------

with open("realeza_pt.json", "r", encoding="utf-8") as f:
    data = json.load(f)

n = Namespace("http://www.semanticweb.org/ajr/ontologies/2025/realeza#")
g = Graph()
g.parse("realeza_pai_mae.ttl")

maes = []

pais = set()


for i,dinastia in enumerate(data):
    dinastiaURI = URIRef(f"{n}Dinastia_{i+1}")
    g.add((dinastiaURI, RDF.type, OWL.NamedIndividual))
    g.add((dinastiaURI, RDF.type, n.Dinastia))
    g.add((dinastiaURI, n.nome, Literal(dinastia)))


    for rei in data[dinastia]:
        reiURI = URIRef(f"{n}{rei['nome'].replace(' ', '_')}")
        paiURI = URIRef(f"{n}{rei['pai'].replace(' ', '_')}")
        maeURI = URIRef(f"{n}{rei['mãe'].replace(' ', '_')}")

        g.add((reiURI, RDF.type, OWL.NamedIndividual))
        g.add((reiURI, RDF.type, n.Pessoa))
        g.add((reiURI, n.pertenceDinastia, dinastiaURI))
        g.add((reiURI, n.nome, Literal(rei['nome'])))
        g.add((reiURI, n.datanascimento, Literal(rei['nascimento'])))
        g.add((reiURI, n.dataobito, Literal(rei['morte'])))
        g.add((reiURI, n.temMae, maeURI))
        g.add((reiURI, n.temPai, paiURI))
        
        if maeURI not in maes:
            maes.append(maeURI)
            g.add((maeURI, RDF.type, OWL.NamedIndividual))
            g.add((maeURI, RDF.type, n.Pessoa))
            g.add((maeURI, n.nome, Literal(rei['mãe'])))

        if paiURI not in pais:
            pais.add(paiURI)
            g.add((paiURI, RDF.type, OWL.NamedIndividual))
            g.add((paiURI, RDF.type, n.Pessoa))
            g.add((paiURI, n.nome, Literal(rei['pai'])))



print(g.serialize(format='turtle'))
