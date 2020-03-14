# inverted indexing
# thanks for nlpforhackers.io

import nltk 
from collections import defaultdict
from nltk.stem.snowball import EnglishStemmer
# nltk.download('punkt')

class IndexingDocument:
    def __init__(self):
        self.__index = 0
        self.__docs_dict = defaultdict(int)
        self.__token_dict = defaultdict(list)
        self.stemmer = EnglishStemmer() 
        self.tokenizer = nltk.word_tokenize 
        

    def lookup(self, word):
        if self.stemmer:
            word = self.stemmer.stem(word.lower())
        list_index = self.__token_dict[word]
        return [self.__docs_dict[index] for index in list_index]

    
    def indexing(self, doc):
        self.__docs_dict[self.__index] = doc
        print(self.__docs_dict)
        for token in [t.lower() for t in self.tokenizer(doc)]:
            if self.stemmer:
                token = self.stemmer.stem(token)
            if self.__index not in self.__token_dict[token]:
                self.__token_dict[token].append(self.__index)
        self.__index += 1



if __name__ == '__main__':
    index_obj = IndexingDocument()
    index_obj.indexing('Hello everyone, My name is Thang')
    index_obj.indexing('Good morning, nice to meet you.')
    index_obj.indexing('Hello Danny, how are you?')
    index_obj.indexing('Great, i am playing football')
    index_obj.indexing('I loved her')
    index_obj.indexing('I played with her yesterday.')

    print(index_obj.lookup('play'))
    print(index_obj.lookup('hello'))