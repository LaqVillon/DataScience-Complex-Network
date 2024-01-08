"""
Este codigo calcula o strength da rede para cada mês de 2019.

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
    file_path = "Strength/strength_2019.txt"
    if os.path.exists(file_path) == False:    
        for mes in range(1,13):
            print("""--------------------------------- Mês: """, mes, """--------------------------""")
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
            with open('Strength/strength_2019.txt', 'a+') as f:
                f.write('""------------------------------------ Mês: ')
                f.write(str(mes))
                f.write(' --------------------------""\n')
                f.write(str(np.mean(lista_strength)))
                f.write('\n')
    
    
# # ------------------------------------ Leitura de dados ------------------------------------
G1 = nx.DiGraph()
with open('Dataset/2019/2019_janeiro_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
with open('Dataset/2019/2019_fevereiro_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G3.add_weighted_edges_from(edges2)
# print(list(G1.edges(data=True)))

G4 = nx.DiGraph()
with open('Dataset/2019/2019_abril_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
with open('Dataset/2019/2019_maio_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
with open('Dataset/2019/2019_junho_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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

G7 = nx.DiGraph()
with open('Dataset/2019/2019_julho_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G7.add_weighted_edges_from(edges2)

G8 = nx.DiGraph()
with open('Dataset/2019/2019_agosto_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G8.add_weighted_edges_from(edges2)

G9 = nx.DiGraph()
with open('Dataset/2019/2019_setembro_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G9.add_weighted_edges_from(edges2)

G10 = nx.DiGraph()
with open('Dataset/2019/2019_outubro_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G10.add_weighted_edges_from(edges2)

G11 = nx.DiGraph()
with open('Dataset/2019/2019_novembro_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G11.add_weighted_edges_from(edges2)

G12 = nx.DiGraph()
with open('Dataset/2019/2019_dezembro_arestas_peso_atualizado.csv', 'r') as edgecsv: # Open the file
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
G12.add_weighted_edges_from(edges2)

# ------------------------------------ CALCULO DO STRENGTH ------------------------------------
print("""------------------------------------ Strength do ano 2019 --------------------------""")
dict_data_meses = {1: G1, 2: G2, 3: G3, 4: G4, 5: G5, 6: G6, 
                   7: G7, 8: G8, 9: G9, 10: G10, 11: G11, 12: G12}
print_strength_meses(dict_data_meses)
