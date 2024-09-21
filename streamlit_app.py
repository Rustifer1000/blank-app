import streamlit as st
from pymongo import MongoClient
import time

st.write("Connecting to MongoDB...")

try:
    # Start a progress bar
    progress = st.progress(0)

    # Simulate connection attempt and progress
    for i in range(10):
        progress.progress(i * 10)
        time.sleep(0.5)

    # MongoDB connection with timeout
    client = MongoClient(st.secrets["mongodb"]["uri"], serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    st.write("Connected to MongoDB!")

    # Access the database
    db = client['mediation_db']
    st.write("Accessing database...")

    collections = db.list_collection_names()
    st.write("Collections in the database:", collections)

except Exception as e:
    st.error(f"An error occurred: {e}")



