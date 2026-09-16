# python 3

"""
maze_builder.py
---------------
Geração procedural de labirintos perfeitos usando busca em profundidade (DFS)
com retrocesso (backtracking).

Um labirinto "perfeito" possui exactamente um caminho entre quaisquer dois
pontos — equivalente a uma árvore geradora aleatória sobre a grade m x n.

Representação interna
~~~~~~~~~~~~~~~~~~~~~
A grade lógica de m linhas X n colunas é expandida para uma matriz de
(2m+1) X (2n+1) células, onde:
  - células de coordenadas ímpares (2i+1, 2j+1) representam salas (rooms);
  - células entre duas salas adjacentes representam paredes derrubáveis;
  - as bordas externas são sempre paredes.

O queijo (cheese) é colocado aleatoriamente em qualquer sala.
"""

import random


def generate_maze(m, n, room=0, wall=1, cheese='.', iter=False):
    """Gera um labirinto perfeito de m X n células usando DFS com backtracking.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):
        """Abre passagens recursivamente a partir da sala (x, y)."""
        maze[2 * x + 1][2 * y + 1] = room

        # Ordem aleatória garante labirintos distintos a cada execução
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                # Derruba a parede entre (x,y) e (nx,ny)
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                dfs(nx, ny)

    def dfs_iter(x, y):
        """Abre passagens recursivamente a partir da sala (x, y)."""
        maze[2 * x + 1][2 * y + 1] = room

        # Um detalhe interessante sobre o código dfs() original é que há um problema quando
        # ocorre a recursão: como o random.shuffle() é in-place, as chamadas posteriores
        # afetam as direções dos nós anteriores quando fazemos o backtracking. Uma abordagem
        # para resolver isso foi armazenar as direções para cada nó visitado (o que acaba
        # aumentando o consumo de memória, infelizmente).

        pilha = [(x, y, random.sample(directions, 4))]

        while len(pilha) != 0:
            xa, ya, dirs = pilha[-1]

            if len(dirs) == 0:
                pilha.pop()
                continue

            dx, dy = dirs.pop()
            nx, ny = xa + dx, ya + dy

            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                # Derruba a parede entre (x,y) e (nx,ny)
                maze[2 * xa + 1 + dx][2 * ya + 1 + dy] = room
                maze[2 * nx + 1][2 * ny + 1] = room

                pilha.append((nx, ny, random.sample(directions, 4)))

    # Inicia a DFS no canto superior-esquerdo da grade lógica
    if iter:
        dfs_iter(0, 0)
    else:
        dfs(0, 0)

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print("".join(map(str, row)))


def solve_maze(maze):
    room, wall = maze[1][1], maze[0][0]
    x, y = 1, 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    para_visitar = [(x, y, random.sample(directions, 4))]
    visitados = set((1, 1))

    while len(para_visitar) != 0:
        x, y, dirs = para_visitar[-1]

        if maze[x][y] not in (room, wall):
            caminho = [(coord_x, coord_y) for coord_x, coord_y, _ in para_visitar]
            for a, b in caminho:
                maze[a][b] = '\u25cf '
            maze[x][y] = '🧀'
            print_maze(maze)
            return caminho

        if len(dirs) == 0:
            para_visitar.pop()
            continue
            
        dx, dy = dirs.pop()
        nx, ny = x + dx, y + dy

        if (nx, ny) not in visitados and maze[nx][ny] != wall:
            para_visitar.append((nx, ny, random.sample(directions, 4)))
            visitados.add((nx, ny))
    return None


        
# Example usage:
if __name__ == '__main__':
    m, n = 30, 20  # Grid size
    # random.seed(3)
    room = '  '
    wall = '\u2588\u2588'
    cheese = '🧀'

    maze = generate_maze(m, n, room, wall, cheese, True)
    print('Maze 1')
    print_maze(maze)
    print()

    # maze = generate_maze(m, n, room, wall, cheese)
    # print('\nMaze 2')
    # print_maze(maze)
    solve_maze(maze)
