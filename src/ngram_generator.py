import random
import re
from collections import defaultdict, Counter

class BigramGenerator:
    def __init__(self):
        # defaultdict(Counter) cria automaticamente um dicionário aninhado 
        # perfeito para contar frequências: {palavra: {proxima_palavra: contagem}}
        self.corpus_map = defaultdict(Counter)

    def train(self, text: str):
        """Treina o modelo com base na frequência das palavras em um corpus."""
        # Normaliza o texto (converte para minúsculas e remove pontuação básica)
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        
        # Tokeniza quebrando a string por espaços
        words = text.split()

        # Constrói o mapa de frequências (Bigramas)
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            # Incrementa a contagem de next_word que aparece logo após current_word
            self.corpus_map[current_word][next_word] += 1

    def get_next_word(self, word: str) -> str:
        """Escolhe a próxima palavra com base nos pesos matemáticos (probabilidade)."""
        # Se a palavra não existe no corpus ou não tem uma palavra seguinte registrada
        if word not in self.corpus_map or not self.corpus_map[word]:
            return None
        
        # Extrai as possíveis próximas palavras e suas respectivas frequências (pesos)
        next_words_counter = self.corpus_map[word]
        possible_words = list(next_words_counter.keys())
        weights = list(next_words_counter.values())

        # random.choices sorteia um item baseado nos pesos passados.
        # k=1 significa que queremos apenas 1 resultado. Retorna uma lista, então pegamos o índice [0]
        chosen_word = random.choices(possible_words, weights=weights, k=1)[0]
        return chosen_word

    def generate(self, start_word: str, length: int = 10) -> str:
        """Gera uma sequência de texto baseada no modelo treinado."""
        start_word = start_word.lower()
        result = [start_word]
        current_word = start_word

        for _ in range(1, length):
            next_word = self.get_next_word(current_word)
            
            if next_word is None:
                break # Para a geração se batermos em um "beco sem saída" do corpus
            
            result.append(next_word)
            current_word = next_word

        return ' '.join(result)

# === Exemplo de Uso ===
if __name__ == "__main__":
    # O mesmo exemplo do seu material para testar os pesos
    corpus = "O gato miou alto. O gato correu rápido. O cachorro latiu. O gato miou novamente. O gato miou muito."
    
    generator = BigramGenerator()
    generator.train(corpus)
    
    # Gera uma frase começando com "o" com limite de 5 palavras
    texto_gerado = generator.generate("o", 5)
    print(f"Texto gerado: {texto_gerado}")
