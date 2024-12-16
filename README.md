
# Descrição do Projeto

Este projeto contém um script Python que remove informações temporais de textos. O objetivo principal é limpar textos que contêm intervalos de tempo no formato `HH:MM:SS - HH:MM:SS` e retornar o conteúdo sem essas marcações temporais.

## Funcionalidade

1. **Entrada de Texto com Marcações Temporais**: O script processa textos com intervalos de tempo no formato `00:00:00 - 00:00:11`.
2. **Remoção de Timestamps**: Utiliza expressões regulares (regex) para identificar e remover as marcações temporais.
3. **Saída Limpa**: O texto resultante é exibido sem os horários, deixando apenas o conteúdo textual relevante.

## Exemplo de Entrada

```text
00:00:00 - 00:00:11
os recursos talvez esse seja o assunto
00:00:09 - 00:00:14
mais importante o que diz respeito à
00:00:11 - 00:00:18
modelagem de um contrato flash bem feito
00:00:14 - 00:00:21
porque é o ponto em que eu exijo mais
00:00:18 - 00:00:25
inteligência de análise de entender como
00:00:21 - 00:00:28
é o negócio e como traduzir e recursos
```

## Exemplo de Saída

```text
os recursos talvez esse seja o assunto
mais importante o que diz respeito à
modelagem de um contrato flash bem feito
porque é o ponto em que eu exijo mais
inteligência de análise de entender como
é o negócio e como traduzir e recursos
```

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **Regex (expressões regulares)**: Para identificar e manipular os intervalos de tempo no texto.

## Potenciais Aplicações

- Processamento de transcrições de vídeos, podcasts ou qualquer conteúdo com marcações temporais.
- Limpeza de dados textuais, como logs ou relatórios.
- Preparação de conteúdo textual para apresentações ou publicações.
