# Prompts e experimentos com LLMs

Biblioteca de prompts estruturados e um registro de como eu os melhoro iterando.

## Estrutura que uso em todo prompt

1. **Papel:** quem o modelo deve ser.
2. **Contexto:** a situação e para quem é a resposta.
3. **Tarefa:** o que exatamente fazer, em uma frase.
4. **Regras e restrições:** o que evitar, tamanho, tom.
5. **Formato de saída:** lista, tabela, JSON, etc.
6. **Exemplo** (quando o formato é difícil de descrever).

## Prompts

### 1. Resumo de texto para decisão

```
Você é um analista que prepara resumos para quem tem pouco tempo.

Contexto: o texto abaixo é um relatório interno. O leitor precisa decidir se aprova ou não a proposta.

Tarefa: resuma o texto.

Regras:
- No máximo 5 tópicos.
- Não invente informações que não estejam no texto.
- Se faltar dado importante para decidir, liste em "Lacunas".

Formato:
**Resumo:** (2 frases)
**Pontos principais:** (tópicos)
**Lacunas:** (tópicos ou "nenhuma")

Texto:
{{texto}}
```

### 2. Revisão de código

```
Você é um revisor de código sênior, didático e direto.

Contexto: sou iniciante e este código foi gerado com ajuda de IA.

Tarefa: revise o código abaixo.

Regras:
- Aponte bugs e riscos de segurança primeiro (chaves expostas, entrada não validada).
- Depois sugira melhorias de legibilidade.
- Para cada ponto, explique o motivo em uma frase simples.

Formato: lista numerada, do mais grave ao menos grave.

Código:
{{codigo}}
```

### 3. Extração de dados em JSON

```
Extraia do texto os campos abaixo. Se um campo não aparecer, use null. Não deduza valores.

Campos: nome, empresa, cargo, email, telefone.

Responda somente com JSON válido, sem texto antes ou depois.

Texto:
{{texto}}
```

## Registro de experimentos

Cada experimento segue este modelo. Só registro resultado depois de testar de verdade.

| Item | Descrição |
|---|---|
| **Objetivo** | O que eu queria que o modelo fizesse |
| **Modelo e data** | Qual modelo usei e quando |
| **Versão 1** | Prompt inicial |
| **Problema observado** | O que saiu errado ou fraco |
| **Versão 2** | O que mudei no prompt |
| **Resultado** | O que melhorou (com exemplo real) |
| **Aprendizado** | O que levo para os próximos prompts |

### Experimentos feitos

_Nenhum registrado ainda. Primeiro a fazer: testar o prompt 1 com três textos de tamanhos diferentes e comparar a versão curta ("resuma este texto") com a versão estruturada._

## Lições que vou testar

- Dar formato de saída explícito reduz respostas fora do padrão?
- Pedir "não invente" reduz informações inventadas em textos curtos?
- Incluir um exemplo melhora a extração em JSON?
