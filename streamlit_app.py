import streamlit as st
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Access credentials from Streamlit secrets
username = st.secrets["mongodb"]["username"]
password = st.secrets["mongodb"]["password"]
cluster_url = st.secrets["mongodb"]["cluster_url"]
dbname = st.secrets["mongodb"]["dbname"]

# Construct the connection string
connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/{dbname}?retryWrites=true&w=majority"

# Try connecting to MongoDB Atlas
try:
    client = MongoClient(connection_string)
    db = client[dbname]
    # Ping the database (list collections as a basic test)
    collections = db.list_collection_names()
    st.success("Successfully connected to MongoDB Atlas!")
    st.write("Collections in the database:", collections)
except ConnectionFailure as e:
    st.error(f"Could not connect to MongoDB Atlas: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")
