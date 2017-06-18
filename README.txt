The submission folder contains following files and folders.

1. classification.py:
This script contains implementation of bag of words model. Did preprocessing without using any python package.
I have also removed numeric and symbols while creating vocab. I have created vocabulary for each of the type 
of language. Given a document/string as an input, computed the occurance of words in document/string in each of 
the language. Using this score, calculated the confidence value for each of the language. Result shown will be 
having highest confidence value among all the languages. 

2. LangDetectorData:
This folder contains language folder which contains data files in the respective language. This folder needs to
in same folder as classification.py script.


Due to time shortage and assigment contraints i.e. not to use existing libraries, have some ideas which can be implemented further in future.
1. Can compute tf-idf of the vocabulary created of each language, which can be used for computing stop-words for that particular language. These stop words can be matched with the input string/document. Maximum number of match will give the resulting language class. Intution is stop words can be useful for classification related to that particular language. 
2. Can also create list of characters used in each type of langauge. This can be matched with set of characters which is in input string/documents. The language for which there is maximum match for set of characters will be answer.
3. Below is given size of vocabulary(unique words after preproceesing) for each of the language.
Danishi vocab : 43656
German vocab : 39328
English vocab : 27081
French vocab : 66524
Portugues vocab : 34586
Spanish vocab : 42177
Italian vocab : 42288

Here the size of vocab for each of the class is less. Need to collect more example to increase vocab size. Then it can be used to train neural nets by feeding vectors of these words as input and classifying them into classes. This can be implemented using tensorflow. We can convert words to vectors form using word2vec algorithm implemented in gensim.
