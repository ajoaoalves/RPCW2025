# --------------------------------------------------------------------
# GeraÃ§Ã£o da ontologia para o dataset dos 120 anos dos Jogos OlÃ­mpicos
# 2025-04-10 by jcr
# --------------------------------------------------------------------
# Ontologia base (estrutura) criada Ã  mÃ£o no ProtÃ©gÃ©
# --------------------------------------------------------------------
import csv
import re
from rdflib import Graph, Namespace, URIRef, RDF, OWL
# --------------------------------------------------------------------
# Carregar a ontologia base para o grafo em memÃ³ria
# --------------------------------------------------------------------
n = Namespace("http://www.semanticweb.org/ajr/ontologies/2025/genoa/")
g = Graph()
g.parse("genoa_base.ttl")

ficheiro = "familia.csv"
individuos = set()



# Ler o CSV com separador ';'
with open(ficheiro, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for linha in reader:

        # CÃ¡lculo dos URI de cada entidade

        pessoaURI = URIRef(f"{n}{linha['Indivíduo'].replace(' ', '_')}")
        individuos.add(pessoaURI)
        paiURI = URIRef(f"{n}{linha['Pai'].replace(' ', '_')}")
        individuos.add(paiURI)
        maeURI = URIRef(f"{n}{linha['Mãe'].replace(' ', '_')}")
        individuos.add(maeURI)

        g.add((pessoaURI, n.temPai,paiURI))
        g.add((pessoaURI, n.temMae,maeURI))

    for i in individuos:
        g.add((i, RDF.type, OWL.NamedIndividual))

print(g.serialize())

