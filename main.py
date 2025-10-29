import streamlit as st
import pickle
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

try:
    #Load the KNN Model and Pivot Table
    model = pickle.load(open('artifacts/model_knn.pkl','rb'))
    book_pivot = pickle.load(open('artifacts/book_pivot.pkl','rb'))
    book_titles = pickle.load(open('artifacts/book_titles.pkl','rb')) # List of titles

    #Load the Image Lookup (Title -> URL)
    image_lookup_df = pd.read_csv('artifacts/image_lookup.csv')


    books_data = pickle.load(open('artifacts/books.pkl','rb'))

except FileNotFoundError:
    st.error("Error")
    st.stop()

def recommend_book(book_name):

    try:
        book_id = np.where(book_pivot.index == book_name)[0][0]
    except IndexError:
        return [f"Sorry, '{book_name}' was not found in our popular book list."]

    # Find similar books using the KNN model
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    recommendations = []
    for i in range(1, len(suggestion[0])):
        recommended_book = book_pivot.index[suggestion[0][i]]
        recommendations.append(recommended_book)

    return recommendations

# Streamlit App UI
st.title('Book Recommendation System')
st.markdown('### Finds similar books based on collective user ratings')


selected_book_name = st.selectbox('Select a book to get similar recommendations:', book_titles)

if st.button('Show Similar Books'):
    if selected_book_name:
        with st.spinner('Generating recommendations...'):
            recommendations = recommend_book(selected_book_name)

        st.subheader(f'If you liked "{selected_book_name}", you might like:')


        cols = st.columns(5)

        for i, book_title in enumerate(recommendations):



            img_url_series = image_lookup_df[image_lookup_df['title'] == book_title]['img_url']
            img_url = img_url_series.iloc[0] if not img_url_series.empty else "https://placehold.co/100x150/AAAAAA/FFFFFF?text=No+Image"

            author_series = books_data[books_data['Book-Title'] == book_title]['Book-Author']
            author_name = author_series.iloc[0] if not author_series.empty else "Unknown Author"

            with cols[i % 5]: # Display 5 books per row
                st.image(img_url, caption=f"By: {author_name}", width=100)
                st.caption(book_title)
    else:
        st.warning('Please select a book name.')