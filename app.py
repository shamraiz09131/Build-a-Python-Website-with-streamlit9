# app.py

import streamlit as st

# Sample data with additional details
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "description": "A novel set in the Jazz Age that tells the story of Jay Gatsby's unrequited love for Daisy Buchanan."},
    {"title": "1984", "author": "George Orwell", "year": 1949, "description": "A dystopian novel set in a totalitarian society ruled by Big Brother."},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "description": "A novel about racial injustice in the Deep South, seen through the eyes of young Scout Finch."},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "description": "A romantic novel that critiques the British landed gentry at the end of the 18th century."},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "description": "A story about teenage angst and alienation as experienced by Holden Caulfield."},
    {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851, "description": "The narrative of Captain Ahab's obsessive quest to kill the white whale, Moby Dick."},
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869, "description": "A historical novel that chronicles the French invasion of Russia and its impact on Tsarist society."},
    {"title": "The Odyssey", "author": "Homer", "year": -800, "description": "An epic poem that follows the Greek hero Odysseus on his journey home after the fall of Troy."},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866, "description": "A psychological novel exploring the moral dilemmas of a young man who commits a murder."},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": 1880, "description": "A philosophical novel that delves into the ethical debates of God, free will, and morality."}
]

# Title of the app
st.title("Book Library")

# Search bar
search_term = st.text_input("Search for a book by title:")

# Filter books based on search term
if search_term:
    filtered_books = [book for book in books if search_term.lower() in book["title"].lower()]
else:
    filtered_books = books

# Display books
st.subheader("Books List")
for book in filtered_books:
    st.write(f"**Title:** {book['title']}")
    st.write(f"**Author:** {book['author']}")
    st.write(f"**Year:** {book['year']}")
    st.write(f"**Description:** {book['description']}")
    st.write("---")

# Run the app with: streamlit run app.py