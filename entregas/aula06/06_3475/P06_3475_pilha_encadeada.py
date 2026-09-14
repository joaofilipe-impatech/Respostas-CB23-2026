class PilhaEncadeada:
    class No:
        def __init__(self, valor, ponteiro=None):
            self.valor = valor
            self.ponteiro = ponteiro
    
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        novo_no = self.No(item, self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        if self._tamanho == 0:
            raise IndexError("A pilha está vazia!")
        no_apagado = self._topo
        self._topo = no_apagado.ponteiro
        self._tamanho -=1
        return no_apagado.valor

    def topo(self):
        if self._tamanho == 0:
            raise IndexError("A pilha está vazia!")
        return self._topo

    def esta_vazia(self):
        return self._tamanho == 0

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        elementos = []
        proximo_no = self._topo
        while proximo_no is not None:
            elementos.append(proximo_no.valor)
            proximo_no = proximo_no.ponteiro
        return " -> ".join(elementos)