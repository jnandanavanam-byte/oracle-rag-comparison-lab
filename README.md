# Oracle RAG Comparison Lab

Enterprise RAG Evaluation Framework for Oracle ERP Documentation.

## Objectives

- Load Oracle Manuals (PDF, DOCX, XLSX)
- Compare Recursive and Section-Based Chunking
- Compare MiniLM and BGE-M3 Embeddings
- Compare ChromaDB and FAISS
- Generate Responses using Qwen3:14B

## Project Status
 
✅ Core Implementation Complete

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

## Example Evaluation Results

> Results shown below were generated using a specific Oracle ERP documentation dataset. Actual results will vary depending on document volume, structure, and content characteristics.

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

### Section-Based Chunking

| Metric | Value |
|---------|---------|
| Chunks Generated | 880 |
| Average Chunk Length | 2830 |
| Maximum Chunk Length | 5066 |
| Minimum Chunk Length | 904 |

### Observations

Recursive Chunking produced a larger number of smaller chunks, enabling more granular retrieval.

Section-Based Chunking produced fewer but significantly larger chunks, preserving more Oracle ERP business context and procedural information.

The minimum-length Recursive chunks corresponded to Roman numeral pages found in Oracle documentation:

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

### Optional GPU Acceleration

The project automatically detects available hardware.

| Environment | Supported |
|------------|------------|
| CPU Only | ✅ |
| NVIDIA CUDA GPU | ✅ |
| Development Laptop | ✅ |
| Enterprise Workstation | ✅ |

GPU acceleration is optional and automatically enabled when a CUDA-compatible NVIDIA GPU is available.

No GPU is required to run this project.

## Notebook Walkthrough

| Notebook | Purpose |
|-----------|-----------|
| 01_Document_Loading.ipynb | Load and validate Oracle ERP documents |
| 02_Recursive_Chunking.ipynb | Implement Recursive Character Chunking |
| 03_Semantic_Chunking.ipynb | Archived Semantic Chunking evaluation |
| 03_Section_Based_Chunking.ipynb | Implement Section-Based Chunking |
| 04_Chunking_Comparison.ipynb | Compare Recursive and Section-Based Chunking |
| 05_MiniLM_Embeddings.ipynb | Generate MiniLM embeddings |
| 06_BGEM3_Embeddings.ipynb | Generate BGE-M3 embeddings |
| 07_Chroma_Indexing.ipynb | Build ChromaDB vector store |
| 08_FAISS_Indexing.ipynb | Build FAISS vector store |
| 09_Retrieval_Comparison.ipynb | Compare retrieval quality |
| 10_Qwen_Inference.ipynb | Compare Qwen3:14B answers generated from both retrieval pipelines |

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

### Verify GPU Support (Optional)

```python
import torch

print(torch.cuda.is_available())

if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
```

Expected output on a CUDA-enabled system:

```text
True
NVIDIA RTX A5000 Laptop GPU
```

## Future Enhancements

- [ ] Streamlit User Interface
- [ ] Interactive Oracle ERP Assistant