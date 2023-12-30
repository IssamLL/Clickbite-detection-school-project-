from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# plot the most used words with seaborn

def plot_most_used_words(df):
    # split title into words
    words = df['title'].str.split(expand=True).unstack().value_counts()

    # remove stopwords
    words = words.drop(stopwords, errors='ignore')

    # remove words with less than 3 characters
    words = words[words.index.str.len() >= 3]

    # plot
    plt.figure(figsize=(10, 5))
    sns.barplot(x=words.values[:20], y=words.index[:20], palette='rocket')
    plt.title('Most used words in titles')
    plt.xlabel('Count')
    plt.ylabel('Words')
    plt.show()

# function that take a df and plot word cloud
def plot_wordcloud(df, max_words = 200, max_font_size = 40):

    plt.figure(figsize=(20, 20))
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        scale=3,
        random_state=1).generate(str(df['title']))
    plt.imshow(wordcloud)
    plt.axis('off')

# most frequent ngrams
import seaborn as sns
def plot_most_frequent_ngrams(df, column_name= 'title', n=2, num_ngrams=10):
    
    # Extract text data from the specified column
    text_data = df[column_name].astype(str).values

    # Use CountVectorizer to convert text data into a bag-of-words representation
    vectorizer = CountVectorizer(ngram_range=(n, n), stop_words='english')
    X = vectorizer.fit_transform(text_data)

    # Sum the counts of each n-gram
    ngram_counts = X.sum(axis=0)

    # Get feature names (n-grams)
    feature_names = vectorizer.get_feature_names_out()

    # Create a DataFrame to store the n-gram counts
    ngram_df = pd.DataFrame(ngram_counts, columns=feature_names)

    # Transpose the DataFrame for easier plotting
    ngram_df = ngram_df.T

    # Get the top n-grams
    top_ngrams = ngram_df.sum(axis=1).nlargest(num_ngrams)

    # Plot the most frequent n-grams
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_ngrams.values, y=top_ngrams.index, palette="viridis")
    plt.title(f"Top {num_ngrams} {n}-grams")
    plt.xlabel("Frequency")
    plt.ylabel(f"{n}-gram")
    plt.show()