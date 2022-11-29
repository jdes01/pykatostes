from collections import Counter

class Game():
    
    def __init__(self, words: list[str], seed: int):
        self.words: list[str] = words
        self.seed: int = seed
        self.played_words: list[str] = []
    
    def evaluate(self, word: str) -> str:
        
        if len(self.played_words) > 5:
            return 'a txuparla'
        
        correct_word: str = self.words[self.seed]
        letter_frequency = Counter(correct_word)
        
        returned_word: str = "-----"
        
        
        for position in range(5):
            letter = word[position]
            if correct_word[position] == letter:
                returned_word = self.__replace_letter(returned_word, letter, position)
                letter_frequency[letter] -= 1
        
        for position in range(5):
            if returned_word[position] != "-":
                continue
            
            letter = word[position]
            if letter_frequency.get(letter, 0) == 0:
                continue
            
            returned_word = self.__replace_letter(returned_word, "+", position)
            letter_frequency[letter] -= 1
            
        self.played_words.append(returned_word)
        
        return returned_word


    def __replace_letter(self, word: str, letter: str, position: int) -> str:
        return word[:position] + letter + word[position + 1:]