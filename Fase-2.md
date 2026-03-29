# Fase 2: Predição por N-Grams (Estatística e Bigramas)

Este documento detalha a implementação do gerador de texto baseado em N-Grams, a segunda fase do projeto "Da ELIZA aos Transformers". Esta fase marca um salto evolutivo fundamental: abandonar regras fixas e abraçar a probabilidade baseada na frequência de palavras em um corpus.

## Objetivo da Fase

Compreender a transição para a Revolução Estatística no Processamento de Linguagem Natural. O objetivo é implementar um modelo de Bigramas, onde o cálculo da probabilidade da palavra n é baseada apenas na palavra n-1, e analisar o impacto do contexto limitado na geração de texto.

## Como Rodar o Gerador N-Grams

Para testar o gerador estatístico de texto, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o Python 3.x instalado em seu sistema.
2.  **Navegue até o diretório:** Abra um terminal e navegue até o diretório onde o arquivo do algoritmo (ex: `ngram_generator.py`) está salvo.
3.  **Execute o script:** Digite o seguinte comando:
    `python ngram_generator.py`
4.  **Analise a Saída:** O script treinará o modelo silenciosamente usando o corpus de texto fornecido e imprimirá no terminal uma frase gerada estatisticamente.

## Funcionamento Técnico dos N-Grams

Diferente da ELIZA (Era Simbólica), este modelo não possui regras engessadas. Ele "aprende" a escrever calculando probabilidades matemáticas a partir de um texto de exemplo (corpus).

### 1. Tokenização e Normalização
Antes de qualquer cálculo, o texto de treinamento é limpo (remoção de pontuação, conversão para minúsculas) e dividido em uma lista sequencial de palavras (tokens).

### 2. Mapeamento de Frequência (Treinamento)
O algoritmo percorre a lista de tokens extraindo pares de palavras adjacentes (Bigramas). Ele mapeia cada palavra para todas as palavras que a sucedem, contando a frequência de cada ocorrência. 

### 3. Peso Matemático e Probabilidade
Na hora de gerar o texto, o algoritmo analisa a palavra atual e consulta o mapa de frequências. Exemplo prático: ao ler "O gato...", se o verbo "miou" apareceu 85% das vezes no texto original, "correu" 10% e "latiu" 5%, o modelo realiza um sorteio ponderado. A frequência dita a próxima palavra a ser escolhida.

### 4. Geração em Cadeia
O processo entra em loop. A palavra sorteada torna-se a nova base para o próximo sorteio, repetindo o ciclo até atingir o limite estipulado.

## Limitações

A abordagem estatística traz uma flexibilidade moderada em relação à ELIZA, mas expõe uma fraqueza crucial que será resolvida nas próximas fases:

* **Contexto Limitado ("Memória Curta"):** O contexto levado em consideração é muito curto (geralmente apenas 2 a 3 palavras). Em um modelo de Bigramas, a IA só olha para a palavra imediatamente anterior.
* **Incoerência em Textos Longos:** Devido ao contexto limitado, o algoritmo gera pares de palavras que fazem sentido localmente, mas a "memória" curta dos n-grams impede a geração de textos coerentes e longos.
* **Dependência Absoluta do Corpus:** O modelo é incapaz de inovar além do vocabulário e das transições exatas que "leu".
