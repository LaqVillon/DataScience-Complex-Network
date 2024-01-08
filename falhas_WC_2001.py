"""
Este codigo encontra a robustez das rede em relação a 
Componentes fracamente conexas correspondente a setembro de 2001.
As variáveis 'r1, r2, r3, r4, r5' representam a quantidade de SC 
por remoção de aeroportos gerados para cada métrica.

Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""

import csv
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
with open('Dataset/2001/2001_setembro_arestas_peso_atualizado.csv', 'r') as edgecsv:  # Open the file
    edgereader = csv.reader(edgecsv)  # Read the csv
    edges = [e for e in edgereader][0:]
edges2 = []
aresta2 = ()
for aresta in edges:
    no_ori = int(aresta[0])
    no_dest = int(aresta[1])
    peso = float(aresta[2])
    if peso != 0.0:
        aresta2 = (no_ori, no_dest, peso)
        edges2.append(aresta2)
G.add_weighted_edges_from(edges2)
print('Numero de componentes fracamente conexos')
print(nx.number_weakly_connected_components(G))
c1 = nx.number_weakly_connected_components(G)


# # ----------------------------------------- GRAU -------------------------------------------
# def Sort(sub_li):
#     sub_li.sort(key=lambda x: x[1], reverse=True)
#     return sub_li


# degree = G.degree()
# degree_1 = tuple(degree)
# degree_2 = list(degree_1)
# degree_sorted = Sort(degree_2)
# # print(degree2)
# for i in degree_sorted:
#     print(i[0], i[1], G.nodes[i[0]])  # ['ORIGIN_CITY_NAME'])
#     #  S
# l1 = [10397, 13487, 11298, 11433, 13930, 15016, 12266, 14747, 11292, 11042]  # dez primeiros
# aux = list()
# aux.append(c1)
# for ele1 in l1:
#     G.remove_node(ele1)
#     cx = nx.number_weakly_connected_components(G)
#     aux.append(cx)
# # Calculado a quantidade de WC geradas por remocção de aeroportos:
# print(aux)  # aux = [2, 9, 12, 13, 14, 14, 24, 33, 34, 37, 37]

r1 = [2, 9, 12, 13, 14, 14, 24, 33, 34, 37, 37]


# # # --------------------------------------- STRENGTH ----------------------------------------
# def Sort(sub_li):
#     sub_li.sort(key=lambda x: x[1], reverse=True)
#     return sub_li

# # print(list(G1.edges(data=True)))
# # IN + OUT
# degree2 = G.degree(weight='weight')
# degree2_1 = tuple(degree2)
# degree2_2 = list(degree2_1)
# degree_sorted_2 = Sort(degree2_2)
# # print(degree2)
# # -----lissta de strength para calcular média
# lista_strength = list()
# # -----------------------------------------
# for i in degree_sorted_2:
#     lista_strength.append(i[1])
#     print(i[0], i[1])  # , G1.nodes[i[0]]['ORIGIN_CITY_NAME'])

# l2 = list()
# x = 1
# for x1 in degree_sorted_2:
#     if x < 11:
#         l2.append(x1[0])
#     x = x + 1
# print(l2)
# l2 = [10397, 13930, 11298, 12892, 14107, 11292, 11433, 12889, 13487, 15016]

# aux = list()
# aux.append(c1)
# for ele2 in l2:
#     G.remove_node(ele2)
#     cx = nx.number_weakly_connected_components(G)
#     aux.append(cx)
# # Calculado a quantidade de WC geradas por remocção de aeroportos:
# print(aux)  # aux = [2, 9, 9, 10, 11, 11, 14, 15, 15, 18, 28]

r2 =[2, 9, 9, 10, 11, 11, 14, 15, 15, 18, 28]


# # # --------------------------------------- Betweenness ---------------------------------------
# y_strength = list()
# center2 = nx.betweenness_centrality(G)
# sort_orders2 = sorted(center2.items(), key=lambda x : x[1])
# for i in sort_orders2:
#     y_strength.append(i[1])
# print(sort_orders2)

# l3 = list()
# x = 1  #  len(sort_orders2)-9
# for x1 in sort_orders2:
#     if  (x > len(sort_orders2)-10):  #  (x < len(sort_orders2) + 1) and (x > len(sort_orders2)-10):
#         l3.append(x1[0])
#     x = x + 1
# l3.reverse()
# print(l3)  # l3 = [13487, 10397, 10299, 14747, 11298, 11433, 15016, 12266, 11630, 12173]

# aux = list()
# aux.append(c1)
# for ele3 in l3:
#     G.remove_node(ele3)
#     cx = nx.number_weakly_connected_components(G)
#     aux.append(cx)
    
# # Calculado a quantidade de WC geradas por remocção de aeroportos:
# print(aux)  # aux = [2, 5, 12, 17, 19, 20, 21, 31, 40, 43, 47]

r3 = [2, 5, 12, 17, 19, 20, 21, 31, 40, 43, 47]


# # # --------------------------------------- closeness ---------------------------------------
# y_strength = list()
# center2 = nx.closeness_centrality(G)
# sort_orders2 = sorted(center2.items(), key=lambda x: x[1])
# for i in sort_orders2:
#     y_strength.append(i[1])
# print(sort_orders2)

# l4 = list()
# x = 1  #  len(sort_orders2)-9
# for x1 in sort_orders2:
#     if  (x > len(sort_orders2)-10):  #  (x < len(sort_orders2) + 1) and (x > len(sort_orders2)-10):
#         l4.append(x1[0])
#     x = x + 1
# l4.reverse()
# print(l4)  # [13487, 11298, 10397, 15016, 12266, 14747, 13930, 11433, 14107, 12892]

# aux = list()
# aux.append(c1)
# for ele4 in l4:
#     G.remove_node(ele4)
#     cx = nx.number_weakly_connected_components(G)
#     aux.append(cx)
# # Calculado a quantidade de WC geradas por remocção de aeroportos:
# print(aux)  # aux = [2, 5, 6, 13, 23, 32, 33, 33, 34, 34, 35]

r4 = [2, 5, 6, 13, 23, 32, 33, 33, 34, 34, 35]


# # # --------------------------------------- Pagerank ---------------------------------------
# y_strength = list()
# center2 = nx.pagerank(G)
# sort_orders2 = sorted(center2.items(), key=lambda x: x[1])
# for i in sort_orders2:
#     y_strength.append(i[1])
# print(sort_orders2)

# l5 = list()
# x = 1  #  len(sort_orders2)-9
# for x1 in sort_orders2:
#     if (x > len(sort_orders2)-10):  #  (x < len(sort_orders2) + 1) and (x > len(sort_orders2)-10):
#         l5.append(x1[0])
#     x = x + 1
# l5.reverse()
# print(l5) # [10397, 11298, 13930, 13487, 12892, 11433, 14747, 11292, 15016, 14107]

# aux = list()
# aux.append(c1)
# for ele5 in l5:
#     G.remove_node(ele5)
#     cx = nx.number_weakly_connected_components(G)
#     aux.append(cx)
    
# # Calculado a quantidade de SC geradas por remocção de aeroportos:
# print(aux)  # aux = [2, 9, 10, 10, 13, 14, 15, 16, 19, 29, 29]

r5 = [2, 9, 10, 10, 13, 14, 15, 16, 19, 29, 29]


# # # ------------- lista de aeroportos fechados logo dos atentados, new york state --------------------
# at = [12478, 12953, 10792, 10257, 14576, 15096, 12197, 12391, 15070, 11537]
# aux = list()
# aux.append(c1)
# for ele5 in at:
#     G.remove_node(ele5)
#     cx = nx.number_strongly_connected_components(G)
#     aux.append(cx)
# print(aux)

t = [2, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

i = 0
list_x = list()
while (i < 11):
    list_x.append(i)
    i = i + 1

plt.plot(list_x, r1, 'o', color='red', linestyle='-', linewidth=0.5, markersize=5, label='Grau')
plt.plot(list_x, r2, 'o', color='blue', linestyle='-', linewidth=0.5, markersize=5, label='Strength')
plt.plot(list_x, r3, 'o', color='green', linestyle='-', linewidth=0.5, markersize=5, label='Betweenness')
plt.plot(list_x, r4, 'o', color='brown', linestyle='-', linewidth=0.5, markersize=5, label='Closeness')
plt.plot(list_x, r5, 'o', color='yellow', linestyle='-', linewidth=0.5, markersize=5, label='Pagerank')
plt.plot(list_x, t, 'x', color='black', linestyle='-', linewidth=1, markersize=8, label='Atentados')
plt.xlabel('Aeroportos removidos', fontsize=10, fontweight='bold')
plt.ylabel('WC', fontsize=10, fontweight='bold')
plt.legend(fontsize='medium')
plt.grid(True)
# plt.show()
plt.savefig("Figuras/falhas_WC_2001.jpg")
plt.clf()
