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
        Retira todos os itens da pilha de origem e os envia para a de destino, trocando a ordem.

        - `pilha_origem`: pilha com os valores a serem retirados.
        - `pilha_destino`: pilha a receber os valores na ordem inversa.

        *Complexidade:* O(n), pois a iteração cresce linearmente com o tamanho da pilha de origem.
        """
        while not pilha_origem.esta_vazia():
            pilha_destino.push(pilha_origem.pop())

    def desenfileirar(self):
        """
        Retira o primeiro item da fila e o devolve ao usuário.
        
        *Complexidade:* O(1) amortizado. O algoritmo roda em tempo O(n) no pior caso (i. e. quando é
        necessário transferir a pilha de entrada para a saída) devido à complexidade de inverter pilha.
        Entretanto, em todos os outros casos (que são a maioria), a complexidade é O(1).
        """
        if len(self) == 0:
            raise IndexError("A fila está vazia!")
        if self._saida.esta_vazia():
            self.inverter_pilha(self._entrada, self._saida)
        return self._saida.pop()

    def frente(self):
        """
        Devolve o primeiro item da fila sem removê-lo.
        
        *Complexidade:* O(1) amortizado. O algoritmo roda em tempo O(n) no pior caso (i. e. quando é
        necessário transferir a pilha de entrada para a saída) devido à complexidade de inverter pilha.
        Entretanto, em todos os outros casos (que são a maioria), a complexidade é O(1).
        """
        if len(self) == 0:
            raise IndexError("A fila está vazia!")
        if self._saida.esta_vazia():
            self.inverter_pilha(self._entrada, self._saida)
        return self._saida.topo()

    def esta_vazia(self):
        """
        Verifica se o tamanho da fila é 0

        *Complexidade:* O(1), pois o `len()` é O(1) e a comparação também é O(1)
        """
        return len(self) == 0

    def __len__(self):
        """
        Retorna o tamanho da fila, que é a soma do tamanho de cada fila.

        *Complexidade:* O(1), pois cada `len()` é O(1) e a soma também é O(1)
        """
        return len(self._entrada) + len(self._saida)

    def __repr__(self):
        """
        Retorna uma representação visual da fila na forma 'fim -> ... -> inicio'

        *Complexidade:* O(n), pois as operações de inverter pilha e representação de cada pilha é O(n)
        em relação ao comprimento de cada pilha, enquanto `join()` é linear com o comprimento das
        representações, que é O(n).
        """
        temp = PilhaEncadeada()
        self.inverter_pilha(self._entrada, temp)
        result = " -> ".join(s for s in (repr(self._saida), repr(temp)) if s)
        self.inverter_pilha(temp, self._entrada)
        return result