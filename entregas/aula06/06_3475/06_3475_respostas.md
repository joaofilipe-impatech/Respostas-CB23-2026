### Justificativa para $\mathcal{O}(1)$ amortizado no método de desenfileirar
Para justificar a complexidade $\mathcal{O}(1)$ no método `desenfileirar()` da classe `FilaEncadeada`, considere a quantidade de vezes cada item é transferido entre as pilhas:

- 1 vez ao entrar na fila pela pilha de entrada
- 1 vez ao ir para a pilha de saída
- 1 vez ao sair da fila pela pilha de saída

Portanto, em geral, ao inserir $n$ elementos na fila, teremos $3n$ operações de transferência entre filas (que é $\mathcal{O}(1)$), o que nos leva a uma complexidade média de $\mathcal{O}(3n)=\mathcal{O}(n)$ no ciclo completo. Mas isso só é possível se remover um item da fila levar, em média, tempo $\mathcal{O}(1)$.

Veja que isso também faz sentido na prática: mesmo que a transferência da pilha de entrada para a de saída ocorra com algum $n$ grande com complexidade $\mathcal{O}(n)$, isso também significa que as próximas $n-1$ vezes que um item for removido terá complexidade $\mathcal{O}(1)$.