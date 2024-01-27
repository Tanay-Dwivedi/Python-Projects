# End to End Chatbot

A chatbot is a computer program that understands the intent of your query to answer with a solution.

To create an end-to-end chatbot using Python, we can follow the steps mentioned below:

- Define Intents
- Create training data
- Train the chatbot
- Build the chatbot
- Test the chatbot
- Deploy the chatbot

-----

## Installation

```
pip install streamlit scikit-learn nltk
```
Firstly import the `streamlit scikit-learn nltk` libraries through the terminal that will help in the program.

-----

## How to run:

To run this chatbot, use the command mentioned below in your terminal:

> streamlit run filename.py

-----

## Code Break:

**Imports:**
```python
import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
```
The code imports necessary libraries, including Streamlit for creating the web app, NLTK for natural language processing, and scikit-learn for machine learning components.

**Setting Up NLTK:**
```python
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download("punkt")
```
This part sets up NLTK by handling SSL context and configuring the data path for NLTK. It also downloads the "punkt" dataset, which is used for tokenization.

**Intent Definitions:**
```python
intents = [ ... ]  # List of dictionaries defining different conversation intents
```
The `intents` list contains dictionaries, each representing a conversation intent. Each dictionary includes a tag, patterns (user input), and responses (bot responses) associated with that intent.

**Machine Learning Setup:**
```python
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)
```
The code initializes a TF-IDF vectorizer and a logistic regression classifier.

**Data Preprocessing for Training:**
```python
tags = []
patterns = []
for intent in intents:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)

x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)
```
It prepares the training data by extracting tags and patterns from the intents. It then fits the vectorizer on the patterns and trains the classifier.

**Chatbot Function:**
```python
def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent["tag"] == tag:
            response = random.choice(intent["responses"])
            return response
```
The `chatbot` function takes user input, predicts the intent using the trained classifier, and returns a random response associated with that intent.

**Streamlit Web App:**
```python
def main():
    global counter
    st.title("Chatbot")
    st.write("Welcome to the chatbot. Please type a message and press Enter to start the conversation.")

    counter += 1
    user_input = st.text_input("You:", key=f"user_input_{counter}")

    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")

        if response.lower() in ["goodbye", "bye"]:
            st.write("Thank you for chatting with me. Have a great day!")
            st.stop()

if __name__ == "__main__":
    main()
```
The `main` function creates a simple Streamlit web app. It takes user input, calls the chatbot function to get a response, and displays the conversation in a text area. The conversation ends when the user says "goodbye" or "bye."

-----