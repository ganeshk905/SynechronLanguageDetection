#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import unicode_literals
import spacy
import glob
import os, re, io
import time

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


data_dir = 'LangDetectorData'
lang_doc = {}

lang_dir = os.listdir(data_dir)

for dir in lang_dir:
	files = os.listdir(data_dir+'/'+dir)
	documents = []
	for file in files:
		with io.open(data_dir+'/'+dir+'/'+file, errors='ignore',encoding='utf-8') as fid:
			txt = u""
			txt += fid.read()
			txt = re.sub('\s', ' ', txt)
			documents.append(txt.lower())
	lang_doc[dir] = documents

################################################################################################



lang_token_corpus = {}

ch_removal = ",;.-#?_:[]{}()!*\"0123456789@<>=+|\\/&"

for key in lang_doc:
	tokenised_documents = []
	for doc in lang_doc[key]:
		tokens = doc.split(' ')
		tokenised_documents.append(tokens)
	lang_token_corpus[key] = tokenised_documents


lang_vocab = {}

for key in lang_token_corpus:
	flat_list = []
	for doc in lang_token_corpus[key]:
		for token in doc:
			for ch in token:
				if ch in ch_removal:
					token = token.replace(ch, '')
			token = token.strip('\'')
			if len(token)>1:
				flat_list.append(token.lower())
	vocab = set(flat_list)
	lang_vocab[key] = sorted(vocab)


################################################################################################

print "Please enter the Required String"
str = u""
str += raw_input()

document = u""


for token in str:
	if token in ch_removal:
		document +=' '
	else:
		document +=token.lower()
words = [token for token in document.split(' ') if len(token)>1]

doc_vocab = sorted(set(words))

print doc_vocab

confidence = {}
match_values = {}

for key in lang_vocab:
	match_values[key] = len(set(doc_vocab)&set(lang_vocab[key]))

sum =0
for key in match_values:
	sum +=match_values[key]

for key in match_values:
	confidence[key] = match_values[key]/float(sum)

max = 0
confidence["Other"] = 0
lang_class = "Other"
for key in confidence:
	if confidence[key]>max:
		lang_class=key
		max= confidence[key]


#print "String:", str
print "Class:", lang_class
print "Confidence:", confidence[lang_class]
