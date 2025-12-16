import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Digraph()
        self._cromosomi = None
        self._geni  = None
        self._interazione = None



    def costruisci_grafo(self):
        self._cromosomi = DAO.read_cromosomi()
        self._geni = DAO.read_geni()
        self._interazione = DAO.read_interazioni()

        self.G.clear()

        for cromosoma in self._cromosomi:
            self.G.add_node(cromosoma)


        for interazione in self._interazione:
            peso = 0
            if interazione.id_gene1 and interazione.id_gene2 in self._geni:
                peso += interazione.correlazione
                self.G.add_edge(interazione.id_gene1, interazione.id_gene2, weight=peso)


    def conta_nodi(self):
        return self.G.number_of_nodes()

    def conta_edges(self):
        return self.G.number_of_edges()

    def conta_min_max_peso(self):
        peso_min = 1000
        for u,v,data in self.G.edges(data = True):
            if data["weight"] < peso_min:
                peso_min = data["weight"]

        peso_max = 0.0
        for u,v,data in self.G.edges(data = True):
            if data["weight"] > peso_min:
                peso_max = data["weight"]


        return peso_min, peso_max







