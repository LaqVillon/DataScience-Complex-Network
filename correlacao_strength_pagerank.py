"""
Este codigo encontra a correlação entre o strength e o pagerank da rede que corresponde a março de 2019
Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""


import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
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
    return (a*x+b)


def objective2(x, a, b):
    lista_x = list()
    for ele in x:
        aux = (a*ele+b)
        lista_x.append(aux)
    return lista_x


G = nx.DiGraph()
with open('Dataset/2019/2019_marco_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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


# ------------------------------------- GRAU - PESOS (STRENGTH) --------------------------------
# IN + OUT
degree2 = G.degree(weight='weight')
degree2_1 = tuple(degree2)
degree2_2 = list(degree2_1)
degree_sorted_2 = Sort(degree2_2)
# lissta de strength para calcular média
lista_strength = list()
for i in degree_sorted_2:
    lista_strength.append(i[1])

# ----------------------------------------- GRAU - PAGERANK -------------------------------------
x_clos, y_strength = [], []
# Strength
vertice_strength = Sort_vertice(degree2_2)
for element_2 in vertice_strength:
    y_strength.append(element_2[1])
center2 = nx.pagerank(G)
sort_orders2 = sorted(center2.items(), key=lambda x: x[0])
for i in sort_orders2:
    x_clos.append(i[1])
x_mean = np.mean(y_strength)
y_mean = np.mean(x_clos)
corr, _ = pearsonr(x_clos, y_strength)
print("Correlação: ", corr)
x_grau = y_strength
y_clos = x_clos

# ------------------------------------  Estimativa  ------------------------------------------------

popt, _ = curve_fit(objective, x_grau, y_clos, maxfev=2000)
a, b = popt

x_line2 = arange(min(x_grau), max(x_grau), 1)
y_line2 = objective(x_line2, a, b)
plt.plot(x_line2, y_line2, '--', color='black', label='Curva aproximada')
# valores das constantes a,b,R2:
a_novo = 4.845981923987908e-09
b_novo = 0.0004033555627398385
R2_novo = 0.8716231949903912

# -------------------------------- Desenho do gráfico --------------------------------------------------------
textstr = '\n'.join((r'$y = 4.85*10^{-9}s + 0.0004$', r'$R^{2}=%.4f$' % (R2_novo, )))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
plt.text(6.5e6, 0.015, textstr, fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=props)
plt.ticklabel_format(useMathText=True)
plt.scatter(x_grau, y_clos, s=10, c='green', cmap='viridis', marker='>', label='Relação empírica')
plt.xlabel('Strength (s)', fontsize=10, fontweight='bold')
plt.ylabel('Pagerank (y)', fontsize=10, fontweight='bold')
plt.legend(fontsize='medium')
# plt.show()
plt.savefig("Figuras/correlacao_strength_pagerank.jpg")
plt.clf()
