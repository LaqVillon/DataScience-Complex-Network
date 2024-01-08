"""
Este codigo encontra a correlação entre o grau e o grau médio dos vizinhods da rede que corresponde a março de 2019
Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""

import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1], reverse=True)
    return sub_li


def Sort2(sub_li):
    sub_li.sort(key=lambda x: x[0])
    return sub_li


G = nx.DiGraph()
with open('Dataset/2019/2019_marco_arestas_peso_atualizado.csv', 'r') as edgecsv:  # Open the file
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

# ------------------------------------------------ GRAU --------------------------------------------------------

degree = G.degree()
degree_1 = tuple(degree)
degree_2 = list(degree_1)

# ----------------------------------------   GRAU MEDIO DOS VIZINHOS ------------------------------------------- 

grau_viz = nx.average_neighbor_degree(G)  #  , weight='weight')
list_grau_viz = []
grau_viz2 = sorted(grau_viz.items(), key=lambda x: x[1], reverse=True)

# -------------------------------- Correlação GRAU - GRAU MEDIO DOS _VIZINHOS --------------------------------
# (necessário os valores totais dos graus e da média dos graus vizinhos)

x_grau, y_gra_viz= [], []
# grau
degree_sorted = Sort2(degree_2)
for i in degree_sorted:
    x_grau.append(i[1])
grau_viz3 = sorted(grau_viz.items(), key=lambda x: x[0])
for element_1 in grau_viz3:
    y_gra_viz.append(element_1[1])
x_mean = np.mean(x_grau)
y_mean = np.mean(y_gra_viz)
corr, _ = pearsonr(x_grau, y_gra_viz)
print("Correlação: ", corr)  

# -------------------------------- Desenho do gráfico --------------------------------------------------------
textstr = r'$r_{p}=%.4f$' % (corr, )
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
plt.text(300, 100, textstr, fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=props)
plt.ticklabel_format(useMathText=True)
plt.scatter(x_grau, y_gra_viz, s=10, c='green', cmap='viridis', marker='+', label='1996')
plt.xlabel('Grau (K)', fontsize=10, fontweight='bold')
plt.ylabel('Grau médio dos Vizinhos', fontsize=10, fontweight='bold')
# plt.show()
plt.savefig("Figuras/correlacao_grau_vizinhos.jpg")
plt.clf()
