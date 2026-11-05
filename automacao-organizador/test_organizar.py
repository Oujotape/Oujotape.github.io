import tempfile
import unittest
from pathlib import Path

import organizar


class TestOrganizar(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.pasta = Path(self._tmp.name)
        for nome in ["foto.PNG", "relatorio.pdf", "dados.csv", "setup.exe", ".oculto"]:
            (self.pasta / nome).write_text("x")

    def tearDown(self):
        self._tmp.cleanup()

    def test_categorias(self):
        self.assertEqual(organizar.categoria_de(Path("foto.PNG")), "Imagens")
        self.assertEqual(organizar.categoria_de(Path("a.xlsx")), "Planilhas")
        self.assertEqual(organizar.categoria_de(Path("a.xyz")), "Outros")

    def test_simulacao_nao_move(self):
        organizar.main([str(self.pasta)])
        self.assertTrue((self.pasta / "foto.PNG").exists())
        self.assertFalse((self.pasta / "Imagens").exists())

    def test_executar_move_e_ignora_ocultos(self):
        organizar.main([str(self.pasta), "--executar"])
        self.assertTrue((self.pasta / "Imagens" / "foto.PNG").exists())
        self.assertTrue((self.pasta / "Documentos" / "relatorio.pdf").exists())
        self.assertTrue((self.pasta / "Planilhas" / "dados.csv").exists())
        self.assertTrue((self.pasta / "Outros" / "setup.exe").exists())
        self.assertTrue((self.pasta / ".oculto").exists())

    def test_nao_sobrescreve(self):
        (self.pasta / "Documentos").mkdir()
        (self.pasta / "Documentos" / "relatorio.pdf").write_text("antigo")
        organizar.main([str(self.pasta), "--executar"])
        self.assertEqual((self.pasta / "Documentos" / "relatorio.pdf").read_text(), "antigo")
        self.assertTrue((self.pasta / "Documentos" / "relatorio (1).pdf").exists())

    def test_pasta_inexistente(self):
        self.assertEqual(organizar.main(["/caminho/que/nao/existe"]), 1)


if __name__ == "__main__":
    unittest.main()
