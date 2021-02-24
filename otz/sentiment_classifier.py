import joblib
import re

class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("./class.pkl")
        self.vectorizer = joblib.load("./vect.pkl")
        self.classes_dict = {0: "negative", 1: "positive", -1: "prediction error"}


    @staticmethod
        
    def get_probability_words(prediction_message):
        if float(prediction_message)<=-1:
            return 'мне не понятен ('+ str(prediction_message)+')'
        elif float(prediction_message)<0.5:
            return 'негативный ('+str(prediction_message)+')'
        else:
            return 'позитивный ('+str(prediction_message)+')'

    def predict_text(self, text):
        try:
            vectorized = self.vectorizer.transform([text])
            return self.model.predict(vectorized)[0], self.model.predict(vectorized)[0]
        except Exception as e:
            print("prediction error:", e)
            return -1, 0.8

    def predict_list(self, list_of_texts):
        try:
            vectorized = self.vectorizer.transform(list_of_texts)
            return self.model.predict(vectorized),\
                   self.model.predict_proba(vectorized)
        except:
            print('prediction error')
            return None

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        class_prediction = prediction[0]
        prediction_probability = prediction[1]
        return str(prediction_probability)
