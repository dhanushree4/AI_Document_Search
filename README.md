# 📄 DataTalk - AI-Powered Document Intelligence System
> **DataTalk** is an intelligent document analysis system that allows users to upload documents and interact with them using natural language queries. Powered by Retrieval-Augmented Generation (RAG), it provides accurate, context-aware answers with source tracking and confidence scoring.

🌐 **Live Demo:** [https://rag-project-aqua-sun.reflex.run/](https://rag-project-aqua-sun.reflex.run/)


---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🧠 How It Works - Deep Dive](#-how-it-works---deep-dive)
- [🏗️ System Architecture](#️-system-architecture)
- [🛠️ Technology Stack](#️-technology-stack)
- [📁 Project Structure](#-project-structure)


---

## ✨ Features

### 📤 Document Upload & Processing
- Support for multiple formats: **PDF**, **TXT**, **CSV**
- Automatic text extraction and preprocessing
- Intelligent chunking with optimal context retention (300 chars with 30 overlap)

### 🤖 Natural Language Queries
- Ask questions in plain English
- Get context-aware responses from your documents
- Real-time streaming responses

### 📊 Intelligent Retrieval
- **Semantic Search** using vector embeddings (384-dim)
- **Max Marginal Relevance (MMR)** for diverse results
- Confidence scores for each answer
- Source tracking and document attribution

### 💬 Conversation Memory
- Maintain chat history across sessions
- Context-aware follow-up questions
- Seamless conversation flow

### 🔒 Data Privacy
- All processing happens locally
- No data retention or storage
- Enterprise-grade security practices


---

## 🧠 How It Works - Deep Dive

### The Core Concept: Retrieval-Augmented Generation (RAG)

Traditional Large Language Models (LLMs) have a fundamental limitation - they can only answer questions based on their training data. If you ask about a specific document they've never seen, they'll either hallucinate or admit they don't know. **RAG solves this problem by combining two powerful techniques:**

1. **Retrieval:** Finding relevant information from your documents
2. **Generation:** Using that information to formulate accurate answers

### Document Processing Pipeline

When you upload a document, DataTalk processes it through several stages:

**1. Text Extraction**
The system extracts raw text from your uploaded file. For PDFs, it uses PyPDFLoader to extract text from each page. For text files, it reads the content directly. CSV files are parsed with CSVLoader to handle structured data appropriately.

**2. Text Cleaning & Normalization**
Extracted text undergoes cleaning to remove special characters, extra whitespace, and formatting artifacts. The text is then normalized to consistent case and encoding format to ensure uniform processing.

**3. Intelligent Chunking**
Documents cannot be processed as whole due to LLM context limitations. DataTalk splits documents into overlapping chunks of 300 characters with a 30-character overlap. This overlap ensures that no critical information is lost at chunk boundaries. If a sentence or concept spans across a chunk boundary, the overlap captures it in both chunks, maintaining semantic continuity.

**4. Embedding Generation**
Each text chunk is converted into a mathematical representation called a vector using the all-MiniLM-L6-v2 model. This model creates 384-dimensional vectors where semantically similar texts have vectors that are close together (high cosine similarity), while unrelated texts have vectors that are far apart (low cosine similarity).

**5. Vector Storage**
All generated vectors are stored in ChromaDB, a vector database that enables fast similarity search. Each vector is stored with metadata including source document name, page number, and position within the document.

### Query Processing Pipeline

When you ask a question, DataTalk follows this process:

**1. Query Embedding**
Your question is converted into a 384-dimensional query vector using the same embedding model used for document chunks.

**2. Semantic Similarity Search**
The system calculates cosine similarity between your query vector and all stored document vectors. Cosine similarity measures the angle between vectors - values close to 1 indicate high similarity, values near 0 indicate low similarity.

**3. MMR Re-ranking**
Instead of simply taking the top 5 most similar chunks, the system applies Max Marginal Relevance (MMR). MMR balances two important factors: relevance to your query and diversity among results. This prevents the system from returning multiple chunks that all say the same thing from the same part of the document. Instead, it ensures you get a diverse set of relevant information from different sections.

**4. Context Construction**
The retrieved chunks are formatted into a structured context with their source metadata. A system prompt is added instructing the AI to answer only based on the provided context. If the answer isn't in the context, the system is instructed to say "I don't have that information" rather than hallucinating.

**5. LLM Inference**
The constructed prompt is sent to Groq's LLaMA 3.1 model (70 billion parameters) for inference. Groq provides ultra-fast inference speeds, enabling near real-time responses. The model generates a response based solely on the provided context.

**6. Response Enhancement**
The generated response is enhanced with:
- **Confidence Score:** Calculated from the similarity scores of retrieved chunks
- **Source Attribution:** Document names and page numbers for each piece of information used
- **Streaming:** Real-time display of generated text as it's produced


---

## 🏗️ System Architecture

### Component Breakdown

**Frontend Layer (Reflex)**
The frontend is built with Reflex, a Python web framework that provides reactive components. It consists of several pages:
- **Upload Page:** Handles file uploads with drag-and-drop functionality
- **Chat Interface:** Manages real-time conversation with streaming responses
- **History Page:** Displays past conversations and allows continuation
- **About Page:** Provides system documentation and information

The frontend maintains application state including uploaded documents, chat history, and user session data. Reflex's reactive architecture ensures that UI updates happen automatically when state changes.

**Backend API Layer**
The backend handles all document processing and RAG operations:
- **Document Processing:** Manages file uploads, text extraction, and preprocessing
- **RAG Pipeline:** Orchestrates the embedding generation, retrieval, and response generation
- **Vector Operations:** Interfaces with ChromaDB for storage and similarity search
- **LLM Integration:** Communicates with Groq API for response generation

**Data Storage Layer**
- **ChromaDB:** Persistent vector storage with efficient similarity search indexing
- **File System:** Temporary storage for uploaded documents during processing
- **Session Storage:** Maintains user chat history and application state

**External Services**
- **Groq API:** Provides ultra-fast LLaMA 3.1 inference with low latency
- **LangChain:** Framework for RAG pipeline orchestration and prompt management
- **Sentence Transformers:** Local embedding model running on your machine


---

### Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Frontend** | Reflex | Web application framework with reactive components |
| **Backend** | Python 3.12 | Core application logic and API endpoints |
| **LLM** | Groq (LLaMA 3.1) | Ultra-fast language model inference (70B parameters) |
| **Embeddings** | Sentence Transformers (all-MiniLM-L6-v2) | Local 384-dim vector generation |
| **Vector DB** | ChromaDB | Persistent vector storage with similarity search |
| **Framework** | LangChain | RAG pipeline orchestration and tools |
| **Document Processing** | PyPDFLoader, TextLoader | Text extraction from various formats |
| **State Management** | Reflex State | Frontend state and session management |


---

## Project Structure
```
RAG_PROJECT/
├── RAG_PROJECT.py           # Main application file
├── rxconfig.py              # Reflex configuration
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys)
│
├── backend/                 # Backend logic
│   └── rag.py              # RAG implementation
│
├── components/              # Reusable UI components
│   ├── footer.py           # Footer component
│   ├── hero.py             # Hero section
│   └── navbar.py           # Navigation bar
│
├── pages/                   # Application pages
│   ├── upload.py           # Document upload page
│   ├── chat.py             # Chat interface
│   ├── history.py          # Chat history
│   └── about.py            # About page
│
├── states/                  # State management
│   └── app_state.py        # Application state
│
├── assets/                  # Static assets
│   └── images/             # Images and icons
│
└── documents/               # Uploaded documents (local only)
```

The implementation of embeddings, vector search, and LLM-based response generation showcases a scalable and efficient approach to document-based question answering, bridging the gap between traditional search and intelligent AI systems.
