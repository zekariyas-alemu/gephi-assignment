import pickle
import networkx as nx
import pydot
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot

MY_ID = 612206431
d=[]


dialogs = pickle.load(open("dialogs.pkl", "rb"))
members = pickle.load(open("members.pkl", "rb"))
print("a")


g = nx.Graph()
'''for i in dialogs:
    print(str(i.chat.title or i.chat.first_name)+str(i.chat.id))
    d.append(i.chat.id)
print(len(d))'''
for k, v in members.items():
    #k=str(k)
    for m in v:
        if m.user.id != MY_ID:
            g.add_edge(k, m.user.id)
            #d.append(k)
    #print(len(d))
        bet_centrality = nx.betweenness_centrality(g)
        print(bet_centrality)

'''g2 = g.copy()
for k, v in nx.degree(g):
    if v == 1:
        g2.remove_node(k)
write_dot(g2, 'graph.dot')
g3 = g2.copy()
for k, v in nx.degree(g2):
    if v == 2:
        g3.remove_node(k)
write_dot(g3, 'graph1.dot')'''
