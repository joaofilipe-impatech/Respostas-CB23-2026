from P06_3475_pilha_encadeada import PilhaEncadeada
from P06_3475_fila_encadeada import FilaEncadeada
import unittest

class TestePilha(unittest.TestCase):
    def setUp(self):
        self.pilha = PilhaEncadeada()

    def test_lifo_pushpopsequence(self):
        self.pilha.push('a')
        self.pilha.push('b')
        self.pilha.push('c')

        self.assertEqual(self.pilha.pop(), 'c')
        self.assertEqual(self.pilha.pop(), 'b')
        self.assertEqual(self.pilha.pop(), 'a')

    def test_poptopo_vazio(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()

        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_len(self):
        self.assertEqual(len(self.pilha), 0)

        self.pilha.push('a')
        self.pilha.push('b')
        self.pilha.push('c')

        self.assertEqual(len(self.pilha), 3)

        self.pilha.pop()
        self.pilha.pop()

        self.assertEqual(len(self.pilha), 1)

    def test_alternating_operations(self):
        self.pilha.push('a')
        self.pilha.push('b')
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



if __name__ == "__main__":
    unittest.main()