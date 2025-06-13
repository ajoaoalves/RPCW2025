

from rdflib import Graph, Namespace, Literal, RDF, OWL, URIRef

n = Namespace("http://www.semanticweb.org/ajr/ontologies/2025/realeza#")
g = Graph().parse("realeza_pai_mae.ttl", format="turtle")

# Define the query to create the temFilho property
query = """
PREFIX : <http://www.semanticweb.org/rpcw.di.uminho.pt/2025/realeza/>
Construct {
    :temProgenitor rdf:type owl:ObjectProperty .
    :temPai rdfs:subPropertyOf :temProgenitor .
    :temMae rdfs:subPropertyOf :temProgenitor .
    ?a :temProgenitor ?b .

    }
    WHERE {
        {?b :temPai ?a .}
        UNION
        {?b :temMae ?a .}
    }
"""

qresult = g.query(query)
g += qresult
print(g.serialize(format="turtle"))
print(len(g))