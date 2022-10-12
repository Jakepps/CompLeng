#2
path = "C:/Users/Артём/source/repos/Jakepps/CompLeng/dataset.txt"  

from nltk import sent_tokenize 
from nltk import word_tokenize 

from pymorphy2 import MorphAnalyzer  

file = open(path, "r", encoding="utf8") 

text = file.readlines() 
words = []  
file.close()
# все слова в датасете добавляем в переменную words
for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        sent = sentences[i]
        words += word_tokenize(sent)

morph = MorphAnalyzer()

# для первых ста слов в датасете выводим их морфологический разбор

for i in range(100):
    print(str(morph.parse(words[i])) + "\n")