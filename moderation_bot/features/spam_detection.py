# spam_detection.py

# Import necessary libraries
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

class SpamDetection:
    def __init__(self):
        # Initialize the TF-IDF Vectorizer
        self.vectorizer = TfidfVectorizer()
        # Initialize the Random Forest Classifier
        self.classifier = RandomForestClassifier()

    def train_model(self, messages, labels):
        # Fit the TF-IDF Vectorizer on the messages
        X = self.vectorizer.fit_transform(messages)
        # Train the Random Forest Classifier
        self.classifier.fit(X, labels)

    def predict(self, message):
        # Transform the message using the TF-IDF Vectorizer
        X = self.vectorizer.transform([message])
        # Predict the label using the trained classifier
        prediction = self.classifier.predict(X)
        return prediction[0]

# Instantiate the SpamDetection class
spam_detector = SpamDetection()