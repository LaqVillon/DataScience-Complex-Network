"""
Este codigo encontra a correlação entre o grau e o strength da rede que corresponde a março de 2019
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

# ----------------------------------------- GRAU -----------------------------------------

def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1], reverse=True)
    return sub_li


degree = G.degree()
degree_1 = tuple(degree)
degree_2 = list(degree_1)
degree_sorted = Sort(degree_2)

# -------------------------------- GRAU - PESOS (STRENGTH) --------------------------------
# IN + OUT
degree2 = G.degree(weight='weight')
degree2_1 = tuple(degree2)
degree2_2 = list(degree2_1)
degree_sorted_2 = Sort(degree2_2)
# lissta de strength para calcular média
lista_strength = list()
for i in degree_sorted_2:
    lista_strength.append(i[1])

# -------------------------------- Correlação GRAU - STRENGTH --------------------------------

vertice_grau = Sort_vertice(degree_sorted)
vertice_strength = Sort_vertice(degree2_2)
x_strength, y_strength = [], []
for element_1 in vertice_grau:
    x_strength.append(element_1[1])
for element_2 in vertice_strength:
    y_strength.append(element_2[1])
x_mean = np.mean(x_strength)
y_mean = np.mean(y_strength)
corr, _ = pearsonr(x_strength, y_strength)
print("Correlação: ", corr)

# --------------------------------Estimativa-------------------------------

popt, _ = curve_fit(objective, x_strength, y_strength, maxfev=2000)
a, b = popt
x_line2 = arange(min(x_strength), max(x_strength), 1)
y_line2 = objective2(x_line2, a, b)
plt.plot(x_line2, y_line2, '--', color='black', label='Curva aproximada')
# valores das constantes a,b,R2:
a_novo = 143.3760
b_novo = 1.8210
R2_novo = 0.8965

# -------------------------------- Desenho do gráfico --------------------------------------------------------

textstr = '\n'.join((r'$s = {%.4f}k^{%.4f}$' % (a_novo, b_novo), r'$R^{2}=%.4f$' % (R2_novo, )))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
plt.gca().get_xaxis().get_major_formatter().set_useOffset(False)
plt.text(100, 4000000, textstr, fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=props)
plt.ticklabel_format(useMathText=True)
plt.scatter(x_strength, y_strength, s=10, c='green', cmap='viridis', marker='>', label='Relação empírica')
plt.xlabel('Grau (k)', fontsize=10, fontweight='bold')
plt.ylabel('Strength (s)', fontsize=10, fontweight='bold')
plt.legend(fontsize='medium')
# plt.show()
plt.savefig("Figuras/correlacao_strength_grau.jpg")
plt.clf()
