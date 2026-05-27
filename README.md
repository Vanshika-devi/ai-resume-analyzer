# 🚀 AI Resume Analyzer

An advanced AI-powered Resume Analyzer built using the MERN Stack, FastAPI, Machine Learning, NLP, and Phi-3 LLM integration.

The platform analyzes resumes, predicts ATS scores, extracts skills, recommends job roles, performs semantic job matching, and provides intelligent AI-generated career guidance.

---

# 🌟 Features

## 🔐 Authentication & Security

- JWT-based Authentication
- Secure User Registration & Login
- Password Hashing using bcryptjs
- Protected Routes
- Helmet Security Middleware
- Express Rate Limiting
- MongoDB Sanitization
- XSS Protection

---

# 📄 Resume Analysis Features

- PDF Resume Upload
- Resume Text Extraction
- ATS Score Prediction
- Resume Role Prediction
- Skill Extraction using NLP
- Resume Parsing
- Resume Improvement Suggestions
- Resume Skill Gap Analysis

---

# 🤖 AI Features

- Phi-3 AI Chatbot Integration using Ollama
- AI Career Guidance
- AI Resume Feedback
- AI-based Resume Optimization Suggestions
- Intelligent Career Recommendations
- Semantic Job Matching using Sentence Transformers

---

# 📊 Machine Learning Features

- Logistic Regression Role Prediction Model
- Random Forest ATS Prediction Model
- TF-IDF Vectorization
- Semantic Similarity Matching
- Dataset-driven ML Pipeline
- NLP-based Resume Processing
- Scikit-learn Model Training
- Real-time Prediction APIs

---

# 🎨 Frontend Features

- Modern Responsive UI
- Dark Professional Theme
- React + Vite Frontend
- Protected Authentication Flow
- Resume Upload Dashboard
- AI Chatbot Interface
- Dynamic Navigation
- Production-style Routing

---

# 🛠️ Tech Stack

## Frontend

- React.js
- Vite
- Tailwind CSS
- Axios
- React Router DOM
- Framer Motion

---

## Backend

- Node.js
- Express.js
- MongoDB
- Mongoose
- JWT Authentication
- Multer
- pdf-parse
- Helmet
- Express Rate Limit

---

## AI / ML Service

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Sentence Transformers
- Ollama
- Phi-3 LLM
- SpaCy

---

# 🧠 AI Architecture

```text
Frontend (React)
        │
        ▼
Node.js Backend API
        │
        ▼
FastAPI AI Service
        │
 ┌──────┼───────────────┐
 │       │                  |
 ▼      ▼                  ▼
ATS ML  Role ML           Phi-3 AI
Model   Model              Chatbot
```

---

# 📁 Project Structure

```text
ai-resume-analyzer/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── uploads/
│   ├── utils/
│   ├── .env
│   ├── package.json
│   └── server.js
│
├── ai-service/
│   ├── datasets/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── training/
│   ├── utils/
│   ├── uploads/
│   ├── venv/
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# ⚙️ Installation Guide

# 1️⃣ Clone Repository

```bash
git clone https://github.com/Vanshika-devi/ai-resume-analyzer.git

cd ai-resume-analyzer
```

---

# 🌐 Frontend Setup

```bash
npm install
```

Run Frontend:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
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

Run Backend:

```bash
npm run dev
```

Backend runs on:

```text
http://localhost:5000
```

---

# 🧠 AI Service Setup

Go to AI service folder:

```bash
cd ai-service
```

---

# Create Virtual Environment

## Windows

```bash
py -3.11 -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

# Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Install SpaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# 🤖 Ollama Setup

Install Ollama:

```text
https://ollama.com
```

Pull Phi-3 model:

```bash
ollama pull phi3
```

Start Ollama:

```bash
ollama serve
```

---

# ▶️ Start FastAPI AI Service

```bash
uvicorn app:app --reload
```

AI Service runs on:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Machine Learning Pipeline

# Merge Datasets

```bash
python -m training.merge_datasets
```

---

# Train Role Prediction Model

```bash
python -m training.train_role_model
```

---

# Train ATS Prediction Model

```bash
python -m training.train_ats_model
```

---

# Evaluate Models

```bash
python -m training.evaluate_models
```

---

# 📡 API Endpoints

# Authentication APIs

## Register User

```http
POST /api/auth/register
```

## Login User

```http
POST /api/auth/login
```

---

# Resume APIs

## Upload Resume

```http
POST /api/resume/upload
```

---

# AI Prediction APIs

## Predict ATS Score + Job Role

```http
POST /predict/resume
```

---

# AI Recommendation APIs

## Recommend Jobs

```http
POST /recommend/jobs
```

---

# AI Chatbot APIs

## Chat with Phi-3

```http
POST /chatbot/ask
```

---

# 📊 Machine Learning Models

| Model | Purpose |
|---|---|
| Logistic Regression | Job Role Prediction |
| Random Forest Regressor | ATS Score Prediction |
| Sentence Transformers | Semantic Job Matching |
| TF-IDF Vectorizer | Resume Text Processing |

---

# 🧠 Datasets Used

- AI_Resume_Screening.csv
- job_dataset.csv
- resume_dataset_1200.csv
- 06_skills.csv
- 05_person_skills.csv
- 04_experience.csv
- 03_education.csv
- 02_abilities.csv
- 01_people.csv

---

# 🔒 Security Features

- JWT Authentication
- Protected APIs
- Password Encryption
- Helmet Security
- Rate Limiting
- MongoDB Sanitization
- XSS Protection

---

# 📈 Future Improvements

- Resume vs Job Description Matching
- AI Interview Question Generator
- Resume Ranking System
- AI-powered Resume Builder
- Voice-based AI Assistant
- Cloud Deployment
- Docker Support
- CI/CD Pipeline
- Real-time Analytics Dashboard
- Advanced NLP Pipeline
- Vector Database Integration
- Multi-language Resume Analysis

---

# 💡 Learning Outcomes

This project demonstrates:

- Full Stack MERN Development
- REST API Development
- FastAPI Integration
- Authentication & Security
- Machine Learning Pipelines
- NLP & Semantic Search
- AI Chatbot Integration
- Dataset Processing
- Model Training & Evaluation
- Production-style Project Architecture

---

# 👩‍💻 Author

## Vanshika Devi

GitHub:

```text
https://github.com/Vanshika-devi
```

---

# ⭐ Project Highlights

- Full Stack AI + ML Project
- MERN + FastAPI Hybrid Architecture
- Real-world Resume Intelligence System
- Semantic AI Matching
- Phi-3 AI Chatbot
- Dataset-driven Machine Learning
- Production-style Authentication System
- Portfolio-ready Advanced Project

---

# 📜 License

This project is licensed under the MIT License.
