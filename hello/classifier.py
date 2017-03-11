import pickle
import os

def ClassifyReviews(text):
	index_to_emotion ={0: 'sadness', 1: 'neutral', 2: 'boredom', 3: 'anger', 4: 'surprise', 5: 'happiness', 6: 'relief'}
	text_classifier = pickle.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'savedclassifier.xploit'), "r+"))
	#text = ['Received defective product ','The Phone is outstanding','I bought iphone6 from amazon and its only 3 months ','Product is very good']		
	predicted_emotion_labels = text_classifier.predict(text)
	predicted_emotion = [index_to_emotion[i] for i in predicted_emotion_labels]
	return predicted_emotion