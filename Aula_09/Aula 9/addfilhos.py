from rdflib import Graph, Namespace, Literal


g = Graph()
g.parse("genoa2.ttl")

q="""
Construct{
    ?prog :temFilho ?filho .
}
WHERE {
    { ?filho :temMae ?prog .}
    UNION
    { ?filho :temPai ?prog .}
}
"""
n = Namespace("http://www.semanticweb.org/gonca/ontologies/2025/genoa#")
for r in g.query(q):
    g.add((r[0], n.temFilho, r[2]))
#    g.add(r)

print(g.serialize("genoa3.ttl", format="turtle"))