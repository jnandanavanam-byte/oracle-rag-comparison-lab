"""
Oracle RAG Comparison Lab
Configuration
"""

# =====================================================
# Documents
# =====================================================

DOCS_PATH = "../docs"

# =====================================================
# Large Language Model
# =====================================================

LLM_MODEL = "qwen3:14b"

# =====================================================
# Pipeline 1
# Recursive + MiniLM + Chroma
# =====================================================

PIPELINE1 = {
    "name": "Recursive + MiniLM + Chroma",
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
    "vectordb": "chroma"
}

# =====================================================
# Pipeline 2
# Semantic + BGE-M3 + FAISS
# =====================================================

PIPELINE2 = {
    "name": "Semantic + BGE-M3 + FAISS",
    "embedding_model": "BAAI/bge-m3",
    "vectordb": "faiss"
}