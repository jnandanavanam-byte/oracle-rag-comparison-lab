# Oracle RAG Comparison Lab

Enterprise RAG Evaluation Framework for Oracle ERP Documentation.

## Objectives

- Load Oracle Manuals (PDF, DOCX, XLSX)
- Compare Recursive and Section-Based Chunking
- Compare MiniLM and BGE-M3 Embeddings
- Compare ChromaDB and FAISS
- Generate Responses using Qwen3:14B

## Project Status

🚧 Development In Progress

## Planned Pipelines

| Component | Pipeline 1 | Pipeline 2 |
|-----------|------------|------------|
| Chunking | Recursive Character Chunking | Section-Based Chunking |
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

## Design Decisions

### Evaluation of Semantic Chunking

During the design phase, a Semantic Chunking implementation was evaluated using:

- Oracle Purchasing User Guide
- Oracle iSupplier Portal Guide

### Test Dataset

| Metric | Value |
|----------|----------|
| Source Files | 2 |
| Source Pages | 1502 |

### Observations

Semantic Chunking produced context-aware chunk boundaries but required significantly higher processing resources compared to Recursive Chunking.

During testing on a large Oracle ERP documentation corpus, execution time exceeded 100 minutes and became impractical for iterative development and experimentation.

### Decision

To maintain:

- Reproducibility
- Faster development cycles
- CPU-only compatibility
- Simpler deployment for GitHub users
- Faster experimentation and debugging

the project architecture was revised.

### Final Pipeline Design

#### Pipeline 1

- Recursive Character Chunking
- Chunk Size: 1000
- Chunk Overlap: 200
- MiniLM Embeddings
- ChromaDB
- Qwen3:14B

#### Pipeline 2

- Section-Based Chunking
- BGE-M3 Embeddings
- FAISS
- Qwen3:14B

### Rationale

Oracle ERP documentation is highly structured and organized into:

- Chapters
- Sections
- Procedures
- Navigation Flows

Section-Based Chunking preserves business context while remaining significantly more efficient for large document collections.

This approach provides a meaningful comparison between two Retrieval-Augmented Generation (RAG) strategies while remaining practical for a wide range of hardware configurations.

## Initial Findings

### Document Loading

| Metric | Value |
|---------|---------|
| Source Files | 2 |
| Pages Loaded | 1502 |

### Recursive Chunking

| Metric | Value |
|---------|---------|
| Chunks Generated | 3519 |
| Average Chunk Length | 802 |
| Maximum Chunk Length | 1000 |
| Minimum Chunk Length | 1 |

### Observations

The minimum-length chunks corresponded to Roman numeral pages found in Oracle documentation:

- x
- xii
- xvi

These were determined to be valid document content and not extraction errors.

## Performance Considerations

### Recursive Chunking

- Fast execution
- Low CPU and memory usage
- Suitable for development and testing
- Ideal for rapid iteration

### Section-Based Chunking

- Preserves Oracle documentation structure
- Retains business context
- More efficient than Semantic Chunking
- Suitable for large Oracle ERP manuals

### Recommended Dataset Sizes

| Corpus Size | Recommendation |
|-------------|---------------|
| Less than 100 Pages | ✅ Ideal for learning |
| 100 - 500 Pages | ✅ Recommended |
| 500 - 1000 Pages | ⚠️ Longer processing times |
| More than 1000 Pages | ⚠️ Recommended for final benchmarking |

### Development Mode

For experimentation and validation:

```python
sample_documents = documents[:100]
```

For full evaluation:

```python
working_documents = documents
```

### Hardware Independence

The project is designed to run on CPU-only environments.

GPU acceleration is optional.

Supported environments:

| Environment | Supported |
|------------|------------|
| CPU Only | ✅ |
| NVIDIA CUDA GPU | ✅ |
| Enterprise Workstation | ✅ |
| Development Laptop | ✅ |

### Optional GPU Acceleration

The project automatically detects available hardware.

| Environment | Supported |
|------------|------------|
| CPU Only | ✅ |
| NVIDIA CUDA GPU | ✅ |
| Development Laptop | ✅ |
| Enterprise Workstation | ✅ |

GPU acceleration is optional and is automatically enabled when a CUDA-compatible NVIDIA GPU is available.

No GPU is required to run this project.

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

## Future Enhancements

- [ ] Parent Child Chunking
- [ ] Hybrid Search
- [ ] BM25 Retrieval
- [ ] Cross Encoder Reranking
- [ ] GPU Acceleration Benchmarking
- [ ] Vision RAG
- [ ] Oracle ERP Knowledge Assistant
- [ ] Streamlit User Interface
- [ ] Oracle Workflow Visualization
- [ ] Retrieval Evaluation Dashboard