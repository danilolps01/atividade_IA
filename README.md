# Da ELIZA aos Transformers: A Evolução do PLN

Este repositório contém a entrega da atividade acadêmica "Da ELIZA aos Transformers: A Evolução do Processamento de Linguagem Natural em 15 Dias". 

## Proposta e Objetivo do Projeto

O objetivo principal desta atividade é compreender a transição de sistemas de regras rígidas baseados em símbolos para os modernos modelos estatísticos, neurais e baseados em atenção. 

O projeto mapeia uma jornada de aprendizado dividida em fases, demonstrando a evolução tecnológica da inteligência artificial aplicada ao texto:
* **Fase 1 (Era Simbólica):** O uso de scripts inspirados na ELIZA, com mapeamento de intenções simples e expressões regulares (Regex).
* **Fase 2 (Revolução Estatística):** O abandono de regras fixas para abraçar a probabilidade baseada na frequência de palavras em um corpus (Predição por N-Grams).
* **Fases 3 e 4 (Contexto Teórico):** A evolução para Word Embeddings (vetores e contexto) e a lógica dos Transformers (processamento paralelo e Self-Attention).

Conforme os critérios de entrega, este repositório foca na implementação funcional das duas primeiras abordagens (Chatbot ELIZA e Gerador N-Grams), acompanhada de um relatório analítico sobre a "inteligência" percebida entre as fases e o impacto do RLHF.

---

## Estrutura do Repositório

* `src/eliza_chatbot.py`: Implementação da **Fase 1**, explorando a Era Simbólica com regras fixas.
* `src/ngram_generator.py`: Implementação da **Fase 2**, explorando a Revolução Estatística com cálculo de probabilidade.
* `docs/relatorio_fases.pdf` (ou .md): Relatório analítico comparativo e conclusão sobre o RLHF.

## Como Executar os Scripts

Certifique-se de ter o Python 3.x instalado em sua máquina. Nenhuma biblioteca externa (`pip`) é necessária para estas implementações base.

### Fase 1: Chatbot ELIZA
Navegue até a pasta `src` e execute:
``` bash
  
python eliza_chatbot.py
  
```
*Interaja com o bot no terminal e digite `sair` para encerrar.*

### Fase 2: Gerador N-Grams (Bigramas)
Navegue até a pasta `src` e execute:
``` bash
   
python ngram_generator.py
  
```
*O script treinará o modelo com o corpus interno e imprimirá uma frase gerada estatisticamente.*

## Relatório e Análise
A discussão detalhada sobre a comparação das abordagens (Simbólica vs. Estatística vs. Neural) e a conclusão sobre o papel do RLHF (Reinforcement Learning from Human Feedback) no resultado final encontram-se no documento de relatório dentro da pasta `docs/`.
