class PilhaEncadeada:
    class _No:
        def __init__(self, valor, ponteiro=None):
            self.valor = valor
            self.ponteiro = ponteiro
    
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        """
        Insere o item no topo da pilha.

        - `item`: valor a ser guardado na pilha.

        *Complexidade:* O(1), pois a criação de um nó, a atribuição de variável e o incremento não mudam
        com o tamanho da pilha, ou seja, cada um deles é O(1), pelo que a soma final também é O(1).
        """
        novo_no = self._No(item, self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        """
        Retorna o item no topo da pilha, removendo-o.
        Caso não haja elementos na pilha, levanta um IndexError.

        *Complexidade:* O(1), pois o condicional, a atribuição de variável e o incremento não mudam com o
        tamanho da pilha, ou seja, cada um deles é O(1), pelo que a soma final também é O(1).
        """
        if len(self) == 0:
            raise IndexError("A pilha está vazia!")
        no_apagado = self._topo
        self._topo = no_apagado.ponteiro
        self._tamanho -= 1
        return no_apagado.valor

    def topo(self):
        """
        Retorna o item no topo da pilha, sem remover.
        Caso não haja elementos na pilha, levanta um IndexError.

        *Complexidade:* O(1), pois a condicional não muda com o tamanho da pilha, ou seja, é O(1).
        """
        if len(self) == 0:
            raise IndexError("A pilha está vazia!")
        return self._topo

    def esta_vazia(self):
        """
        Retorna um booleano indicando se a pilha está vazia.

        *Complexidade:* O(1), pois a comparação não muda com o tamanho da pilha, ou seja, é O(1).
        """
        return len(self) == 0

    def __len__(self):
        """
        Retorna o tamanho da pilha.

        *Complexidade:* O(1), pois o acesso à memória não muda com o tamanho da pilha, ou seja, é O(1).
        """
        return self._tamanho

    def __repr__(self):
        """
        Retorna uma representação visual da pilha na forma 'topo -> ... -> base'.

        *Complexidade:* O(n), pois a iteração sobre os elementos cresce linearmente com o tamanho da pilha,
        mas cada operação dentro da iteração é O(1).
        """
        elementos = []
        proximo_no = self._topo
        while proximo_no is not None:
            elementos.append(str(proximo_no.valor))
            proximo_no = proximo_no.ponteiro
        return " -> ".join(elementos)