# Organizador de arquivos

Script em Python que organiza uma pasta bagunçada (como Downloads) em subpastas por tipo.

## O problema

Pastas de Downloads acumulam dezenas de arquivos misturados e achar algo leva tempo.

## Como funciona

- Classifica cada arquivo pela extensão (Imagens, Documentos, Planilhas, Apresentações, Compactados, Áudio/Vídeo, Código, Outros).
- **Simulação por padrão:** sem `--executar`, só mostra o que seria movido.
- **Nunca sobrescreve:** se já existir um arquivo com o mesmo nome, o novo vira `nome (1).ext`.
- Ignora arquivos ocultos e subpastas.

## Uso

```bash
python organizar.py ~/Downloads             # simulação
python organizar.py ~/Downloads --executar  # move de verdade
```

Só usa a biblioteca padrão do Python (3.8+), sem instalar nada.

## Testes

```bash
python test_organizar.py
```

Cobrem classificação, simulação, movimentação, arquivos ocultos, nomes repetidos e pasta inexistente.

## Como foi feito

Escrito com ajuda de IA (Claude), a partir de uma descrição do problema e das regras de segurança desejadas (simular antes, não sobrescrever). Os testes foram executados antes de publicar.

## Resultado medido

_A preencher._ Para medir o ganho real: cronometre quanto leva para organizar uma pasta à mão e compare com o tempo do script. Registre aqui os números e a data.
