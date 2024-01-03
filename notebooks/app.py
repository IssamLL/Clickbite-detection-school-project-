import streamlit as st
from tensorflow.keras.models import load_model
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the tokenizer tokenizer.pickle
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the model

model = load_model('model.h5')
# On subsequent interactions, the cached model will be used

# When the input changes, the cached model will be used
st.header('Clickbait Binary Classifier Develepped')
st.write(' by ECH-CHAOUI Issam and EL BHIRI Zakariae')
st.write('This app is based on a LSTM model')
st.write('The model is trained on the Clickbait dataset')
st.write('The model is trained on the Clickbait dataset')

text = st.text_input("Enter some text")


# * optional kwarg unsafe_allow_html = True
if text:
    title = [text]

    sequences = tokenizer.texts_to_sequences(title)
    padded_sequences = pad_sequences(sequences, maxlen=12, padding='post')
    output = model.predict(padded_sequences)

    
    st.write(output)
    if model.predict(output) > 0.5:
        st.write("This is not a clickbait title")
    else:
        st.write("This is a clickbait tile")
