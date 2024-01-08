"""
Este codigo calcula o strength da rede para cada mês de 2020.

Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""

import csv
import os
import networkx as nx
import numpy as np


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1], reverse=True)
    return sub_li


def print_strength_meses(data: dict) -> None:
    file_path = "Strength/strength_2020.txt"
    if os.path.exists(file_path) == False:    
        for mes in range(1,7):
            print("""-------------------------------- Mês: """, mes, """--------------------------""")
            # print(list(G1.edges(data=True)))
            # IN + OUT
            degree2 = data[mes].degree(weight='weight')
            degree2_1 = tuple(degree2)
            degree2_2 = list(degree2_1)
            degree_sorted_2 = Sort(degree2_2)
            # print(degree2)
            # -----lissta de strength para calcular média
            lista_strength = list()
            # -----------------------------------------
            for i in degree_sorted_2:
                lista_strength.append(i[1])
                # print(i[0], i[1]) #, G1.nodes[i[0]]['ORIGIN_CITY_NAME'])
            # print(lista_strength)
            # print(sum(lista_strength))
            print(np.mean(lista_strength))
            with open('Strength/strength_2020.txt', 'a+') as f:
                f.write('""------------------------------------  Mês: ')
                f.write(str(mes))
                f.write(' --------------------------""\n')
                f.write(str(np.mean(lista_strength)))
                f.write('\n')
    
    
# # ------------------------------------ Leitura de dados ------------------------------------
G1 = nx.DiGraph()
with open('Dataset/2020/2020_janeiro_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G1.add_weighted_edges_from(edges2)

G2 = nx.DiGraph()
with open('Dataset/2020/2020_fevereiro_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G2.add_weighted_edges_from(edges2)

G3 = nx.DiGraph()
with open('Dataset/2020/2020_marco_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G3.add_weighted_edges_from(edges2)
# print(list(G1.edges(data=True)))

G4 = nx.DiGraph()
with open('Dataset/2020/2020_abril_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G4.add_weighted_edges_from(edges2)

G5 = nx.DiGraph()
with open('Dataset/2020/2020_maio_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G5.add_weighted_edges_from(edges2)

G6 = nx.DiGraph()
with open('Dataset/2020/2020_junho_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G6.add_weighted_edges_from(edges2)


# ------------------------------------ CALCULO DO STRENGTH ------------------------------------
print("""------------------------------------ Strength do ano 2020 --------------------------""")
dict_data_meses = {1: G1, 2: G2, 3: G3, 4: G4, 5: G5, 6: G6}
print_strength_meses(dict_data_meses)
