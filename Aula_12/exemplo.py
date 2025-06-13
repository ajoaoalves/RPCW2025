

from rdflib import Graph, Namespace, Literal, RDF, OWL, URIRef

n = Namespace("http://www.example.org/disease-ontology#")
g = Graph().parse("diagonostico_doenca.ttl", format="turtle")

# Define the query to create the temFilho property
query = """
PREFIX : <http://www.example.org/disease-ontology#>
Construct {
    :temFilho rdf:type owl:ObjectProperty .
    ?a :temFilho ?b .
    }
    WHERE {
    {?b :temPai ?a .}
    UNION
    {?b :temMae ?a .}
    }
"""

qresult = g.query(query)
print(qresult)
g += qresult
print(g.serialize(format="turtle"))