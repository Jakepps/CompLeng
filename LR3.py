#3
from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    Doc
)

path = "C:/Users/Артём/source/repos/Jakepps/CompLeng/dataset.txt"
from nltk import sent_tokenize

file = open(path, "r", encoding="utf8")
text = file.readlines()
words = []
file.close()

segmenter = Segmenter()
emb = NewsEmbedding() #для кодировки слов
morph_tagger = NewsMorphTagger(emb) #для морф разбора слов
syntax_parser = NewsSyntaxParser(emb) #для синтаксического разбора слов

for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        sent = sentences[i]
        doc = Doc(sent)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        doc.parse_syntax(syntax_parser)
        print(doc.tokens[:5])
        doc.sents[0].syntax.print()