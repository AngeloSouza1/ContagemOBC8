import unittest
from modulo_niveis import calcular_niveis_exclusivos

class TestCalcularNiveisExclusivos(unittest.TestCase):
    def test_experiencias_basicas(self):
        # Caso base do exemplo fornecido
        self.assertEqual(calcular_niveis_exclusivos([100, 300, 250, 500]), 4)
    
    def test_todos_menores_que_200(self):
        # Nenhuma experiência completa níveis
        self.assertEqual(calcular_niveis_exclusivos([100, 150, 199]), 0)

    def test_todos_maiores_que_200(self):
        # Todos valores completam níveis diretamente
        self.assertEqual(calcular_niveis_exclusivos([200, 400, 600]), 6)

    def test_mistura_de_valores(self):
        # Mistura de valores que completam e não completam níveis
        self.assertEqual(calcular_niveis_exclusivos([50, 200, 350, 150, 400]), 4)

    def test_lista_vazia(self):
        # Sem experiências fornecidas
        self.assertEqual(calcular_niveis_exclusivos([]), 0)

if __name__ == "__main__":
    unittest.main()
