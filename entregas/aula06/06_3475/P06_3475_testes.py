from P06_3475_pilha_encadeada import PilhaEncadeada
from P06_3475_fila_encadeada import FilaEncadeada

if __name__ == "__main__":
    pilha = PilhaEncadeada()
    print(pilha.esta_vazia())
    # pilha.pop()

    pilha.push('programação')
    pilha.push('calculo')
    pilha.push('algebra linear')
    print(repr(pilha))
    print(len(pilha))
    print(pilha.esta_vazia())
    print(pilha.pop())
    print(repr(pilha))
    print(len(pilha))

    print("==============================")

    fila = FilaEncadeada()
    # fila.desenfileirar()

    fila.enfileirar('programação')
    fila.enfileirar('calculo')
    fila.enfileirar('algebra linear')
    print(repr(fila))
    print(fila.desenfileirar())
    print(repr(fila))