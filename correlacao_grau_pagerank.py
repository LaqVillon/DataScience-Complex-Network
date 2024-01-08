"""
Este codigo encontra a correlação entre o grau e pagerank da rede que corresponde a março de 2019
Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""


import csv
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from scipy.optimize import curve_fit
from numpy import arange


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1], reverse=True)
    return sub_li


def Sort_vertice(sub_li):
    sub_li.sort(key=lambda x: x[0])
    return sub_li


def objective(x, a, b):
    return (a*(x**b))


def objective2(x, a, b):
    lista_x = list()
    for ele in x:
        aux = a*(ele**b)
        lista_x.append(aux)
    return lista_x


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
degree_sorted = Sort(degree_2)

# ------------------------------------  Correlação GRAU - Pagerank --------------------------------------------

x_grau, y_clos = [], []
# grau
vertice_grau = Sort_vertice(degree_2)
for element_1 in vertice_grau:
    x_grau.append(element_1[1])
center2 = nx.pagerank(G)
sort_orders2 = sorted(center2.items(), key=lambda x: x[0])
for i in sort_orders2:
    y_clos.append(i[1])
corr, _ = pearsonr(x_grau, y_clos)
print(corr)  # 0.848595305311133

# ------------------------------------- Estimativa -----------------------------------------------------------

popt, _ = curve_fit(objective, x_grau, y_clos, maxfev=2000)
a, b = popt
x_line2 = arange(min(x_grau), max(x_grau), 1)
y_line2 = objective2(x_line2, a, b)
plt.plot(x_line2, y_line2, '--', color='black', label='Curva aproximada')

# valores das constantes a,b,R2:
a_novo = 1.4328839194867389e-06
b_novo = 1.6994027686630586
R2_novo = 0.8057178028783031

# -------------------------------- Desenho do gráfico --------------------------------------------------------
textstr = '\n'.join((r'$y = 1.4*10^{-6}k^{%.4f}$' % (b_novo), r'$R^{2}=%.4f$' % (R2_novo, )))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
plt.text(275, 0.033, textstr, fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=props)
plt.scatter(x_grau, y_clos, s=10, c='green', cmap='viridis', marker='>', label='Relação empírica')
plt.xlabel('Grau (k)', fontsize=10, fontweight='bold')
plt.ylabel('Pagerank (y)', fontsize=10, fontweight='bold')
plt.legend(fontsize='medium')
# plt.show()
plt.savefig("Figuras/correlacao_grau_pagerank.jpg")
plt.clf()
