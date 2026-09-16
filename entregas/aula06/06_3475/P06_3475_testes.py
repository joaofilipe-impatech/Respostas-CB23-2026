from P06_3475_pilha_encadeada import PilhaEncadeada
from P06_3475_fila_encadeada import FilaEncadeada
import unittest

class TestePilha(unittest.TestCase):
    def setUp(self):
        self.pilha = PilhaEncadeada()

    def test_lifo_ordem(self):
        self.pilha.push('a')
        self.pilha.push('b')
        self.pilha.push('c')

        self.assertEqual(self.pilha.pop(), 'c')
        self.assertEqual(self.pilha.pop(), 'b')
        self.assertEqual(self.pilha.pop(), 'a')

    def test_excecoes_pilha_vazia(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()

        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_len(self):
        self.assertEqual(len(self.pilha), 0)

        self.pilha.push('a')
        self.pilha.push('b')
        self.pilha.push('c')

        self.assertEqual(len(self.pilha), 3)

        self.pilha.pop()
        self.pilha.pop()

        self.assertEqual(len(self.pilha), 1)

    def test_operacoes_alternadas(self):
        self.pilha.push('a')
        self.pilha.push('b')

        self.assertEqual(self.pilha.topo(), 'b')

        self.pilha.push('c')
        self.pilha.push('d')

        self.assertEqual(self.pilha.pop(), 'd')
        self.assertEqual(self.pilha.pop(), 'c')

        self.pilha.push('e')

        self.assertEqual(self.pilha.pop(), 'e')
        self.assertEqual(self.pilha.pop(), 'b')

        self.pilha.push('f')

        self.assertEqual(self.pilha.pop(), 'f')
        self.assertEqual(self.pilha.pop(), 'a')

    def test_tipos_diferentes_repetidos_none(self):
        self.pilha.push(10)
        self.pilha.push("texto")
        self.pilha.push(None)
        self.pilha.push(10)

        self.assertEqual(self.pilha.pop(), 10)
        self.assertIsNone(self.pilha.pop())
        self.assertEqual(self.pilha.pop(), "texto")
        self.assertEqual(self.pilha.pop(), 10)



class TesteFila(unittest.TestCase):
    def setUp(self):
        self.fila = FilaEncadeada()

    def test_fifo_ordem(self):
        self.fila.enfileirar('a')
        self.fila.enfileirar('b')
        self.fila.enfileirar('c')

        self.assertEqual(self.fila.desenfileirar(), 'a')
        self.assertEqual(self.fila.desenfileirar(), 'b')
        self.assertEqual(self.fila.desenfileirar(), 'c')

    def test_excecoes_fila_vazia(self):
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()

        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_coerencia_len(self):
        self.assertEqual(len(self.fila), 0)
        
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.assertEqual(len(self.fila), 2)
        
        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 1)
        
        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 0)

    def test_operacoes_alternadas(self):
        self.fila.enfileirar('a')
        self.fila.enfileirar('b')
        self.assertEqual(self.fila.desenfileirar(), 'a')
        
        self.fila.enfileirar('c')
        self.assertEqual(self.fila.desenfileirar(), 'b')
        
        self.assertEqual(self.fila.desenfileirar(), 'c')
        self.assertTrue(self.fila.esta_vazia())

        self.fila.enfileirar('x')
        self.fila.enfileirar('y')
        self.assertEqual(self.fila.desenfileirar(), 'x')
        self.assertEqual(self.fila.frente(), 'y')
        self.assertEqual(self.fila.desenfileirar(), 'y')



if __name__ == "__main__":
    unittest.main()