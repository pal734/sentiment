 
!pip install streamlit textblob nltk
import streamlit as st

st.title("Sentiment analysis ")


import streamlit as st
from textblob import TextBlob
import nltk


@st.cache_resource
def download_nltk_data():
    nltk.download('punkt')
    nltk.download('brown')
    nltk.download('wordnet')

download_nltk_data()

text = st.text_area("Enter text")
if st.button("Analyze"):
    blob = TextBlob(text)
    st.write(blob.sentiment)
