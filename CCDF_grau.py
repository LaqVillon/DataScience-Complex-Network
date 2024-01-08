"""
Este arquivo encontra o CCDF para o Grau da rede que corresponde a março de 2019
Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""


import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import statistics as sta
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


def objective(x, a, b):
    return (x**a)*(2.7183**(x*b))


def objective2(x, a, b):
    lista_x = list()
    for ele in x:
        aux = (ele ** a) * (2.7183 ** (ele * b))
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
G.add_weighted_edges_from(edges2)

# ------------------------------------ Estimativa -------------------------------------------------

degree_sequence = [d for n, d in G.degree()]  # degree sequence
list_degree = rel_freq(degree_sequence)
x, y = zip(*list_degree)
list_degree_ccdf = rel_freq_ccdf(y)
popt, _ = curve_fit(objective, x, list_degree_ccdf, maxfev=2000)
a, b = popt
plt.scatter(x, list_degree_ccdf, s=12, c='green', cmap='viridis', marker='o', label='CCDF empírica')
x_line = x
y_line = objective2(x, a, b)
plt.plot(x_line, y_line, '--', color='black', label='CCDF aproximada')


corre_R2_matrix = np.corrcoef(list_degree_ccdf, y_line)
corre = corre_R2_matrix[0, 1]
R_sq = corre**2
# valores das constantes a,b,R2:
a_novo = -0.3995
b_novo = -0.0086
R2_novo = 0.9715
# print(R_sq)
slope, intercept, r_value, p_value, std_err = stats.linregress(list_degree_ccdf, y_line)
print("r-squared:", r_value**2)
# ---------------------Desenho do gráfico------------------
textstr = '\n'.join((r'$P(X>=k) = k ^{%.4f}e^{%.4fk}$' % (a_novo, b_novo), r'$R^{2}=%.4f$' % (R2_novo, )))
props = dict(boxstyle='round', facecolor='white', alpha=0.5)

# ------------Escala linear -------------
# plt.text(150, 0.5, textstr, fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=props)
# plt.title(r'$\alpha > \beta$')
# plt.axvline(5,color='k',linestyle='solid')
# ------------Escala log-------------
plt.text(10, 0.01, textstr, fontsize=10, horizontalalignment='center', verticalalignment='center', bbox=props) 
plt.yscale('log')
plt.xscale('log')
# # ---------------------------------
plt.grid(True)
plt.xlabel('Grau (k)', fontsize=10, fontweight='bold')
plt.ylabel('P(X>=k)', fontsize=10, fontweight='bold')
plt.legend(fontsize='medium')
# plt.show()
plt.savefig("Figuras/CCDF_grau.jpg")
plt.clf()
