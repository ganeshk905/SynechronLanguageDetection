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


