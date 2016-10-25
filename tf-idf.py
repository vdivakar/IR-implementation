document_0 = "China has a strong economy that is growing at a rapid pace. However politically it differs greatly from the US Economy."
document_1 = "At last, China seems serious about confronting an endemic problem: domestic violence and corruption."
document_2 = "Japan's prime minister, Shinzo Abe, is working towards healing the economic turmoil in his own country for his view on the future of his people."
document_3 = "Vladimir Putin is working hard to fix the economy in Russia as the Ruble has tumbled."
document_4 = "What's the future of Abenomics? We asked Shinzo Abe for his views"
document_5 = "Obama has eased sanctions on Cuba while accelerating those against the Russian Economy, even as the Ruble's value falls almost daily."
document_6 = "Vladimir Putin is riding a horse while hunting deer. Vladimir Putin always seems so serious about things - even riding horses. Is he crazy?"

doc_dic = [document_0, document_1, document_2, document_3, document_4, document_5, document_6]

import string
import math

def tokenize_doc(doc):
    list_with_stopwords= doc.translate(string.maketrans("", ""), string.punctuation).lower().split()
    list_without_stopwords = []
    with open("stop_words.txt", 'r') as s_w:
        text = s_w.read().split(",")
        for x in list_with_stopwords:
	    	if x not in text:
	    		list_without_stopwords.append(x)

	return list_without_stopwords
	s_w.close()

def occur_times(term, doc):
	return doc.count(term)

def find_tf(term, doc):
	doc = tokenize_doc(doc)
	return (occur_times(term,doc) + 0.0) / (len(doc)+0.0)

def find_if_occur_in_document(term,doc):
	doc = tokenize_doc(doc)
	if term in doc:
		return 1
	else: 
		return 0

def find_idf(term, corpus):
	total_docs = len(corpus)
	occurence_in_docs = 0
	for d in corpus:
		occurence_in_docs+= find_if_occur_in_document(term, d)

	val = (total_docs+0.0) / (occurence_in_docs+ 0.0)
	return math.log(val)

# def find_tfidf_score(term, )

# print find_idf("obama", doc_dic)
# print find_tf("divakar", "hello my name is divakar. divakar studies in BITS Pilani. divakar is doing IR project")

# def create_corpus():
#     corpus = []
#     for d in doc_dic:
#         corpus += (tokenize_doc(d))
#     return corpus


# def remove_stopwords_from_corpus(raw_corpus):
#     with open("stop_words.txt", 'r') as s_w:
#         text = s_w.read().split(",")
#         corpus2 = []
#         for x in raw_corpus:
#             if x not in text:
#                 corpus2.append(x)
#         return corpus2


# raw_corpus = create_corpus()
# print raw_corpus
# corpus=remove_stopwords_from_corpus(raw_corpus)
# print corpus


