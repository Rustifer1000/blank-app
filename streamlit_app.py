import streamlit as st
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import time

st.write("Connecting to MongoDB...")

try:
    # Establish MongoDB connection
    client = MongoClient(st.secrets["mongodb"]["uri"])

    # Optional: Use ping command to check connection
    client.admin.command('ping')
    st.write("Connected to MongoDB!")

    # Access the database
    db = client['your_database_name']
    st.write("Accessing database...")

    # Example operation: List collections
    collections = db.list_collection_names()
    st.write("Collections in the database:", collections)

except ConnectionFailure as e:
    st.error(f"MongoDB connection failed: {e}")
except OperationFailure as e:
    st.error(f"Operation failed: {e}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")


