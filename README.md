# 🚀 AI Resume Analyzer

An advanced AI-powered Resume Analyzer built using the MERN Stack, Python AI/ML services, NLP, and Ollama LLM integration.

The platform analyzes resumes, predicts ATS scores, extracts skills, recommends job roles, provides AI-generated feedback, and offers intelligent career suggestions.

---

# ✨ Features

## 🔐 Authentication System

* JWT-based Login & Registration
* Secure Password Hashing using bcryptjs
* Protected Routes
* Production-style Authentication Flow

## 📄 Resume Analysis

* PDF Resume Upload
* Resume Text Extraction
* ATS Score Prediction
* NLP-based Skill Extraction
* Job Role Prediction
* Semantic Job Matching
* Resume Improvement Suggestions

## 🤖 AI Features

* Ollama LLM Integration
* AI Resume Feedback
* Career Suggestions
* Intelligent Chatbot Assistant
* Resume Optimization Suggestions

## 📊 Machine Learning Features

* Random Forest ATS Prediction Model
* Logistic Regression Role Prediction
* Sentence Transformers Semantic Matching
* TF-IDF Vectorization
* Dataset-driven ML Pipeline

## 🎨 Frontend Features

* Responsive Modern UI
* Floating AI Chatbot
* Dashboard Analytics
* Resume Upload Interface
* Multi-page Navigation
* Dark Professional Theme

---

# 🛠️ Tech Stack

## Frontend

* React.js
* Vite
* Tailwind CSS
* React Router DOM
* Axios
* Framer Motion

## Backend

* Node.js
* Express.js
* MongoDB
* Mongoose
* JWT Authentication
* Multer
* pdf-parse

## AI/ML

* Python
* Flask
* Scikit-learn
* SpaCy
* NLTK
* Sentence Transformers
* Ollama LLM
* Pandas
* NumPy

---

# 📁 Project Structure

```text
ai-resume-analyzer
│
├── backend
│   ├── controllers
│   ├── middleware
│   ├── models
│   ├── routes
│   ├── services
│   ├── uploads
│   ├── server.js
│   └── package.json
│
├── ai-service
│   ├── datasets
│   ├── models
│   ├── services
│   ├── training
│   ├── utils
│   ├── app.py
│   └── requirements.txt
│
├── src
│   ├── components
│   ├── pages
│   ├── routes
│   ├── services
│   ├── context
│   ├── App.jsx
│   └── main.jsx
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd ai-resume-analyzer
```

---

# 🌐 Frontend Setup

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

---

# 🖥️ Backend Setup

Go to backend folder:

```bash
cd backend
```

Install dependencies:

```bash
npm install
```

Run backend:

```bash
npm run dev
```

---

# 🧠 AI Service Setup

Go to AI service folder:

```bash
cd ai-service
```

Create virtual environment:

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install SpaCy model:

```bash
python -m spacy download en_core_web_sm
```

---

# 🤖 Ollama Setup

Install Ollama:

[https://ollama.com](https://ollama.com)

Pull model:

```bash
ollama pull phi3
```

OR:

```bash
ollama pull llama3
```

Start Ollama:

```bash
ollama serve
```

---

# ▶️ Start AI Service

```bash
python app.py
```

---

# 🧪 Machine Learning Pipeline

## Merge Datasets

```bash
python training/merge_datasets.py
```

## Train ATS Model

```bash
python training/train_ats_model.py
```

## Train Role Prediction Model

```bash
python training/train_role_model.py
```

---

# 📡 API Endpoints

## Authentication

### Register

```http
POST /api/auth/register
```

### Login

```http
POST /api/auth/login
```

---

## Resume Analysis

### Upload Resume

```http
POST /api/analyze/resume
```

---

## AI Service

### Analyze Resume

```http
POST /analyze
```

### AI Chatbot

```http
POST /chat
```

---

# 📊 AI Features Output

The AI engine provides:

* ATS Score Prediction
* Resume Skill Extraction
* Job Match Percentage
* Predicted Job Role
* AI-generated Feedback
* Resume Suggestions
* Career Recommendations

---

# 🔒 Security Features

* JWT Authentication
* Password Hashing
* Protected APIs
* Helmet Security Middleware
* Rate Limiting
* CORS Protection

---

# 📈 Future Improvements

* Resume Version Tracking
* Cloud Deployment
* Real-time Analytics
* Advanced Resume Ranking
* Multi-language Resume Support
* AI Interview Preparation
* Voice-based AI Assistant
* Docker Deployment
* CI/CD Pipelines

---

# 💡 Learning Outcomes

This project demonstrates:

* Full Stack MERN Development
* REST API Development
* Authentication & Security
* AI/ML Integration
* NLP & Semantic Search
* LLM Integration
* Python Flask Services
* Dataset Processing
* Machine Learning Model Training
* Production-style Architecture

---

# 👩‍💻 Author

Vanshika Devi

---

# ⭐ Project Highlights

* Full Stack AI Project
* Real-world Resume Intelligence System
* MERN + Python Hybrid Architecture
* AI Chatbot Integration
* Dynamic ML-driven Analysis
* Portfolio-ready Advanced Project
