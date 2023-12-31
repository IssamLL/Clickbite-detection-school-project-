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
text = st.text_input("Enter some text", value="Classify this")
if text:
    new_title = list(text)
    new_sequences = tokenizer.texts_to_sequences(new_title)
    new_padded_sequences = pad_sequences(new_sequences, maxlen=12, padding='post')
    output = model.predict(new_padded_sequences)
    if len(output) > 1:
        st.write(output)
        if model.predict(output)[0][0] > 0.5:
           st.write("This is a postive title")
        else:
            st.write("This is a negative tile")
