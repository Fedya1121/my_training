class WordsFinder:

    def __init__(self, *file_names ):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                words = file.read().split()
                all_words[name] = words
        return all_words

    def find(self, word):
        found_words = {}
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            for index, w in enumerate(words):
                index += 1
                if w.lower() == word_lower:
                    found_words[name] = index
                    break
        return found_words

    def count(self, word):
        words_counts = {}
        word_lower = word.lower()
        for name, words in self.get_all_words().items():
            words_counts[name] = sum(1 for w in words if w.lower() ==word_lower )
        return words_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

