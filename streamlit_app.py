import time
import streamlit as st
from pymongo import MongoClient

# Create a progress bar
progress_bar = st.progress(0)

# Step 1: Connect to MongoDB
st.write("Connecting to MongoDB...")
client = MongoClient(st.secrets["mongodb"]["uri"])
progress_bar.progress(30)

# Step 2: Access the database
st.write("Accessing database...")
db = client["mediation_db"]
progress_bar.progress(60)

# Step 3: Query the collections
st.write("Querying the 'conversations' collection...")
collection = db["conversations"]
documents = list(collection.find())
progress_bar.progress(90)

# Display the documents
if documents:
    st.write(f"Documents: {documents}")
else:
    st.write("No documents found.")
progress_bar.progress(100)

st.write("Operation completed!")




