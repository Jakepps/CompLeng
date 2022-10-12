from nltk import sent_tokenize  
from nltk import word_tokenize  
from nltk.corpus import stopwords

def graph_analysis(dataset):
    sent = sent_tokenize(dataset)
    result_list=[]
    stop_words=set(stopwords.words('russian'))
    for index in sent:
        temp=index
        words=word_tokenize(temp)
        without_stop_word=[word for word in words if not word in stop_words]
        for index2 in without_stop_word:
            result_list.append(index2)
    dict_={}
    for index in result_list:
        if index in dict_.keys():
            dict_[index]+=1
        else:
            dict_[index]=1
    print()
    for key in dict_.items():
        print(key,end=' ')
    print()

file = open("C:/Users/Артём/source/repos/Jakepps/CompLeng/dataset.txt", "r", encoding="utf8") 
input_file2 = file.read()
input_file= ' '
for i in range(len(input_file2)):#удаления из текста лишних символов
    if input_file2[i] != '\xa0' and input_file2[i] != '\ufeff':
        input_file += input_file2[i]

print(graph_analysis(input_file))
text = file.readlines()  
SW= set(stopwords.words('russian'))
d = 1 # № предложения 
for elements in text:
    sentences = sent_tokenize(elements)
    for i in range(len(sentences)):
        print("Предложение №" + " " + str(d) + ": " + str(sentences[i]))
        sentword = sentences[i]
        d += 1
        words = word_tokenize(sentword)
        withoutSW = [word for word in words if not word in SW]
        print("Слова из этого предложения: ", sep="")
        print(withoutSW, sep=" ")
        print("\n") 
