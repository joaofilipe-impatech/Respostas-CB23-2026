from P06_3475_pilha_encadeada import PilhaEncadeada

class FilaEncadeada:
    def __init__(self):
        self._entrada = PilhaEncadeada()
        self._saida = PilhaEncadeada()

    def enfileirar(self, item):
        """
        Insere o item no fim da fila (no topo da pilha de entrada).

        - `item`: valor a ser guardado na fila.

        *Complexidade:* O(1), pois o método `push()` da pilha possui complexidade O(1).
        """
        self._entrada.push(item)

    @staticmethod
    def inverter_pilha(pilha_origem, pilha_destino):
        """
        Retira os itens da pilha de origem e os envia para a de destino, trocando a ordem.

        - `pilha_origem`: pilha com os valores a serem retirados.
        - `pilha_destino`: pilha a receber os valores na ordem inversa.

        *Complexidade:* O(n), pois a iteração cresce linearmente com o tamanho da pilha de origem.
        """
        while not pilha_origem.esta_vazia():
            pilha_destino.push(pilha_origem.pop())

    def desenfileirar(self):
        if len(self) == 0:
            raise IndexError("A fila está vazia!")
        if self._saida.esta_vazia():
            self.inverter_pilha(self._entrada, self._saida)
        return self._saida.pop()

    def frente(self):
        if len(self) == 0:
                raise IndexError("A fila está vazia!")
        if self._saida.esta_vazia():
            while not self._entrada.esta_vazia():
                self._saida.push(self._entrada.pop())
        return self._saida.topo()

    def esta_vazia(self):
        return len(self) == 0

    def __len__(self):
        return len(self._entrada) + len(self._saida)

    def __repr__(self):
        temp = PilhaEncadeada()
        self.inverter_pilha(self._entrada, temp)
        result = " -> ".join(s for s in (repr(self._saida), repr(temp)) if s)
        self.inverter_pilha(temp, self._entrada)
        return result