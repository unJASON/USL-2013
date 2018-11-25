import rdflib
from rdflib.namespace import RDF
from rdflib.namespace import FOAF
from rdflib import URIRef
g=rdflib.Graph()
result=g.parse(r"e:\iswc-2013-complete.rdf")
with open(r"iswc-2013-complete\organizations.txt") as file:
    for line in file:
        print (line.strip(),end="")
        print(" ",end="")
        for subject,predicate,obj in result:
            if subject==URIRef(line.strip()) and predicate==URIRef("http://xmlns.com/foaf/0.1/member"):
                print (obj,end="")
                print (" ",end="")

        print("")
