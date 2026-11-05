#!/usr/bin/env python3
"""Organizador de arquivos.

Move os arquivos de uma pasta (por exemplo, Downloads) para subpastas por tipo
(Imagens, Documentos, Planilhas, etc.). Por padrão só MOSTRA o que faria
(--executar é necessário para mover de verdade) e nunca sobrescreve arquivos.

Uso:
    python organizar.py ~/Downloads             # simulação
    python organizar.py ~/Downloads --executar  # move de verdade
"""
import argparse
import shutil
import sys
import time
from pathlib import Path

CATEGORIAS = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".heic"},
    "Documentos": {".pdf", ".doc", ".docx", ".txt", ".odt", ".md"},
    "Planilhas": {".xls", ".xlsx", ".csv", ".ods"},
    "Apresentacoes": {".ppt", ".pptx", ".odp", ".key"},
    "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Audio_Video": {".mp3", ".wav", ".mp4", ".mov", ".mkv", ".avi"},
    "Codigo": {".py", ".js", ".html", ".css", ".json", ".ipynb"},
}


def categoria_de(arquivo: Path) -> str:
    ext = arquivo.suffix.lower()
    for nome, extensoes in CATEGORIAS.items():
        if ext in extensoes:
            return nome
    return "Outros"


def destino_livre(destino: Path) -> Path:
    """Se já existir um arquivo com o mesmo nome, acrescenta (1), (2)..."""
    if not destino.exists():
        return destino
    n = 1
    while True:
        candidato = destino.with_name(f"{destino.stem} ({n}){destino.suffix}")
        if not candidato.exists():
            return candidato
        n += 1


def planejar(pasta: Path):
    """Devolve a lista de (origem, destino) sem mover nada."""
    plano = []
    for item in sorted(pasta.iterdir()):
        if not item.is_file() or item.name.startswith("."):
            continue
        destino = pasta / categoria_de(item) / item.name
        plano.append((item, destino))
    return plano


def executar(plano):
    movidos = 0
    for origem, destino in plano:
        destino.parent.mkdir(exist_ok=True)
        shutil.move(str(origem), str(destino_livre(destino)))
        movidos += 1
    return movidos


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Organiza arquivos por tipo.")
    parser.add_argument("pasta", type=Path)
    parser.add_argument("--executar", action="store_true",
                        help="move de verdade (sem isso, apenas simula)")
    args = parser.parse_args(argv)

    if not args.pasta.is_dir():
        print(f"Pasta não encontrada: {args.pasta}", file=sys.stderr)
        return 1

    inicio = time.perf_counter()
    plano = planejar(args.pasta)
    for origem, destino in plano:
        print(f"{origem.name}  ->  {destino.parent.name}/")

    if not plano:
        print("Nada para organizar.")
        return 0

    if args.executar:
        movidos = executar(plano)
        print(f"\n{movidos} arquivo(s) movido(s) em {time.perf_counter() - inicio:.2f}s.")
    else:
        print(f"\nSimulação: {len(plano)} arquivo(s) seriam movidos. "
              "Rode com --executar para aplicar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
