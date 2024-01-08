"""
Este codigo encontra o CCDF para o Strength da rede que corresponde a março de 2019
Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""


import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit


def rel_freq(x):
    freq = [(value, x.count(value) / len(x)) for value in set(x)]
    freq.sort()
    return freq


def rel_freq_ccdf(y):
    lista1 = list(y)
    lista2 = lista1.copy()
    soma = 0
    j = 1
    for ele2 in lista1:
        soma = soma + ele2
        ccdf = 1 - soma
        if j < len(lista1):
            lista2[j] = ccdf
        j = j+1
    lista2[0] = 1
    tupla = tuple(lista2)
    return tupla


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1], reverse=True)
    return sub_li


def objective(x, a, b):
    return a*x**b


def objective2(x, a, b):
    lista_x = list()
    for ele in x:
        aux = a*ele**b
        lista_x.append(aux)
    return lista_x


# -------------------------------- Atualizando a rede --------------------------------------------

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

# -------------------------------- Preparando o grafo --------------------------------------------

G.add_weighted_edges_from(edges2)
degree2 = G.degree(weight='weight')
degree2_1 = tuple(degree2)
degree2_2 = list(degree2_1)
degree_sorted_2 = Sort(degree2_2)
# ----- lissta de strength para calcular média
lista_strength = list()
for i in degree_sorted_2:
    lista_strength.append(i[1])

# -------------------------------- Estimativa ----------------------------------------------------

sigma = 686923.7387
list_degree = rel_freq(lista_strength)
x, y = zip(*list_degree)
list_degree_ccdf = rel_freq_ccdf(y)

popt, _ = curve_fit(objective, x, list_degree_ccdf, maxfev=10000)
a, b = popt
# print(a, b)
# print(x)

plt.scatter(x, list_degree_ccdf, s=5, c='green', cmap='viridis', marker='o', label='CCDF empírica')
y_line = objective2(x, a, b)
corre_R2_matrix = np.corrcoef(list_degree_ccdf, y_line)
corre = corre_R2_matrix[0, 1]
R_sq = corre**2
b_novo = 0.01054213

# print(R_sq)
slope, intercept, r_value, p_value, std_err = stats.linregress(list_degree_ccdf, y_line)
# print("r-squared:", r_value**2)
#  ---------------------- Escala log -------------
# plt.yscale('log')
# plt.xscale('log')
plt.grid(True)
plt.xlabel('Strength (s)', fontsize=10, fontweight='bold')
plt.ylabel('P(X>=s)', fontsize=10, fontweight='bold')
plt.legend(fontsize='medium')
# plt.show()
plt.savefig("Figuras/CCDF_strength.jpg")
plt.clf()
