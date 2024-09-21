import streamlit as st
from pymongo import MongoClient

# Access MongoDB URI from Streamlit secrets
mongodb_uri = st.secrets["mongodb"]["uri"]

# Create a MongoDB client using the URI directly
client = MongoClient(mongodb_uri)

# Access the database (replace 'your_database_name' with actual DB name)
db = client['your_database_name']

# Test: List collections in the database
st.write(db.list_collection_names())

