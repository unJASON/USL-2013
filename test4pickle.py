from igraph import *
import pickle
with open('comboVertexClustering.pk', 'rb') as f:
    louvian = pickle.load(f)
with open('fastUVertexClustering.pk', 'rb') as f:
    louvian_fastU = pickle.load(f)
with open('fastnewman.pk', 'rb') as f:
    louvian_fastNewMan = pickle.load(f)



t=compare_communities(louvian,louvian_fastU,method="nmi")
print(t)
t=compare_communities(louvian,louvian_fastNewMan,method="nmi")
print(t)
t=compare_communities(louvian_fastU,louvian_fastNewMan,method="nmi")
print(t)
t=compare_communities(louvian,louvian_fastU,method="split-join")
print(t)
t=compare_communities(louvian,louvian_fastNewMan,method="split-join")
print(t)
t=compare_communities(louvian_fastU,louvian_fastNewMan,method="split-join")
print(t)

testplot=Plot(bbox=(3000,3000))
testplot2=Plot(bbox=(3000,3000))
testplot3=Plot(bbox=(3000,3000))

layout=louvian.graph.layout("kk")
layout2=louvian_fastU.graph.layout("kk")
layout3=louvian_fastNewMan.graph.layout("kk")

testplot.add(louvian,layout=layout,bbox=(3000,3000))
testplot.save("louvian.png")
testplot.remove(louvian)

testplot2.add(louvian_fastU,layout=layout,bbox=(3000,3000))
testplot2.save("louvian_fastU.png")
testplot2.remove(louvian_fastU)

testplot3.add(louvian_fastNewMan,layout=layout,bbox=(3000,3000))
testplot3.save("louvian_fastNewMan.png")
testplot3.remove(louvian_fastNewMan)
