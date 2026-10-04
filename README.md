# Oracle RAG Comparison Lab

Enterprise RAG Evaluation Framework for Oracle ERP Documentation.

## Objectives

- Load Oracle Manuals (PDF, DOCX, XLSX)
- Compare Recursive and Semantic Chunking
- Compare MiniLM and BGE-M3 Embeddings
- Compare ChromaDB and FAISS
- Generate Responses using Qwen3:14B

## Project Status

🚧 Project Setup In Progress

## Planned Pipelines

| Component | Pipeline 1 | Pipeline 2 |
|-----------|------------|------------|
| Chunking | Recursive | Semantic |
| Embeddings | MiniLM | BGE-M3 |
| Vector DB | ChromaDB | FAISS |
| LLM | Qwen3:14B | Qwen3:14B |

## Repository Structure

```text
oracle-rag-comparison-lab
│
├── docs
├── notebooks
├── screenshots
├── diagrams
├── src
├── vectorstores
├── README.md
├── requirements.txt
└── .gitignore
```

## Technology Stack

### Core Framework

- LangChain
- LangChain Core
- LangChain Text Splitters

### Large Language Model

- Ollama
- Qwen3:14B

### Embedding Models

- all-MiniLM-L6-v2
- BAAI/bge-m3

### Vector Databases

- ChromaDB
- FAISS

### Document Types Supported

- PDF
- DOCX
- XLSX

### Development Environment

- Python
- Jupyter Notebooks
- VS Code

### UI

- Streamlit

### Visualization

- Matplotlib
- Seaborn

## Future Enhancements

- [ ] Parent Child Chunking
- [ ] Hybrid Search
- [ ] BM25 Retrieval
- [ ] Cross Encoder Reranking
- [ ] Oracle ERP Knowledge Assistant

## Installation

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```powershell
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```