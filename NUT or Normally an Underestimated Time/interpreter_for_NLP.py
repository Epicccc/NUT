import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords


sample_text = open("test.nut", "r").read()

stop_words = set(stopwords.words("english"))

custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = list(nltk.word_tokenize(i))
			filtered_sentance = [w for w in words if not w in stopwords]
			tagged = nltk.pos_tag(filtered_sentance)
			print tagged
	except Exception as e:
		print str(e)

process_content()