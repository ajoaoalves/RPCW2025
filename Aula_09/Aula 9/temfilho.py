from rdflib import Graph, Namespace, Literal


g = Graph()
g.parse("genoa.ttl")

q="""
Select ?s
where {
    ?s a :Pessoa .
}
"""
n = Namespace("http://www.semanticweb.org/gonca/ontologies/2025/genoa#")
for r in g.query(q):
    g.add((r[0], n.nome, Literal(r[0].split("#")[1], lang="pt")))
#    g.add(r)

print(g.serialize("genoa2.ttl", format="turtle"))