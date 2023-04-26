import joblib
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import streamlit as st
model = joblib.load('model.joblib')
text = st.text_input('Enter text you want to classify: ')
st.title('Spam or Ham')
# Define a function to process text data
def text_process(mess):
    STOPWORDS = stopwords.words('english')
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return ' '.join([word for word in nopunc.split() if word.lower() not in STOPWORDS])

# Define a function to make predictions on new data
def predict_spam_ham(text):
    text = text_process(text)
    text=text.lower()
    pred = model.predict([text])[0]
    if pred == 0:
        return 'ham'
    else:
        return 'spam'
if st.button('Predict'):
    st.success(predict_spam_ham(text))
