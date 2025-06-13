from rdflib import Graph, Namespace, Literal, RDF, OWL


g = Graph()
g.parse("genoa3.ttl")


q="""
Construct{
    ?a :temIrmao ?b.
}
WHERE {
    ?a :temPai ?pai.
    ?b :temPai ?pai.
    ?a :temMae ?mae.
    ?b :temMae ?mae.
    FILTER (?a != ?b)

    }
"""
n = Namespace("http://www.semanticweb.org/gonca/ontologies/2025/genoa#")

g.add((n.temSogro, RDF.type, OWL.ObjectProperty))
g.add((n.temSogra, RDF.type, OWL.ObjectProperty))

for r in g.query(q):
    #print (r[0].split("#")[1], r[1], r[2].split("#")[1])
    g.add((r))
    #g.add((r[0], n.tem, r[2]))
print(g.serialize())
(g.serialize("genoa4.ttl", format="turtle"))