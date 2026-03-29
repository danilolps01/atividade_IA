import re
import random

# Lista para armazenar as últimas frases do usuário para uma "memória" simples
last_user_phrases = []
MAX_MEMORY = 3

def eliza_response(user_input):
    global last_user_phrases
    user_input_lower = user_input.lower()

    # Adiciona a frase do usuário à memória
    last_user_phrases.append(user_input_lower)
    if len(last_user_phrases) > MAX_MEMORY:
        last_user_phrases.pop(0)

    # Substituições de pronomes para respostas mais naturais
    reflections = {
        "eu": "você",
        "me": "você",
        "meu": "seu",
        "minha": "sua",
        "você": "eu",
        "seu": "meu",
        "sua": "minha",
        "estou": "está",
        "sou": "é",
        "fui": "foi",
        "minhas": "suas",
        "meus": "seus",
        "nós": "vocês",
        "nosso": "seu",
        "nossa": "sua"
    }

    def reflect(fragment):
        words = fragment.split()
        reflected_words = [reflections.get(word, word) for word in words]
        return ' '.join(reflected_words)

    # Regras e respostas para o chatbot ELIZA
    rules = {
        r'.*eu preciso de (.*)': [
            'Por que você precisa de {0}?',
            'Isso faria você feliz se você tivesse {0}?',
            'Você realmente acha que eu posso te ajudar a conseguir {0}?'
        ],
        r'.*eu não posso (.*)': [
            'Como você sabe que não pode {0}?',
            'Você gostaria de poder {0}?',
            'O que seria necessário para você poder {0}?'
        ],
        r'.*eu sou (.*)': [
            'Você veio até mim porque você é {0}?',
            'Você realmente é {0}?',
            'Como você se sente sendo {0}?'
        ],
        r'.*eu estou (.*)': [
            'Você veio até mim porque você está {0}?',
            'Há quanto tempo você está {0}?',
            'Você se sente feliz estando {0}?'
        ],
        r'.*eu sinto (.*)': [
            'Por que você me diz que sente {0}?',
            'Você costuma sentir {0}?',
            'Quando você se sente {0}?'
        ],
        r'.*minha (.*)': [
            'Conte-me mais sobre sua {0}.',
            'Sua {0} é importante para você?',
            'Como sua {0} te afeta?'
        ],
        r'.*você é (.*)': [
            'Por que você se importa se eu sou {0}?',
            'Você gostaria que eu fosse {0}?',
            'Talvez você queira que eu seja {0}.'
        ],
        r'.*sempre (.*)': [
            'Você pode pensar em um exemplo específico?',
            'Quando?',
            'O que isso significa para você?'
        ],
        r'.*o que (.*)': [
            'Por que você pergunta?',
            'O que você acha?',
            'Você realmente não sabe o que {0}?'
        ],
        r'.*quem (.*)': [
            'Por que você pergunta?',
            'Você acha que quem {0}?',
            'Você gostaria de saber quem {0}?'
        ],
        r'.*quando (.*)': [
            'Você tem algum interesse em quando {0}?',
            'O que você acha sobre quando {0}?',
            'Você gostaria de saber quando {0}?'
        ],
        r'.*onde (.*)': [
            'Você tem algum interesse em onde {0}?',
            'O que você acha sobre onde {0}?',
            'Você gostaria de saber onde {0}?'
        ],
        r'.*por que (.*)': [
            'Isso é uma boa pergunta. Por que você acha {0}?',
            'Você tem alguma ideia do porquê {0}?',
            'Você realmente quer saber por que {0}?'
        ],
        r'.*sim': [
            'Você parece bastante certo.',
            'Você pode elaborar um pouco mais?',
            'Por que sim?'
        ],
        r'.*não': [
            'Por que não?',
            'Você está com medo de não?',
            'Você realmente não quer?'
        ],
        r'.*olá|oi|bom dia|boa tarde|boa noite': [
            'Olá. Como posso ajudar você hoje?',
            'Olá, como você está se sentindo hoje?',
            'Oi. O que te traz aqui?'
        ],
        r'.*adeus|tchau|até logo': [
            'Adeus. Espero que tenhamos conversado novamente.',
            'Tchau. Cuide-se.',
            'Até logo. Volte sempre.'
        ],
        r'.*família|familiares|pais|mãe|pai|irmão|irmã': [
            'Conte-me mais sobre sua família.',
            'Como sua família te afeta?',
            'Você se sente compreendido por sua família?'
        ],
        r'.*trabalho|emprego|carreira': [
            'Como está seu trabalho?',
            'Você se sente realizado em sua carreira?',
            'O que você gostaria de mudar em seu trabalho?'
        ],
        r'.*sonho|sonhos': [
            'Você se lembra de seus sonhos com frequência?',
            'O que seus sonhos significam para você?',
            'Você tem algum sonho que gostaria de realizar?'
        ],
        r'.*problema|dificuldade|questão': [
            'Você pode descrever o problema com mais detalhes?',
            'Como você se sente em relação a essa dificuldade?',
            'O que você já tentou para resolver essa questão?'
        ],
        r'.*medo|ansiedade|preocupação': [
            'O que te causa esse medo?',
            'Você se sente ansioso com frequência?',
            'O que você faz para lidar com suas preocupações?'
        ],
        r'.*feliz|alegre|contente': [
            'O que te faz feliz?',
            'Há quanto tempo você se sente feliz?',
            'Você compartilha sua alegria com outras pessoas?'
        ],
        r'.*sozinho|solitário': [
            'Você se sente sozinho com frequência?',
            'O que você faz quando se sente solitário?',
            'Você gostaria de ter mais companhia?'
        ],
        r'.*ajuda|socorro': [
            'Como posso te ajudar?',
            'O que você espera de mim?',
            'Você já procurou ajuda antes?'
        ],
        r'.*porque (.*)': [
            'Você acha que {0} é a razão?',
            'Isso é interessante. Continue.',
            'Você tem certeza de que {0} é a causa?'
        ],
        r'.*eu gostaria de (.*)': [
            'O que te impede de {0}?',
            'Por que você gostaria de {0}?',
            'Como você se sentiria se pudesse {0}?'
        ],
        r'.*você me entende': [
            'Eu me esforço para entender você. O que te faz perguntar isso?',
            'Você sente que não está sendo compreendido?',
            'O que eu poderia fazer para te entender melhor?'
        ],
        r'.*lembra de (.*)': [
            'Você se refere a algo que você mencionou anteriormente?',
            'Por que você quer saber se eu lembro de {0}?',
            'Minha função é te ouvir. O que você gostaria de me dizer sobre {0}?'
        ],
        r'.*': [
            'Por favor, elabore um pouco mais.',
            'Você pode me dizer mais sobre isso?',
            'Entendo. E o que mais?',
            'Como isso faz você se sentir?',
            'Isso é interessante. Continue.',
            'Você já pensou sobre isso antes?',
            'O que você acha que isso significa?'
        ]
    }

    # Tenta usar a memória ocasionalmente
    if random.random() < 0.2 and last_user_phrases and len(last_user_phrases) > 1:
        # Tenta pegar uma frase anterior que não seja a última
        previous_phrase = random.choice(last_user_phrases[:-1])
        if 'eu estou' in previous_phrase:
            match = re.search(r'eu estou (.*)', previous_phrase)
            if match:
                return f'Você mencionou que estava {reflect(match.group(1))}. Você ainda se sente assim?'
        elif 'eu sinto' in previous_phrase:
            match = re.search(r'eu sinto (.*)', previous_phrase)
            if match:
                return f'Você disse que sentia {reflect(match.group(1))}. Isso ainda é verdade?'
        elif 'eu preciso de' in previous_phrase:
            match = re.search(r'eu preciso de (.*)', previous_phrase)
            if match:
                return f'Você ainda precisa de {reflect(match.group(1))}?'

    for pattern, responses in rules.items():
        match = re.match(pattern, user_input_lower)
        if match:
            # Se houver grupos de captura, refletir o primeiro grupo
            if match.groups():
                response_fragment = reflect(match.group(1))
                return random.choice(responses).format(response_fragment)
            else:
                return random.choice(responses)
    return random.choice(rules[r'.*'])

if __name__ == "__main__":
    print("Olá. Eu sou ELIZA, sua terapeuta virtual. Como posso ajudar você hoje? (Digite 'sair' para encerrar)")
    while True:
        user_message = input("> ")
        if user_message.lower() == 'sair':
            print("Adeus. Espero que tenhamos conversado novamente.")
            break
        response = eliza_response(user_message)
        print(response)
