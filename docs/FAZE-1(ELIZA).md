# Fase 1: O Psicólogo de Terminal (ELIZA)

Este documento detalha a implementação do chatbot ELIZA, a primeira fase do projeto "Da ELIZA aos Transformers: A Evolução do Processamento de Linguagem Natural". Esta fase explora os fundamentos dos sistemas de PLN baseados em regras, demonstrando como a ilusão de compreensão pode ser criada através de padrões textuais simples.

## Objetivo da Fase

Compreender os princípios dos sistemas de Processamento de Linguagem Natural baseados em regras, implementando um chatbot que simula a ELIZA original (1966) e analisando suas capacidades e limitações.

## Como Rodar o Chatbot ELIZA

Para interagir com o chatbot ELIZA, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o Python 3.x instalado em seu sistema.
2.  **Navegue até o diretório:** Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo `eliza_chatbot.py` está salvo.
3.  **Execute o script:** Digite o seguinte comando:
    ```bash
    python eliza_chatbot.py
    ```
4.  **Interaja:** O chatbot iniciará a conversa. Digite suas mensagens e pressione Enter. Para encerrar a sessão, digite `sair`.

## Funcionamento Técnico do ELIZA

O chatbot ELIZA opera com base em um conjunto de regras e padrões predefinidos, sem qualquer compreensão semântica real da linguagem. Sua "inteligência" é uma ilusão criada por:

### 1. Expressões Regulares (Regex)

O coração da ELIZA são as expressões regulares. Elas são usadas para identificar padrões específicos na entrada do usuário. Por exemplo, o padrão `r'.*eu estou (.*)'` procura por frases que contenham "eu estou" e captura o que vem depois (o `(.*)`).

### 2. Grupos de Captura e Reflexão

Quando um padrão é encontrado, o texto capturado pelos grupos de parênteses no Regex é extraído. Este texto é então processado por uma função de `reflexão` que inverte pronomes e verbos (ex: "eu" vira "você", "meu" vira "seu"). Isso permite que a ELIZA reformule a frase do usuário em uma pergunta reflexiva.

### 3. Dicionário de Regras (`rules`)

Um dicionário (`rules`) armazena pares de padrões Regex e listas de respostas. Para cada padrão, há várias respostas possíveis, e uma é escolhida aleatoriamente para evitar repetição. As respostas utilizam placeholders `{0}` que são preenchidos com o texto refletido do usuário.

### 4. Memória Simples

Uma lista (`last_user_phrases`) mantém um histórico limitado das últimas frases do usuário. Ocasionalmente, a ELIZA pode "lembrar" de algo que foi dito anteriormente e fazer uma pergunta relacionada, criando uma sensação de continuidade na conversa.

### 5. Resposta Genérica (Fallback)

Caso nenhuma das regras específicas corresponda à entrada do usuário, há uma regra genérica (`r'.*'`) que fornece respostas abertas como "Por favor, elabore um pouco mais." ou "Como isso faz você se sentir?". Isso garante que a ELIZA sempre tenha uma resposta, mesmo quando não "entende" a mensagem.

## Limitações

Apesar de sua capacidade de simular uma conversa, a ELIZA possui limitações significativas:

*   **Falta de Compreensão Semântica:** Ela não entende o significado das palavras ou o contexto real da conversa. Apenas manipula símbolos.
*   **Rigidez:** É limitada aos padrões predefinidos. Frases que não se encaixam em nenhuma regra resultam em respostas genéricas ou irrelevantes.
*   **Ausência de Raciocínio:** Não consegue inferir, aprender com a conversa (além da memória de curto prazo) ou gerar informações novas.

Esta fase serve como um ponto de partida para entender a evolução do PLN, destacando a necessidade de abordagens mais sofisticadas para a compreensão da linguagem natural.
