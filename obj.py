import streamlit as st
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
import torch

genai.configure(api_key="AIzaSyC-45MSDZKaXsINcdEf3gwx8ozNnypdeLw")

model_name = "cl-nagoya/ruri-v3-310m"
device = "cuda" if torch.cuda.is_available() else "cpu"
faiss_db_path = "./faiss-jap-db"

@st.cache_resource
def load_embedder(model_name, device):
    embedder = SentenceTransformer(model_name,
                                    device=device,
                                    trust_remote_code=True)
    return embedder

embedder = load_embedder(model_name, device)

@st.cache_resource
def load_vector_store(faiss_path):
    def embed_func(chunks):
        return embedder.encode(chunks, 
                               show_progress_bar=False)

    vector_store = FAISS.load_local(faiss_path,
                                     embeddings=embed_func,
                                     allow_dangerous_deserialization=True)
    return vector_store

vector_store = load_vector_store(faiss_db_path)