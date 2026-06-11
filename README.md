# Simple RAG System (Without Pretrained Models)

> A lightweight Retrieval-Augmented Generation pipeline using classical Information Retrieval — no LLMs, no embeddings, no external APIs.

---

## Overview

This project implements a simple RAG system using TF-IDF and cosine similarity. Users upload `.txt` documents through a Streamlit web interface, ask questions, and receive answers extracted from the most relevant document chunks.

---

## Features

- Upload multiple `.txt` documents
- Automatic document chunking
- TF-IDF based indexing
- Cosine similarity retrieval
- Rule-based answer extraction
- Displays retrieved chunks with similarity scores
- Simple, interactive Streamlit UI
- No pretrained models required

---

## Project Architecture

```
User Uploads TXT Files
        │
        ▼
Document Parser
        │
        ▼
Text Chunking
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Document Index
        │
        ▼
User Question
        │
        ▼
TF-IDF Retrieval
        │
        ▼
Top-K Relevant Chunks
        │
        ▼
Answer Extraction
        │
        ▼
Display Answer in UI
```

---

## Folder Structure

```
rag/
│
├── app.py
│
├── modules/
│   ├── parser.py
│   ├── chunker.py
│   ├── retriever.py
│   └── answer_extractor.py
│
├── uploads/
│
├── requirements.txt
│
└── README.md
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11.9 | Core language |
| Streamlit | Web interface |
| Scikit-learn | TF-IDF vectorization & cosine similarity |
| NumPy | Numerical operations |

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## How It Works

### 1. Document Upload
Users upload one or more `.txt` files through the web interface.

### 2. Document Parsing
Uploaded files are read and converted into plain text.

### 3. Chunking
Documents are split into ~100-word chunks to improve retrieval granularity.

### 4. TF-IDF Indexing
Each chunk is transformed into a TF-IDF vector using Scikit-learn's `TfidfVectorizer`.

### 5. Query Processing
When a question is submitted:
- The query is converted into a TF-IDF vector
- Cosine similarity is computed against all document chunks
- The top-K matching chunks are retrieved

### 6. Answer Extraction
A keyword-overlap mechanism identifies the most relevant sentence from the retrieved chunks and returns it as the answer.

---

## Example

**Uploaded Document:**
```
John works at Google.
John joined Google in 2021.
His manager is Sarah.
```

**User Question:**
```
Who is John's manager?
```

**System Response:**
```
His manager is Sarah.
```

---

## Advantages

- Simple and easy to understand
- Lightweight with minimal dependencies
- No LLMs or pretrained embeddings needed
- Fast retrieval for small to medium document collections
- Demonstrates the complete RAG workflow end-to-end

---

## Limitations

- Keyword-based retrieval — no semantic understanding
- Synonyms and paraphrased questions may miss relevant results
- Limited answer generation capability
- Supports `.txt` files only
- No conversation history

---

## Future Improvements

- [ ] Support PDF and DOCX documents
- [ ] Implement BM25 retrieval
- [ ] Add persistent indexing
- [ ] Improve answer extraction
- [ ] Add chat history support
- [ ] Semantic retrieval using embeddings
- [ ] LLM integration for advanced answer generation

---

## Conclusion

This project demonstrates a complete RAG pipeline using classical IR techniques — TF-IDF retrieval and rule-based answer extraction — offering a lightweight, explainable alternative to modern LLM-based RAG systems.
