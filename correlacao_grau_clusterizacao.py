"""
Este codigo encontra a correlação entre o grau e clusterizalção da rede que corresponde a março de 2019
Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""


import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from scipy.optimize import curve_fit


def objective(x, a, b):
    # return a*math.exp(-x)
    return (a*(x**b))
    # return (a*(x**b))


def objective2(x, a, b):
    # return a*math.exp(-x)
    lista_x = list()
    for ele in x:
        aux = a*(ele**b)
        # aux = (a * (ele ** b))
        lista_x.append(aux)
    return lista_x


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1], reverse=True)
    return sub_li


def Sort_vertice(sub_li):
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

# -------------------------------------------- GRAU ---------------------------------------------------

degree = G.degree()
degree_1 = tuple(degree)
degree_2 = list(degree_1)


# ------------------------------ Correlação GRAU - closeeness -----------------------------------------
x_grau, y_clos = [], []
vertice_grau = Sort_vertice(degree_2)
for element_1 in vertice_grau:
    x_grau.append(element_1[1])
# closeness
center2 = nx.clustering(G, weight=None)
sort_orders2 = sorted(center2.items(), key=lambda x: x[0])
for i in sort_orders2:
    y_clos.append(i[1])
corr, _ = pearsonr(x_grau, y_clos)
print("Correlação: ", corr) 

# --------------------------------Estimativa-------------------------------

popt, _ = curve_fit(objective, x_grau, y_clos, maxfev=2000)
a, b = popt
x_line2 = x_grau
y_line2 = objective2(x_line2, a, b)
corre_R2_matrix = np.corrcoef(y_clos, y_line2)
corre = corre_R2_matrix[0, 1]
R_sq = corre**2
# print(R_sq)

# valores das constantes a,b,R2:
a_novo = 5.585427189111784e-07
b_novo = 2.0188726455811654
R2_novo = 0.25851000255250917

# ---------------------Desenho do gráfico------------------
textstr = r'$r_{p}=%.4f$' % (corr, )
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
plt.text(300, 0.6, textstr, fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=props)
plt.ticklabel_format(useMathText=True)
plt.scatter(x_grau, y_clos, s=10, c='green', cmap='viridis', marker='>', label='Relação empírica')
plt.xlabel('Grau (k)', fontsize=10, fontweight='bold')
plt.ylabel('Clusterização local', fontsize=10, fontweight='bold')
# plt.show()
plt.savefig("Figuras/correlacao_grau_clusterizacao.jpg")
plt.clf()
