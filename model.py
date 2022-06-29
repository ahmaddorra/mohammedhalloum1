import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import pickle
import logging

class MultinomialNB:
    def __init__(self):
        logging.info("MultinomialNB class initialized")
        f = open(os.getcwd()+'/MultinomialNB.pickle', 'rb')
        self.model  = pickle.load(f)
        self.vectorizer = pickle.load(open(os.getcwd()+"/vector.pickel", "rb"))
        f.close()
        logging.info("Model is loaded!")

    def predict(self, text):
        logging.info(text)
        txtTransformed = self.vectorizer.transform([text])
        pred = self.model.predict(txtTransformed)
        print(pred)
        return self.news_result(pred)
        
    def news_result(self,y):
        result = ""
        if y == [0]:
            result = "Politics News"
        elif y == [1]:
            result = "World News"
        elif y == [2]:
            result = "Politics News"
        elif y == [3]:
            result = "Government News"
        elif y == [4]:
            result = "Left News"
        elif y == [5]:
            result = "US News"
        elif y == [6]:
            result = "Middle East News"
        return result
