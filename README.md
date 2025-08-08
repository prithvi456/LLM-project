# 📑 Insurance Decision Assistant

An **AI-powered, LLM-based system** that processes insurance policy documents, understands user queries, and delivers **instant claim decisions** with clear justifications.  
The system combines **document parsing**, **semantic search**, and **Large Language Model reasoning** to automate insurance claim evaluations.

---

## 🚀 Features

- **📂 Document Parsing** – Upload PDF/DOCX insurance policies, extract text, and split into searchable chunks.
- **🔍 Semantic Search** – Retrieve the most relevant clauses using FAISS + SentenceTransformers embeddings.
- **🧠 Query Parsing** – Extracts structured data (age, gender, procedure, location, policy duration) from natural language queries.
- **✅ Decision Engine** – Uses LLM to return Approval/Rejection, confidence score, claim amount, and justification.
- **💡 Clause Highlighting** – Shows exactly which clauses influenced the decision.
- **📄 PDF Report Generation** – Download decision report with query, parsed details, relevant clauses, and final verdict.
- **📧 Email Integration** – Send approved claims directly to the insurance company.
- **🔐 Secure API Key Handling** – Store API keys in `.env` file using `python-dotenv`.

---

## 🛠️ Tech Stack

- **Language:** Python  
- **UI Framework:** Streamlit  
- **Document Processing:** PyMuPDF, python-docx  
- **Search Engine:** FAISS, SentenceTransformers (`all-MiniLM-L6-v2`)  
- **LLM Provider:** Groq API (LLaMA 3)  
- **PDF Generation:** ReportLab  
- **Email Sending:** smtplib / yagmail  
- **Environment Variables:** python-dotenv  

---



