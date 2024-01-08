"""
Este codigo encontra a robustez das rede em relação a 
Componentes fortemente conexas correspondente a março de 2020.
As variáveis 'r1, r2, r3, r4, r5' representam a quantidade de SC 
por remoção de aeroportos gerados para cada métrica.

Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""


import csv
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

with open('Dataset/2020/2020_marco_arestas_peso_atualizado.csv', 'r') as edgecsv:  # Open the file
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
print(nx.number_strongly_connected_components(G))
c1 = nx.number_strongly_connected_components(G)


# # ----------------------------------------- GRAU -------------------------------------------
# def Sort(sub_li):
#     sub_li.sort(key=lambda x: x[1], reverse=True)
#     return sub_li


# degree = G.degree()
# degree_1 = tuple(degree)
# degree_2 = list(degree_1)
# degree_sorted = Sort(degree_2)
# # print(degree2)
# # for i in degree_sorted:
#     # print(i[0], i[1], G.nodes[i[0]])  # ['ORIGIN_CITY_NAME'])
#     #  S
# l1 = [11292, 11298, 13930, 10397, 11057, 13487, 12889, 14107, 11433, 12892]  # dez primeiros
# aux = list()
# aux.append(c1)
# for ele1 in l1:
#     G.remove_node(ele1)
#     cx = nx.number_strongly_connected_components(G)
#     aux.append(cx)
    
# # Calculado a quantidade de SC geradas por remocção de aeroportos:
# print(aux)  # aux = [50, 67, 78, 86, 92, 97, 103, 104, 113, 121, 124]

r1 = [50, 67, 78, 86, 92, 97, 103, 104, 113, 121, 124]


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

# l2 = [10397, 13930, 12892, 11298, 11292, 14107, 13204, 12889, 11057, 14747]

# aux = list()
# aux.append(c1)
# for ele2 in l2:
#     G.remove_node(ele2)
#     cx = nx.number_strongly_connected_components(G)
#     aux.append(cx)
    
# # Calculado a quantidade de SC geradas por remocção de aeroportos:
# print(aux)  # aux = [50, 55, 61, 63, 76, 95, 103, 104, 106, 111, 114]

r2 = [50, 55, 61, 63, 76, 95, 103, 104, 106, 111, 114]


# # # --------------------------------------- Betweenness ---------------------------------------
# y_strength = list()
# center2 = nx.betweenness_centrality(G)
# sort_orders2 = sorted(center2.items(), key=lambda x: x[1])
# for i in sort_orders2:
#     y_strength.append(i[1])
# print(sort_orders2)

# l3 = [10299, 14747, 11292, 13930, 11630, 11298, 13487, 10551, 14107, 12892]

# aux = list()
# aux.append(c1)
# for ele3 in l3:
#     G.remove_node(ele3)
#     cx = nx.number_strongly_connected_components(G)
#     aux.append(cx)
# # # Calculado a quantidade de SC geradas por remocção de aeroportos:
# print(aux)  # aux = [50, 54, 59, 76, 83, 101, 113, 119, 125, 133, 136]

r3 = [50, 54, 59, 76, 83, 101, 113, 119, 125, 133, 136]


# # ------------------------------clos------------------
# y_strength = list()
# center2 = nx.closeness_centrality(G)
# sort_orders2 = sorted(center2.items(), key=lambda x: x[1])
# for i in sort_orders2:
#     y_strength.append(i[1])
# print(sort_orders2)

# l4 = [11292, 13930, 14747, 13487, 14107, 12892, 14057, 11298, 10397, 10299]
# aux = list()
# aux.append(c1)
# for ele4 in l4:
#     G.remove_node(ele4)
#     cx = nx.number_strongly_connected_components(G)
#     aux.append(cx)
# # Calculado a quantidade de SC geradas por remocção de aeroportos:
# print(aux)  # aux = [50, 67, 74, 77, 83, 87, 90, 92, 108, 114, 120]


r4 = [50, 67, 74, 77, 83, 87, 90, 92, 108, 114, 120]

# # # --------------------------------------- Pagerank ---------------------------------------

# y_strength = list()
# center2 = nx.pagerank(G)
# sort_orders2 = sorted(center2.items(), key=lambda x: x[1])
# for i in sort_orders2:
#     y_strength.append(i[1])
# print(sort_orders2)

# l5 = [10397, 14747, 13930, 11292, 11298, 10299, 12892, 14107, 11057, 12889]
# aux = list()
# aux.append(c1)
# for ele5 in l5:
#     G.remove_node(ele5)
#     cx = nx.number_strongly_connected_components(G)
#     aux.append(cx)
# # Calculado a quantidade de SC geradas por remocção de aeroportos:
# print(aux)  # aux = [50, 55, 58, 64, 82, 95, 101, 104, 112, 117, 119]

r5 = [50, 55, 58, 64, 82, 95, 101, 104, 112, 117, 119]


# # ------------- lista de aeroportos parcialmente fechados pelo coronavirus, new york state -------------
# at = [14747, 12892, 14771, 13204, 11292, 11618, 14057, 10397, 12478, 13495]
# aux = list()
# aux.append(c1)
# for ele5 in at:
#     G.remove_node(ele5)
#     cx = nx.number_strongly_connected_components(G)
#     aux.append(cx)
# print(aux)  # [50, 53, 55, 57, 58, 76, 77, 79, 84, 85, 85]

corona = [50, 53, 55, 57, 58, 76, 77, 79, 84, 85, 85]

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
plt.plot(list_x, corona, 'x', color='black', linestyle='-', linewidth=1, markersize=8, label='Pandemia')
plt.xlabel('Aeroportos removidos', fontsize=10, fontweight='bold')
plt.ylabel('SC', fontsize=10, fontweight='bold')
plt.legend(fontsize='medium')
plt.grid(True)
# plt.show()
plt.savefig("Figuras/falhas_SC_2020.jpg")
plt.clf()

