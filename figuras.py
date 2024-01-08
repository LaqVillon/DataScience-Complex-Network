"""
Este codigo calcula todos os gráficos exibidos na pasta Figure

Author: Luis Armando Quintanilla Villon
Data: Janeiro/2021
"""


def main() -> None:
    with open("CCDF_grau.py") as f:
        exec(f.read())
    with open("CCDF_strength.py") as f:
        exec(f.read())
    with open("correlacao_grau_clusterizacao.py") as f:
        exec(f.read())
    with open("correlacao_grau_pagerank.py") as f:
        exec(f.read())
    with open("correlacao_grau_vizinhos.py") as f:
        exec(f.read())
    with open("correlacao_strength_grau.py") as f:
        exec(f.read())
    with open("correlacao_strength_pagerank.py") as f:
        exec(f.read())
    with open("falhas_SC_2001.py") as f:
        exec(f.read())
    with open("falhas_SC_2020.py") as f:
        exec(f.read())
    with open("falhas_WC_2001.py") as f:
        exec(f.read())
    with open("falhas_WC_2020.py") as f:
        exec(f.read())


if __name__ == '__main__':
    main()
