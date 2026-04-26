# 🤖 AI Resume Analyzer (Full-Stack + LLM Integration)

An end-to-end full-stack application that analyzes resumes against job descriptions, computes a compatibility score, extracts technical skills, and generates actionable improvement suggestions using rule-based NLP and LLM integration.

---

## 🚀 Overview

The **AI Resume Analyzer** is designed to simulate a simplified Applicant Tracking System (ATS). It enables users to evaluate how well their resume aligns with a target job role.

The system combines:

* Deterministic logic (skill matching)
* Lightweight NLP techniques
* LLM-based suggestions (via Hugging Face APIs)

---

## 🎯 Core Features

### 📄 Resume Processing

* Upload resume files (text-based parsing)
* Lightweight preprocessing for content extraction

### 🧠 Skill Extraction Engine

* Rule-based keyword matching using predefined skill sets
* Case-insensitive detection for robustness
* Easily extendable skill dictionary

### 📊 Job Match Scoring

* Compares extracted skills with job description requirements
* Computes a percentage-based compatibility score
* Identifies:

  * ✅ Matched skills
  * ❌ Missing skills

### 💡 AI-Powered Suggestions

* Generates resume improvement suggestions
* Integrates with Hugging Face inference API (LLMs)
* Focuses on:

  * Skill gaps
  * Resume clarity
  * Industry relevance

### 💬 Career Assistant (Chat Interface)

* Interactive chat UI for career-related queries
* Designed for integration with LLM-based responses

---

## 🏗️ System Architecture

```id="arch01"
Frontend (React + Vite)
        ↓
REST API (Spring Boot)
        ↓
AI Layer
 ├── Rule-based NLP (Skill Extraction)
 └── Hugging Face API (LLM Suggestions)
```

---

## 🧰 Tech Stack

### Frontend

* React.js (Vite)
* JavaScript (ES6+)
* CSS (Custom UI + responsive layout)

### Backend

* Java 21
* Spring Boot 3.x
* RESTful API architecture

### AI / NLP

* Rule-based keyword extraction
* Hugging Face Inference API (LLM integration)

---

## 📂 Project Structure

```id="arch02"
ai-resume-analyzer/
├── backend/
│   ├── controller/        # API endpoints
│   ├── service/           # Business logic + AI integration
│   └── application.properties
│
├── frontend/
│   ├── src/
│   │   ├── components/    # UI components
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   └── package.json
```

---

## ⚙️ Local Setup

### 🔹 Backend

```bash id="run1"
cd backend
mvn spring-boot:run
```

Runs at:

```id="run2"
http://localhost:8080
```

---

### 🔹 Frontend

```bash id="run3"
cd frontend
npm install
npm run dev
```

Runs at:

```id="run4"
http://localhost:5173
```

---

## 🔗 API Specification

### POST `/analyze`

**Request:**

* Multipart file (resume)
* Job description (string)

**Response:**

```json id="api01"
{
  "score": 78,
  "skills": ["Java", "React", "SQL"],
  "missingSkills": ["Docker", "AWS"],
  "suggestions": [
    "Include cloud-based project experience",
    "Add quantified achievements",
    "Improve keyword alignment with job role"
  ]
}
```

---

## 🤖 Hugging Face Integration

The system is designed to integrate with Hugging Face models for:

* Skill extraction enhancement
* Resume feedback generation
* Natural language suggestions

Example use case:

* Sending resume + job description as prompt
* Receiving structured improvement insights

> Note: API keys are handled securely via environment variables and are not exposed in the frontend.

---

## 📈 Future Enhancements

* PDF parsing (Apache Tika / PDFBox)
* Advanced NLP (NER-based skill extraction)
* Resume scoring using semantic similarity
* Authentication & user dashboards
* Deployment (Vercel + Render / Railway)
* Persistent storage (MongoDB / PostgreSQL)

---

## 🎯 Learning Outcomes

This project demonstrates:

* Full-stack system design (React + Spring Boot)
* REST API development and integration
* Applied NLP techniques
* LLM integration in real-world workflows
* UI/UX structuring for interactive applications

---

## 👩‍💻 Author

**Vanshika Devi**
B.Tech Computer Science and Information Technology Student

---

## ⭐ Contribution / Feedback

If you find this project useful, feel free to:

* Star ⭐ the repository
* Suggest improvements
* Open issues for enhancements

---
