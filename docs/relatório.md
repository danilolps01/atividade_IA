# Relatório: Comparação da "inteligência" percebida entre as fases

Este projeto mostra, de forma prática, como a "inteligência" percebida em sistemas de linguagem evolui conforme muda a técnica utilizada. Na Fase 1, com a ELIZA, a conversa parece inteligente porque o sistema reconhece padrões e devolve perguntas que soam naturais. No entanto, essa inteligência é apenas superficial: o programa não entende o significado do que foi dito, apenas aplica regras predefinidas e reorganiza partes da fala do usuário.

Na Fase 2, com o modelo de N-Grams, a percepção muda. O sistema deixa de depender de regras fixas e passa a gerar texto com base em probabilidades observadas em um corpus. Isso representa um avanço importante, porque o comportamento passa a ser orientado por dados e não apenas por respostas programadas manualmente. Mesmo assim, a inteligência percebida continua limitada, já que o modelo considera um contexto muito curto e tende a produzir saídas localmente plausíveis, mas globalmente incoerentes.

Comparando as duas fases, a ELIZA parece mais "inteligente" em diálogos curtos, porque foi construída justamente para simular escuta e manter uma conversa minimamente convincente. Já o modelo de N-Grams parece mais "autônomo" na geração de frases, mas expõe com mais facilidade sua falta de compreensão quando o texto cresce ou quando o contexto exige coerência mais longa. Em outras palavras, a ELIZA engana melhor no formato de conversa, enquanto os N-Grams demonstram melhor a transição para sistemas estatísticos, embora ainda estejam longe de uma compreensão real.

Do ponto de vista da evolução do PLN, essas duas fases deixam claro que a inteligência percebida não depende apenas de responder alguma coisa, mas da capacidade de manter contexto, coerência, adaptação e adequação ao que o usuário espera. Esse salto só se torna mais evidente nas abordagens neurais e, depois, nos Transformers, que conseguem representar relações semânticas mais amplas e lidar com contextos muito maiores.

# Conclusão: Impacto do RLHF no resultado final

O RLHF (Reinforcement Learning from Human Feedback) tem papel decisivo no resultado final dos modelos modernos porque atua justamente na camada da inteligência percebida pelo usuário. Enquanto modelos anteriores podem gerar texto estatisticamente correto ou estruturalmente plausível, o RLHF ajuda a alinhar as respostas com preferências humanas, tornando-as mais úteis, claras, seguras e coerentes com a intenção da pergunta.

Na prática, isso significa que o RLHF não transforma um sistema simples como ELIZA ou N-Grams em um modelo realmente inteligente, mas nos modelos avançados ele melhora muito a qualidade da interação final. O usuário passa a perceber o sistema como mais inteligente não apenas porque ele gera texto, mas porque responde de forma mais relevante, organizada, contextual e colaborativa.

Assim, o impacto do RLHF está menos em "ensinar fatos" e mais em refinar comportamento. Ele reduz respostas confusas, melhora a adequação ao contexto, favorece explicações mais naturais e aproxima a saída do modelo daquilo que as pessoas consideram uma boa conversa. Por isso, no estágio final da evolução apresentada no trabalho, o RLHF é um dos principais responsáveis por transformar capacidade técnica em uma experiência de uso que parece, de fato, mais inteligente.
