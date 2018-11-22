import rdflib
import re
g1 = rdflib.graph.Graph()
g1.parse("iswc-2013-complete.rdf",format="xml")

for s, p, o in g1:
    print((s, p, o))
