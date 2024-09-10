class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(j, '')
                words = text.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        dict_ = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                dict_[key] = value.index(word.lower()) + 1
        return dict_

    def count(self, word):
        dict_2 = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            dict_2[value] = words_count
        return dict_2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего